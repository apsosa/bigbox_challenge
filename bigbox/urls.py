"""bigbox URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
import debug_toolbar
from rest_framework import routers
from quickstart import views
from graphene_django.views import GraphQLView
from django.views.decorators.csrf import csrf_exempt
from .schema import schema
from django.conf.urls import url, include

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)



urlpatterns = [
    path('', include(router.urls)),
    path('snippets/', include('snippets.urls')),
    #path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
    path('api/', include('core.api.urls')),
    path('/api-auth/', include('rest_framework.urls')),
    url(r'^graphql$', GraphQLView.as_view(graphiql=True)),
    #path("graphql", csrf_exempt(GraphQLView.as_view(graphiql=True, schema=schema))),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


if settings.DEBUG:
    urlpatterns += path('__debug__/',include(debug_toolbar.urls)),