from rest_framework import serializers
from .models import Post
from creator.models import Creator


class PostSerializer(serializers.ModelSerializer):
    """Serializer for Post model"""
    # text = serializers.SerializerMethodField()
    author = serializers.SlugRelatedField(slug_field='username', read_only=True)
    class Meta:
        model = Post
        fields = '__all__'

    # def get_text(self, obj):
    #     a = 500  # limiting the number of visible characters
    #     return obj.text[:a] + '...' if len(obj.text) > a else obj.text
