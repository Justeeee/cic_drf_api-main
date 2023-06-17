from django.shortcuts import render
from rest_framework.serializers import ModelSerializer

from apps.models import Author


# Create your serializers here.
class AuthorModelSerializer(ModelSerializer):
    class Meta:
        model = Author
        exclude = ('slug',)


class ListAuthorModelSerializer(ModelSerializer):
    direction = AuthorModelSerializer(read_only=True)

    """
    List all CREATORS command GET
    """

    class Meta:
        model = Author
        fields = ('id', 'first_name', 'last_name', 'direction')


class AuthorListModelSerializer(ModelSerializer):
    direction = AuthorModelSerializer(read_only=True)

    class Meta:
        model = Author
        exclude = ('slug', )


class CreateAuthorModelSerializer(ModelSerializer):
    direction = AuthorModelSerializer(read_only=True)
    """
     Create Author POST
    """

    class Meta:
        model = Author
        exclude = ('slug', 'created_at', 'updated_at')


class UpdateAuthorModelSerializer(ModelSerializer):
    """

    Update Author obj/{id}  PUT/PATCH

    """

    class Meta:
        model = Author
        exclude = ('slug', 'created_at', 'updated_at')


class RetrieveAuthorModelSerializer(ModelSerializer):
    direction = AuthorModelSerializer(read_only=True)

    """
        GET ONE CREATOR obj/{id} RETRIEVE
    """

    class Meta:
        model = Author
        fields = ('id',  'first_name', 'last_name', 'direction')
