from django.db import models
from rest_framework import fields, serializers
from core.models import Activity,Box,Category,BoxImage

class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Activity
        fields = '__all__'

    def to_representation(self, instance):

        return {
           'name' : instance.name,
            'slug' : instance.slug,
            'category': instance.category_id,
            'description': instance.description,
            'purchase_available': instance.purchase_available,
        }

class BoxSerializer(serializers.ModelSerializer):
    class Meta:
        model = Box
        fields = '__all__'
    def to_representation(self, instance):
        box_image = BoxImage.objects.get(pk=instance.id)
        return {
           'name' : instance.name,
            'slug' : instance.slug,
            'category': instance.category_id,
            'description': instance.description,
            'purchase_available': instance.purchase_available,
            'price': instance.price,
            'boximage_set': [{
                    'id' : box_image.id,
                    'order': box_image.order,
                    #'upload': box_image.upload,            
                }]
        }

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

    def to_representation(self, instance):
        box = Box.objects.get(pk=instance.id)

        return {
           'name' : instance.name,
            'slug' : instance.slug,
            'description': instance.description,
            'box_set': [{
                'name' : box.name,
                'slug' : box.slug,
                'price': box.price,
            }]
        }