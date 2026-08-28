from django.db import models


# Create your models here.
class Topic(models.Model):
    """A topic the user is learning about"""

    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return a string representation of the model."""
        return self.text


class Entry(models.Model):
    """Something specific learned about a topic."""

    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "entries"

    def __str__(self):
        """Return a string Representing the model."""
        bar = self.text
        if bar > 50:
            return f"{bar[:50]}..."
        else:
            return bar
        


        # How to add if statement in django 
        # if self.text > 50:
        #     return foo
        # else:
        #     return foo 
         