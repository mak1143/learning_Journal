from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse


class AuthenticationViewTests(TestCase):
	def setUp(self):
		self.user = User.objects.create_user(
			username="testuser",
			password="testpass123",
		)

	def test_logout_rejects_get_requests(self):
		self.client.force_login(self.user)

		response = self.client.get(reverse("users:logout"))

		self.assertEqual(response.status_code, 405)
		self.assertTrue(response.wsgi_request.user.is_authenticated)

	def test_logout_accepts_post_requests(self):
		self.client.force_login(self.user)

		response = self.client.post(reverse("users:logout"))

		self.assertEqual(response.status_code, 200)
		self.assertTemplateUsed(response, "registration/logged_out.html")
		self.assertFalse(response.wsgi_request.user.is_authenticated)
