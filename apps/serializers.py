from rest_framework.serializers import ModelSerializer

from apps.models import Branch, Category, Blog, Tag


class BranchModelSerializer(ModelSerializer):
    class Meta:
        model = Branch
        fields = '__all__'


class CategoryModelSerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class BlogModelSerializer(ModelSerializer):
    class Meta:
        model = Blog
        fields = '__all__'


class TagModelSerializer(ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'


