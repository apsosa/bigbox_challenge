from django.contrib import admin
from .models import Box,BoxImage,Activity,ActivityImage,Category,Reason

# Register your models here.
admin.site.register(Box)
admin.site.register(BoxImage)
admin.site.register(Activity)
admin.site.register(ActivityImage)
admin.site.register(Category)
admin.site.register(Reason)