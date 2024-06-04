from rest_framework import serializers
from creator.models import Creator


class CreatorSerializer(serializers.ModelSerializer):
    """Serializer for Creator model"""

    class Meta:
        model = Creator
        fields = ('username', 'first_name', 'last_name', 'email', 'date_joined', 'creator_image')
