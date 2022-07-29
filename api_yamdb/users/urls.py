from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import UserViewSet, SignUpViewSet, TokenViewSet

app_name = 'users'

router_v1 = DefaultRouter()
router_v1.register('users', UserViewSet, basename='users')
router_v1.register('auth/signup', SignUpViewSet, basename='sign-up')
router_v1.register('auth/token', TokenViewSet, basename='token')

urlpatterns = [
    path('', include(router_v1.urls)),
]
