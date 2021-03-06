
from django.db.models import manager
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import pagination
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework.pagination import PageNumberPagination,LimitOffsetPagination
from rest_framework.views import APIView
from rest_framework import filters
from core.models import Activity, Box,Category,Reason
from core.api.serializers import ActivitySerializer,BoxSerializer,CategorySerializer


class ActivityAPIView(APIView):
    def get(self,request):
        params = []
        for p in request.query_params.lists():
            params.append(p)

        if len(params) == 0: #No parameters
            pg = LimitOffsetPagination()
            activities = Activity.objects.all()
            page_roles = pg.paginate_queryset(queryset=activities, request=request, view=self)
            activities_serializer = ActivitySerializer(instance=page_roles,many=True)
            return Response(activities_serializer.data)
        
        elif len(params) > 1: #multiple parameters
            data = Activity.objects.filter(id = params[0])
            activities = Activity.objects.filter(slug=params[0])
            activities_serializer = ActivitySerializer(activities,many=True)
            return Response(activities_serializer.data)
        
        elif request.query_params.get('box_slug') != None:
            box_slug = request.query_params.get('box_slug')
            activities = Activity.objects.filter(slug=box_slug)
            activities_serializer = ActivitySerializer(activities,many=True)
            return Response(activities_serializer.data)
        
        elif request.query_params.get('category_id') != None:
            category_id = request.query_params.get('category_id')
            activities = Activity.objects.filter(category_id=category_id)
            activities_serializer = ActivitySerializer(activities,many=True)
            return Response(activities_serializer.data)

        elif request.query_params.get('reason_id') != None:
            reason_id = request.query_params.get('reason_id')
            reason = Reason.objects.filter(id=reason_id)
            activities = Activity.objects.filter(reasons__in=reason)
            activities_serializer = ActivitySerializer(activities,many=True)
            return Response(activities_serializer.data)

    def post(self,request):
        activities_serializer = ActivitySerializer(data=request.data)
        if activities_serializer.is_valid():
            activities_serializer.save()
        return Response({"Success": "Activity '{}' created successfully".format(activities_serializer.field_name)})


class ActivitySlugAPIView(APIView):
    def get(self,request,slug): #slug in a url
        activities = Activity.objects.filter(slug=slug)
        activities_serializer = ActivitySerializer(activities,many=True)
        return Response(activities_serializer.data)


class BoxAPIView(APIView):
    def get(self,request):
        params = []
        for p in request.query_params.lists(): 
            params.append(p)
        if len(params) == 0: #No parameters
            boxes = Box.objects.all()
            boxes_serializer = BoxSerializer(boxes,many=True)
            return Response(boxes_serializer.data)
        
        elif request.query_params.get('slug') != None: #slug as a paremeter
            box_slug = request.query_params.get('slug')
            boxes = Box.objects.filter(slug=box_slug)
            boxes_serializer = BoxSerializer(boxes,many=True)
            return Response(boxes_serializer.data)
        
class BoxSlugAPIView(APIView):
    def get(self,request,slug): #slug in a url
        boxes = Box.objects.filter(slug=slug)
        boxes_serializer = BoxSerializer(boxes,many=True)
        return Response(boxes_serializer.data)

class CategoryAPIView(APIView):
    def get(self,request):
        params = []
        for p in request.query_params.lists(): 
            params.append(p)
        if len(params) == 0: #No parameters
            categories = Category.objects.all()
            categories_serializer = CategorySerializer(categories,many=True)
            return Response(categories_serializer.data)

        elif request.query_params.get('slug') != None: #slug as a paremeter
            box_slug = request.query_params.get('slug')
            boxes = Category.objects.filter(slug=box_slug)
            boxes_serializer = CategorySerializer(boxes,many=True)
            return Response(boxes_serializer.data)


class CategorySlugAPIView(APIView):
    def get(self,request,slug):
        categories = Category.objects.filter(slug=slug)
        categories_serializer = CategorySerializer(categories,many=True)
        return Response(categories_serializer.data)

