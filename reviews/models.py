from django.db import models
from tracks.models import Track
from django.contrib.auth.models import User


class Review(models.Model):
    track = models.ForeignKey(
        Track, related_name='reviews', on_delete=models.CASCADE)
    reviewer = models.ForeignKey(
        User, related_name='reviews', on_delete=models.CASCADE)
    feedback = models.TextField()  # Review comments/feedback
    reviewed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review for {self.track.title} by {self.reviewer.username}"
