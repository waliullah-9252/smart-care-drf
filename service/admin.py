from django.contrib import admin
from .models import Service
# Register your models here.
# list display show in admin panel
class AdminService(admin.ModelAdmin):
    list_display = ['name', 'description', 'image']
admin.site.register(Service, AdminService)
