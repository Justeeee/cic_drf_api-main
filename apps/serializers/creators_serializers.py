from django.shortcuts import render
from rest_framework.serializers import ModelSerializer

from apps.models import Creators


# Create your serializers here.
class CreatorsModelSerializer(ModelSerializer):
    class Meta:
        model = Creators
        exclude = ('slug',)


class ListCreatorsModelSerializer(ModelSerializer):
    direction = CreatorsModelSerializer(read_only=True)

    """
    List all CREATORS command GET
    """

    class Meta:
        model = Creators
        fields = ('id', 'first_name', 'last_name', 'direction')


class CreatorsListModelSerializer(ModelSerializer):
    direction = CreatorsModelSerializer(read_only=True)

    class Meta:
        model = Creators
        exclude = ('slug', )


class CreateCreatorsModelSerializer(ModelSerializer):
    direction = CreatorsModelSerializer(read_only=True)
    """
     Create Creators POST
    """

    class Meta:
        model = Creators
        exclude = ('slug', 'created_at', 'updated_at')


class UpdateCreatorsModelSerializer(ModelSerializer):
    """

    Update Creators obj/{id}  PUT/PATCH

    """

    class Meta:
        model = Creators
        exclude = ('slug', 'created_at', 'updated_at')


class RetrieveCreatorsModelSerializer(ModelSerializer):
    direction = CreatorsModelSerializer(read_only=True)

    """
        GET ONE CREATOR obj/{id} RETRIEVE
    """

    class Meta:
        model = Creators
        fields = ('id',  'first_name', 'last_name', 'direction')
