from django.shortcuts import render
from rest_framework.serializers import ModelSerializer

from apps.models import Branch


# Create your serializers here.
class BranchModelSerializer(ModelSerializer):
    class Meta:
        model = Branch
        exclude = ('slug', )


class ListBranchModelSerializer(ModelSerializer):
    direction = BranchModelSerializer(read_only=True)

    """
    List all BRANCHS command GET
    """

    class Meta:
        model = Branch
        fields = ('id', 'name', 'direction')


class BranchListModelSerializer(ModelSerializer):
    direction = BranchModelSerializer(read_only=True)

    class Meta:
        model = Branch
        exclude = ('slug', )


class CreateBranchModelSerializer(ModelSerializer):
    direction = BranchModelSerializer(read_only=True)
    """
     Create Branch POST
    """

    class Meta:
        model = Branch
        exclude = ('slug','created_at', 'updated_at')


class UpdateBranchModelSerializer(ModelSerializer):
    """

    Update Branch obj/{id}  PUT/PATCH

    """

    class Meta:
        model = Branch
        exclude = ('slug','created_at', 'updated_at')


class RetrieveBranchModelSerializer(ModelSerializer):
    direction = BranchModelSerializer(read_only=True)

    """
        GET ONE BRANCH obj/{id} RETRIEVE
    """

    class Meta:
        model = Branch
        fields = ('id', 'name', 'direction')
