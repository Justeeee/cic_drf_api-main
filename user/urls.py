from django.conf.urls.static import static
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from user.views import UserModelViewSet

router = DefaultRouter()
router.register('user', UserModelViewSet)

urlpatterns = [
    path('', include(router.urls)),
    # path('get-count/', GetCountAPIView.as_view())
]
