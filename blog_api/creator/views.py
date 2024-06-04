from rest_framework import viewsets
from .models import Creator
from .serializers import CreatorSerializer

class CreatorView(viewsets.ModelViewSet):
    """View for Creator model"""
    queryset = Creator.objects.all()
    serializer_class = CreatorSerializer
