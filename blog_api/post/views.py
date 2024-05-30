from rest_framework import viewsets
from .models import Post
from .serializers import PostSerializer


class PostViewSet(viewsets.ModelViewSet):
    """View for Post model"""

    queryset = Post.objects.all()
    serializer_class = PostSerializer

