from rest_framework import serializers
from .models import Creator
from post.serializers import PostSerializer


class CreatorSerializer(serializers.ModelSerializer):
    """Serializer for Creator model"""
    posts = serializers.SerializerMethodField()

    class Meta:
        model = Creator
        fields = ('id', 'username', 'first_name', 'last_name', 'email', 'date_joined', 'creator_image', 'posts')

    def get_posts(self, obj):
        posts = obj.post_set.all()
        return PostSerializer(posts, many=True).data
