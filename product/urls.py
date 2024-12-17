from django.urls import path, include
from rest_framework.routers import DefaultRouter
from product.views import *


urlpatterns = [
    path('', ProductListView.as_view()),
    path('detail/', ProductDetailView.as_view()), 
    path('delete/', ProductDeleteView.as_view()), 
    path('create/', ProductCreateView.as_view()), 
    path('update/', ProductUpdateView.as_view()), 
    path('forecast/', ProductForecastView.as_view()),

]
