from rest_framework import serializers
from .models import Post


class PostSerializer(serializers.ModelSerializer):
    """ Post Serializer class """
    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'author', 'category', 'likes', 'likes_count']