from rest_framework import serializers
from .models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(
        source="owner.username")

    class Meta:
        model = Profile
        fields = ['id', 'owner',
                  'display_name', 'bio', 'avatar', 'is_editor']
