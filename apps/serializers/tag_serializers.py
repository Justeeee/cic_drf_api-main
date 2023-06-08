from django.shortcuts import render
from rest_framework.serializers import ModelSerializer

from apps.models import Tag


# Create your serializers here.
class TagModelSerializer(ModelSerializer):
    class Meta:
        model = Tag
        exclude = ('slug', )


class ListTagModelSerializer(ModelSerializer):
    direction = TagModelSerializer(read_only=True)

    """
    List all TAGS command GET
    """

    class Meta:
        model = Tag
        fields = ('id', 'name', 'direction')


class TagListModelSerializer(ModelSerializer):
    direction = TagModelSerializer(read_only=True)

    class Meta:
        model = Tag
        exclude = ('slug',)


class CreateTagModelSerializer(ModelSerializer):
    direction = TagModelSerializer(read_only=True)
    """
     Create Tag POST
    """

    class Meta:
        model = Tag
        exclude = ('slug','created_at', 'updated_at')


class UpdateTagModelSerializer(ModelSerializer):
    """

    Update Tag obj/{id}  PUT/PATCH

    """

    class Meta:
        model = Tag
        exclude = ('slug','created_at', 'updated_at')


class RetrieveTagModelSerializer(ModelSerializer):
    direction = TagModelSerializer(read_only=True)

    """
        GET ONE TAG obj/{id} RETRIEVE
    """

    class Meta:
        model = Tag
        fields = ('id', 'name', 'direction')