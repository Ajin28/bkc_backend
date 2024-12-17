from django.urls import path, include
from user.views import *
# from rest_framework.routers import DefaultRouter
# from common.views import UserViewSet, ProductViewSet

# router = DefaultRouter()
# router.register(r'users', UserViewSet, basename='user')
# router.register(r'products', ProductViewSet, basename='product')

urlpatterns = [
    path('register/', RegisterAPIView.as_view()),
    path('login/', LoginAPIView.as_view()),
]
