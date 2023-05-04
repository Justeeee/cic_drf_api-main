from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.parsers import MultiPartParser
from rest_framework.viewsets import ModelViewSet

from apps.models import Branch, Category, Blog, Tag
from apps.serializers import BranchModelSerializer, CategoryModelSerializer, BlogModelSerializer, \
    TagModelSerializer


class BranchModelViewSet(ModelViewSet):
    queryset = Branch.objects.all()
    serializer_class = BranchModelSerializer
    filter_backends = (DjangoFilterBackend,)
    parser_classes = (MultiPartParser,)
    filterset_fields = ('name',)
    # permission_classes = (~IsAuthenticated, )
    # permission_classes = (NOT(IsAuthenticated), )
    # search_fields = ('name', )


class CategoryModelViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategoryModelSerializer


class TagModelViewSet(ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagModelSerializer


class BlogModelViewSet(ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogModelSerializer


