
from django.db.models import manager
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework.serializers import Serializer
from rest_framework.views import APIView
from rest_framework import status,generics,filters,viewsets
from core import api
from core.models import Activity, Box,Category,Reason
from core.api.serializers import ActivitySerializer,BoxSerializer,CategorySerializer


class ActivityAPIView(APIView):
    def get(self,request):
        #filter_backends = [DjangoFilterBackend]
        #filterset_fields = ['category']
        filter_backends = [filters.SearchFilter]
        search_fields = ['name', 'slug']
        params = []
        for p in request.query_params.lists():
            params.append(p)

        if len(params) == 0: #No parameters
            print("return all")
            activities = Activity.objects.all()
            activities_serializer = ActivitySerializer(activities,many=True)
            return Response(activities_serializer.data)
        
        elif len(params) > 1: #multiple parameters
            print("return multiples filter")
            data = Activity.objects.filter(id = params[0])
            activities = Activity.objects.filter(slug=params[0])
            activities_serializer = ActivitySerializer(activities,many=True)
            return Response(activities_serializer.data)
        
        elif request.query_params.get('box_slug') != None:
            print("box_slug")
            box_slug = request.query_params.get('box_slug')
            activities = Activity.objects.filter(slug=box_slug)
            activities_serializer = ActivitySerializer(activities,many=True)
            return Response(activities_serializer.data)
        
        elif request.query_params.get('category_id') != None:
            print("category_id")
            category_id = request.query_params.get('category_id')
            print(category_id)
            activities = Activity.objects.filter(category_id=category_id)
            activities_serializer = ActivitySerializer(activities,many=True)
            return Response(activities_serializer.data)

        elif request.query_params.get('reason_id') != None:
            print("reason_id")
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
        print(slug)
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
            print(request.query_params.get('slug'))
            box_slug = request.query_params.get('slug')
            boxes = Box.objects.filter(slug=box_slug)
            boxes_serializer = BoxSerializer(boxes,many=True)
            return Response(boxes_serializer.data)
        
class BoxSlugAPIView(APIView):
    def get(self,request,slug): #slug in a url
        print(slug)
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
            print(request.query_params.get('slug'))
            box_slug = request.query_params.get('slug')
            boxes = Category.objects.filter(slug=box_slug)
            boxes_serializer = CategorySerializer(boxes,many=True)
            return Response(boxes_serializer.data)


class CategorySlugAPIView(APIView):
    def get(self,request,slug):
        categories = Category.objects.filter(slug=slug)
        categories_serializer = CategorySerializer(categories,many=True)
        return Response(categories_serializer.data)

