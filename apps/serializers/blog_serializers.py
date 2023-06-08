from django.shortcuts import render
from rest_framework.serializers import ModelSerializer

from apps.models import Blog


# Create your serializers here.
class BlogModelSerializer(ModelSerializer):
    class Meta:
        model = Blog
        exclude = ('slug',)


class ListBlogModelSerializer(ModelSerializer):
    direction = BlogModelSerializer(read_only=True)

    """
    List all BLOGS command GET
    """

    class Meta:
        model = Blog
        fields = ('id', 'title', 'text', 'branch', 'tag', 'author', 'direction')


class BlogListModelSerializer(ModelSerializer):
    direction = BlogModelSerializer(read_only=True)

    class Meta:
        model = Blog
        exclude = ('slug',)


class CreateBlogModelSerializer(ModelSerializer):
    direction = BlogModelSerializer(read_only=True)
    """
     Create Blog POST
    """

    class Meta:
        model = Blog
        exclude = ('slug','created_at', 'updated_at')


class UpdateBlogModelSerializer(ModelSerializer):
    """

    Update Blog obj/{id}  PUT/PATCH

    """

    class Meta:
        model = Blog
        exclude = ('slug','created_at', 'updated_at')


class RetrieveBlogModelSerializer(ModelSerializer):
    direction = BlogModelSerializer(read_only=True)

    """
        GET ONE BLOG obj/{id} RETRIEVE
    """

    class Meta:
        model = Blog
        fields = ('id', 'title', 'text', 'branch', 'tag', 'author', 'direction')
