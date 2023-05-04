from django.urls import path, include
from rest_framework.routers import DefaultRouter

from apps.views import BranchModelViewSet, CategoryModelViewSet, TagModelViewSet, BlogModelViewSet

router = DefaultRouter()
router.register('branch', BranchModelViewSet, 'branch')
router.register('tag', TagModelViewSet, 'tag')
router.register('category', CategoryModelViewSet, 'category')
router.register('blog', BlogModelViewSet, 'blog')

urlpatterns = [
    path('', include(router.urls)),
]
