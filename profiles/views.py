from .serializers import ProfileSerializer
from rest_framework import generics
from .models import Profile
from mp_api.permissions import IsOwnerOrReadOnly
from rest_framework.permissions import IsAuthenticated


class ProfileList(generics.ListAPIView):
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
    queryset = Profile.objects.all()


class ProfileDetail(generics.RetrieveUpdateAPIView):
    serializer_class = ProfileSerializer
    # Ensure user is authenticated and owner
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
    queryset = Profile.objects.all()

    def get_queryset(self):
        """
        Only the authenticated user can access their own profile.
        """
        return self.queryset.filter(owner=self.request.user)
