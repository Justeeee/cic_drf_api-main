from rest_framework.decorators import action
from rest_framework.filters import SearchFilter
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from shared.pagination import UserPagination
from user.models import User
from user.serializers import UserModelSerializer, ListUserModelSerializer, RetrieveUserModelSerializer, \
    UpdateUserModelSerializer, UserListModelSerializer


class UserModelViewSet(ModelViewSet):
    queryset = User.objects.order_by('-created_at')
    serializer_class = UserModelSerializer
    permission_classes = [AllowAny]
    parser_classes = (MultiPartParser, FormParser,)
    pagination_class = UserPagination
    lookup_url_kwarg = 'id'
    search_fields = ['id', 'first_name', 'last_name', 'slug']
    filter_backends = [SearchFilter]

    def get_serializer_class(self):
        serializer_dict = {
            'list': ListUserModelSerializer,
            'create': UserModelSerializer,
            'retrieve': RetrieveUserModelSerializer,
            'update': UpdateUserModelSerializer
        }

        return serializer_dict.get(self.action, self.serializer_class)

    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'delete']:
            self.permission_classes = [IsAuthenticated]
        else:
            self.permission_classes = [AllowAny]

        return super().get_permissions()

    @action(methods=['GET'], detail=False, url_path='list', url_name='list-user',
            serializer_class=UserListModelSerializer, pagination_class=UserPagination)
    def get(self, request):
        users = User.objects.all()
        serializer = UserListModelSerializer(users, many=True)
        return Response(serializer.data)
