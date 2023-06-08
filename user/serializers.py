from django.shortcuts import render
from rest_framework.serializers import ModelSerializer

from user.models import User


# Create your serializers here.
class UserModelSerializer(ModelSerializer):
    class Meta:
        model = User
        exclude = ('slug', )


class ListUserModelSerializer(ModelSerializer):
    direction = UserModelSerializer(read_only=True)

    """
    List all USERS command GET
    """

    class Meta:
        model = User
        fields = ('id', 'first_name','last_name', 'direction')


class UserListModelSerializer(ModelSerializer):
    direction = UserModelSerializer(read_only=True)

    class Meta:
        model = User
        exclude = ('slug', )


class CreateUserModelSerializer(ModelSerializer):
    direction = UserModelSerializer(read_only=True)
    """
     Create User POST
    """

    class Meta:
        model = User
        exclude = ('slug','created_at', 'updated_at')


class UpdateUserModelSerializer(ModelSerializer):
    """
        Update User obj/{id}  PUT/PATCH
    """
    class Meta:
        model = User
        exclude = ('slug', 'created_at', 'updated_at')


class RetrieveUserModelSerializer(ModelSerializer):
    direction = UserModelSerializer(read_only=True)

    """
        GET ONE USER obj/{id} RETRIEVE
    """

    class Meta:
        model = User
        fields = ('id', 'first_name','last_name', 'direction')
