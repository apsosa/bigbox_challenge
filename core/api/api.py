from rest_framework.response import Response
from rest_framework.views import APIView
from core import api
from core.models import Activity, Box,Category
from core.api.serializers import ActivitySerializer,BoxSerializer,CategorySerializer




class ActivityAPIView(APIView):
    def get(self,request):
        activities = Activity.objects.all()
        activities_serializer = ActivitySerializer(activities,many=True)
        return Response(activities_serializer.data)



class BoxAPIView(APIView):
    def get(self,request):
        boxes = Box.objects.all()
        boxes_serializer = BoxSerializer(boxes,many=True)
        return Response(boxes_serializer.data)



class CategoryAPIView(APIView):
    def get(self,request):
        categories = Category.objects.all()
        categories_serializer = CategorySerializer(categories,many=True)
        return Response(categories_serializer.data)
