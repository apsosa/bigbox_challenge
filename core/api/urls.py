from django.urls import path,re_path
from django.urls.resolvers import URLPattern
from core.api.api import  ActivityAPIView, BoxAPIView, CategoryAPIView,ActivitySlugAPIView,BoxSlugAPIView,CategorySlugAPIView

urlpatterns = [
    path('activities/',ActivityAPIView.as_view(), name='activities_api'),
    path('activities/<slug>/',ActivitySlugAPIView.as_view(), name='activities_slug_api'),
    path('boxes/',BoxAPIView.as_view(), name='boxes_api'),
    path('boxes/<slug>/',BoxSlugAPIView.as_view(), name='boxes_slug_api'),
    path('category/',CategoryAPIView.as_view(), name='categories_api'),
    path('category/<slug>/',CategorySlugAPIView.as_view(), name='categories_slug_api'),
]