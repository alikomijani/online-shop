from django.urls import path
from .views import AddressViewSet, register, profile
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from rest_framework import routers
router = routers.SimpleRouter()
router.register(r'address', AddressViewSet)
urlpatterns = [
    path('register/', register, name='register'),
    path('profile/', profile, name='profile'),
    path('login/', TokenObtainPairView.as_view(),
         name='login'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
] + router.urls
