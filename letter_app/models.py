from django.db import models

from django.contrib.auth.models import User

# Create your models here.

# My models

class Message(models.Model):
    """A message that user can write."""
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        # to print id, user, and text message on admin page.
        if len(self.text) >= 50:
            return str(self.id) + " | " + str(self.owner) + " | " + self.text[:50] + " ..."
        else:
            return str(self.id) + " | " + str(self.owner) + " | " + self.text
