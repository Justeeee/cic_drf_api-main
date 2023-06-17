from rest_framework.decorators import action
from rest_framework.filters import SearchFilter
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from apps.serializers.author_serializers import AuthorModelSerializer, ListAuthorModelSerializer, \
    RetrieveAuthorModelSerializer, UpdateAuthorModelSerializer, AuthorListModelSerializer
from apps.serializers.blog_serializers import BlogModelSerializer, ListBlogModelSerializer, RetrieveBlogModelSerializer, \
    UpdateBlogModelSerializer, BlogListModelSerializer
from apps.serializers.branch_serializers import BranchListModelSerializer, UpdateBranchModelSerializer, \
    RetrieveBranchModelSerializer, BranchModelSerializer, ListBranchModelSerializer
from apps.serializers.creators_serializers import CreatorsModelSerializer, ListCreatorsModelSerializer, \
    RetrieveCreatorsModelSerializer, UpdateCreatorsModelSerializer, CreatorsListModelSerializer
from apps.serializers.tag_serializers import TagListModelSerializer, ListTagModelSerializer, TagModelSerializer, \
    RetrieveTagModelSerializer, UpdateTagModelSerializer
from shared.pagination import BlogPagination, TagPagination, BranchPagination, CreatorsPagination, AuthorPagination
from apps.models import Blog, Tag, Branch, Creators, Author


class BlogModelViewSet(ModelViewSet):
    queryset = Blog.objects.order_by('-created_at')
    serializer_class = BlogModelSerializer
    permission_classes = [AllowAny]
    parser_classes = (MultiPartParser, FormParser,)
    pagination_class = BlogPagination
    lookup_url_kwarg = 'id'
    search_fields = ['id', 'first_name', 'last_name']
    filter_backends = [SearchFilter]

    def get_serializer_class(self):
        serializer_dict = {
            'list': ListBlogModelSerializer,
            'create': BlogModelSerializer,
            'retrieve': RetrieveBlogModelSerializer,
            'update': UpdateBlogModelSerializer
        }

        return serializer_dict.get(self.action, self.serializer_class)

    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'delete']:
            self.permission_classes = [IsAuthenticated]
        else:
            self.permission_classes = [AllowAny]

        return super().get_permissions()

    @action(methods=['GET'], detail=False, url_path='list', url_name='list-blog',
            serializer_class=BlogListModelSerializer, pagination_class=BlogPagination)
    def get(self, request):
        blogs = Blog.objects.all()
        serializer = BlogListModelSerializer(blogs, many=True)
        return Response(serializer.data)


class TagModelViewSet(ModelViewSet):
    queryset = Tag.objects.order_by('-created_at')
    serializer_class = TagModelSerializer
    permission_classes = [AllowAny]
    parser_classes = (MultiPartParser, FormParser,)
    pagination_class = TagPagination
    lookup_url_kwarg = 'id'
    search_fields = ['id', 'first_name', 'last_name']
    filter_backends = [SearchFilter]

    def get_serializer_class(self):
        serializer_dict = {
            'list': ListTagModelSerializer,
            'create': TagModelSerializer,
            'retrieve': RetrieveTagModelSerializer,
            'update': UpdateTagModelSerializer
        }

        return serializer_dict.get(self.action, self.serializer_class)

    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'delete']:
            self.permission_classes = [IsAuthenticated]
        else:
            self.permission_classes = [AllowAny]

        return super().get_permissions()

    @action(methods=['GET'], detail=False, url_path='list', url_name='list-tag',
            serializer_class=TagListModelSerializer, pagination_class=TagPagination)
    def get(self, request):
        tags = Tag.objects.all()
        serializer = TagListModelSerializer(tags, many=True)
        return Response(serializer.data)


class BranchModelViewSet(ModelViewSet):
    queryset = Branch.objects.order_by('-created_at')
    serializer_class = BranchModelSerializer
    permission_classes = [AllowAny]
    parser_classes = (MultiPartParser, FormParser,)
    pagination_class = BranchPagination
    lookup_url_kwarg = 'id'
    search_fields = ['id', 'first_name', 'last_name']
    filter_backends = [SearchFilter]

    def get_serializer_class(self):
        serializer_dict = {
            'list': ListBranchModelSerializer,
            'create': BranchModelSerializer,
            'retrieve': RetrieveBranchModelSerializer,
            'update': UpdateBranchModelSerializer
        }

        return serializer_dict.get(self.action, self.serializer_class)

    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'delete']:
            self.permission_classes = [IsAuthenticated]
        else:
            self.permission_classes = [AllowAny]

        return super().get_permissions()

    @action(methods=['GET'], detail=False, url_path='list', url_name='list-tag',
            serializer_class=BranchListModelSerializer, pagination_class=BranchPagination)
    def get(self, request):
        branches = Branch.objects.all()
        serializer = BranchListModelSerializer(branches, many=True)
        return Response(serializer.data)


class CreatorModelViewSet(ModelViewSet):
    queryset = Creators.objects.order_by('-created_at')
    serializer_class = CreatorsModelSerializer
    permission_classes = [AllowAny]
    parser_classes = (MultiPartParser, FormParser,)
    pagination_class = CreatorsPagination
    lookup_url_kwarg = 'id'
    search_fields = ['id', 'first_name', 'last_name']
    filter_backends = [SearchFilter]

    def get_serializer_class(self):
        serializer_dict = {
            'list': ListCreatorsModelSerializer,
            'create': CreatorsModelSerializer,
            'retrieve': RetrieveCreatorsModelSerializer,
            'update': UpdateCreatorsModelSerializer
        }

        return serializer_dict.get(self.action, self.serializer_class)

    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'delete']:
            self.permission_classes = [IsAuthenticated]
        else:
            self.permission_classes = [AllowAny]

        return super().get_permissions()

    @action(methods=['GET'], detail=False, url_path='list', url_name='list-tag',
            serializer_class=CreatorsListModelSerializer, pagination_class=CreatorsPagination)
    def get(self, request):
        branches = Branch.objects.all()
        serializer = BranchListModelSerializer(branches, many=True)
        return Response(serializer.data)


class AuthorModelViewSet(ModelViewSet):
    queryset = Author.objects.order_by('-created_at')
    serializer_class = AuthorModelSerializer
    permission_classes = [AllowAny]
    parser_classes = (MultiPartParser, FormParser,)
    pagination_class = AuthorPagination
    lookup_url_kwarg = 'id'
    search_fields = ['id', 'first_name', 'last_name']
    filter_backends = [SearchFilter]

    def get_serializer_class(self):
        serializer_dict = {
            'list': ListAuthorModelSerializer,
            'create': AuthorModelSerializer,
            'retrieve': RetrieveAuthorModelSerializer,
            'update': UpdateAuthorModelSerializer
        }

        return serializer_dict.get(self.action, self.serializer_class)

    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'delete']:
            self.permission_classes = [IsAuthenticated]
        else:
            self.permission_classes = [AllowAny]

        return super().get_permissions()

    @action(methods=['GET'], detail=False, url_path='list', url_name='list-tag',
            serializer_class=AuthorListModelSerializer, pagination_class=AuthorPagination)
    def get(self, request):
        branches = Branch.objects.all()
        serializer = BranchListModelSerializer(branches, many=True)
        return Response(serializer.data)
