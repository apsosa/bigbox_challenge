
from rest_framework import  serializers
from core.models import Activity, ActivityImage,Box,Category,BoxImage
from django.contrib.auth.models import User



class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Activity
        fields = '__all__'

    def to_representation(self, instance):
        reasons = instance.reasons.all()
        activity_imagen = ActivityImage.objects.filter(activity=instance.id)
        reasons_set= []
        for r in reasons:
            reasons_set.append({
                'name':r.name,
                'order':r.order,
                'slug':r.slug
            })
        activities_img_set = []
        for act in activity_imagen:
            upload = 'https://placeimg.com/'+ str(act.upload)
            activities_img_set.append({
                'id': act.id,
                'order':act.order,
                'upload':upload}) 
        return {
           'name' : instance.name,
            'slug' : instance.slug,
            'category': instance.category_id,
            'description': instance.description,
            'purchase_available': instance.purchase_available,
            'reasons':reasons_set,
            'activityimage_set':activities_img_set,
        }

class BoxSerializer(serializers.ModelSerializer):
    class Meta:
        model = Box
        fields = '__all__'
    def to_representation(self, instance):
        box_image = BoxImage.objects.get(pk=instance.id)
        box_image_set ='https://placeimg.com/'+ str(box_image.upload)
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
                    'upload': box_image_set,            
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
