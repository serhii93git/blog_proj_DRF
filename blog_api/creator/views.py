from rest_framework import viewsets
from .models import Creator
from .serializers import CreatorSerializer
from rest_framework.permissions import IsAuthenticated


class CreatorView(viewsets.ModelViewSet):
    """View for Creator model"""

    serializer_class = CreatorSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """Get current creator only"""
        return Creator.objects.filter(id=self.request.user.id)
