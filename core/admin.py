from django.contrib import admin
from .models import Box,BoxImage,Activity,ActivityImage,Category,Reason
from django_extensions.admin import ForeignKeyAutocompleteAdmin
# Register your models here.
#admin.site.register(Box)
admin.site.register(BoxImage)
admin.site.register(Activity)
admin.site.register(ActivityImage)
admin.site.register(Category)
admin.site.register(Reason)

class BofAdmin(ForeignKeyAutocompleteAdmin):
  # User is your FK attribute in your model
    # first_name and email are attributes to search for in the FK model
    related_search_fields = {
       'activities': ('name', 'slug'),
    }

    fields = ('user', 'avatar', 'is_active')

admin.site.register(Box,BofAdmin)
