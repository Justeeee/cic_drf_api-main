from django.urls import path, include
from rest_framework.routers import DefaultRouter

from apps.views import BlogModelViewSet, BranchModelViewSet, TagModelViewSet, CreatorModelViewSet, AuthorModelViewSet

# from apps.views import BranchModelViewSet, CategoryModelViewSet, TagModelViewSet, BlogModelViewSet

router = DefaultRouter()
router.register('branch', BranchModelViewSet)
router.register('blog', BlogModelViewSet)
router.register('creator', CreatorModelViewSet)
router.register('author', AuthorModelViewSet)
router.register('tag', TagModelViewSet)

urlpatterns = [
    path('', include(router.urls)),
    # path('get-count/', GetCountAPIView.as_view())
]