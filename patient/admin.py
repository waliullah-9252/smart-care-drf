from django.contrib import admin
from .models import Pateint
# Register your models here.
# list display show in admin panel 
class PateintAdmin(admin.ModelAdmin):
    list_display = ['first_name','last_name','mobile_no', 'image']

    def first_name(self, obj):
        return obj.user.first_name
    def last_name(self, obj):
        return obj.user.last_name
admin.site.register(Pateint, PateintAdmin)