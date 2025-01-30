from rest_framework import serializers
from .models import Track, Instrument
from albums.models import Album


class TrackSerializer(serializers.ModelSerializer):
    album = serializers.PrimaryKeyRelatedField(
        queryset=Album.objects.all(), allow_null=True, required=False
    )
    instruments = serializers.PrimaryKeyRelatedField(
        queryset=Instrument.objects.all(), many=True, required=False
    )
    assigned_user = serializers.StringRelatedField()  # Display username instead of ID

    class Meta:
        model = Track
        fields = '__all__'  # Includes all fields
