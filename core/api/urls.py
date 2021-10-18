from django.urls import path
from django.urls.resolvers import URLPattern
from core.api.api import ActivityAPIView, BoxAPIView, CategoryAPIView

urlpatterns = [
    path('activities/',ActivityAPIView.as_view(), name='activities_api'),
    path('boxes/',BoxAPIView.as_view(), name='boxes_api'),
    path('category/',CategoryAPIView.as_view(), name='categories_api'),
]