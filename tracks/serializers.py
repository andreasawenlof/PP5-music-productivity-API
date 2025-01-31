from rest_framework import serializers
from .models import Track, Genre, Mood
from instruments.models import Instrument
from albums.models import Album
from albums.serializers import AlbumSerializer  # Import the AlbumSerializer


class TrackSerializer(serializers.ModelSerializer):
    # Use AlbumSerializer to show album details
    album = serializers.PrimaryKeyRelatedField(
        queryset=Album.objects.all(), required=False)
    album_title = serializers.StringRelatedField(
        source='album', read_only=True)
    instruments = serializers.SlugRelatedField(
        queryset=Instrument.objects.all(), slug_field='name', many=True)

    assigned_composers = serializers.SlugRelatedField(
        many=True, read_only=True, slug_field='username'
    )  # Shows assigned composers' names

    assigned_reviewer = serializers.ReadOnlyField(
        source='assigned_reviewer.username'
    )  # Shows reviewer's name

    genre = serializers.SlugRelatedField(
        queryset=Genre.objects.all(), slug_field='name')
    mood = serializers.SlugRelatedField(
        queryset=Mood.objects.all(), slug_field='name')

    class Meta:
        model = Track
        fields = [
            'id', 'title', 'notes', 'status', 'project_type',
            'genre', 'mood', 'album', 'instruments',
            'assigned_composers', 'assigned_reviewer',
            'created_at', 'updated_at'
        ]
        read_only_fields = ['created_at', 'updated_at']
