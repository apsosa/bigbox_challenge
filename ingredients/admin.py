from django.contrib import admin

# Register your models here.
from ingredients.models import CategoryI, Ingredient

admin.site.register(CategoryI)
admin.site.register(Ingredient)