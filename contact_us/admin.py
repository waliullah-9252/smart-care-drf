from django.contrib import admin
from .models import ContactUs
# Register your models here.

# list display show in admin panel
class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone', 'description',]
admin.site.register(ContactUs, ContactAdmin)