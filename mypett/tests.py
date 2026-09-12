from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from .models import Entry, Topic


class LearningJournalViewTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser",
            password="testpass123",
        )
        self.client.login(username="testuser", password="testpass123")
        self.topic = Topic.objects.create(text="Django", owner=self.user)
        self.entry = Entry.objects.create(
            topic=self.topic,
            text="Learning Django views",
        )

    def test_new_topic_is_owned_by_logged_in_user(self):
        response = self.client.post(
            reverse("mypett:new_topic"),
            {"text": "Testing"},
        )

        self.assertRedirects(response, reverse("mypett:topics"))
        self.assertTrue(Topic.objects.filter(text="Testing", owner=self.user).exists())

    def test_topic_page_displays_topic_and_entry(self):
        response = self.client.get(reverse("mypett:topic", args=[self.topic.id]))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Topic: Django")
        self.assertContains(response, self.entry.text)

    def test_new_entry_page_renders(self):
        response = self.client.get(reverse("mypett:new_entry", args=[self.topic.id]))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "mypett/new_entry.html")

    def test_new_entry_is_created(self):
        response = self.client.post(
            reverse("mypett:new_entry", args=[self.topic.id]),
            {"text": "Learning Django forms"},
        )

        self.assertRedirects(
            response,
            reverse("mypett:topic", args=[self.topic.id]),
        )
        self.assertTrue(
            Entry.objects.filter(
                topic=self.topic,
                text="Learning Django forms",
            ).exists()
        )

    def test_edit_entry_page_renders(self):
        response = self.client.get(reverse("mypett:edit_entry", args=[self.entry.id]))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "mypett/edit_entry.html")
        self.assertContains(response, self.entry.text)

    def test_edit_entry_is_updated(self):
        response = self.client.post(
            reverse("mypett:edit_entry", args=[self.entry.id]),
            {"text": "Updated Django entry"},
        )

        self.assertRedirects(
            response,
            reverse("mypett:topic", args=[self.topic.id]),
        )
        self.entry.refresh_from_db()
        self.assertEqual(self.entry.text, "Updated Django entry")

    def test_invalid_edit_keeps_form_page(self):
        response = self.client.post(
            reverse("mypett:edit_entry", args=[self.entry.id]),
            {"text": ""},
        )

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "mypett/edit_entry.html")
        self.assertContains(response, "This field is required.")

    def test_other_user_cannot_edit_entry(self):
        other_user = User.objects.create_user(
            username="otheruser",
            password="otherpass123",
        )
        self.client.force_login(other_user)

        response = self.client.get(reverse("mypett:edit_entry", args=[self.entry.id]))

        self.assertEqual(response.status_code, 404)
