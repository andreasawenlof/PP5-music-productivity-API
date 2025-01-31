from django.db import models
from django.contrib.auth.models import User
from albums.models import Album
from profiles.models import Profile


class Genre(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Mood(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Track(models.Model):
    title = models.CharField(max_length=255, blank=False, null=False)
    notes = models.TextField(blank=True, default="")
    status = models.CharField(
        max_length=20, choices=[
            ('in_progress', 'In Progress'),
            ('review', 'Ready for Review'),
            ('completed', 'Completed and Reviewed'),
        ],
        default='in_progress', blank=False, null=False
    )
    project_type = models.CharField(
        max_length=20, choices=[
            ('quantity', 'Quantity'),
            ('quality', 'Quality'),
            ('custom', 'Custom Work'),
            ('other', 'Other'),
        ],
        default='quantity', blank=False, null=False
    )

    genre = models.ForeignKey(
        Genre, on_delete=models.SET_NULL, null=True, blank=True, related_name='tracks')
    mood = models.ForeignKey(
        Mood, on_delete=models.SET_NULL, null=True, blank=True, related_name='tracks')

    album = models.ForeignKey(Album, on_delete=models.SET_NULL,
                              null=True, blank=True, related_name='album_tracks')
    instruments = models.ManyToManyField(
        'Instrument', blank=True, related_name='instrument_tracks')

    assigned_composers = models.ManyToManyField(
        Profile, blank=True, related_name="assigned_tracks"
    )

    assigned_reviewer = models.ForeignKey(
        Profile, on_delete=models.SET_NULL, null=True, blank=True, related_name="assigned_reviews"
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-updated_at']  # ✅ Sorting latest updated first

    def __str__(self):
        return f"{self.title} - {self.status} ({self.project_type})"
