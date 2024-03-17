from django.contrib import admin
from .models import Specialization, Designation, AvailableTime, Doctor,Review
# Register your models here.
class SpecializationAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',), }

class DesignationAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',), }

admin.site.register(Specialization, SpecializationAdmin)
admin.site.register(Designation, DesignationAdmin)
admin.site.register(AvailableTime)

class DoctorAdmin(admin.ModelAdmin):
    list_display = ['first_name','last_name','image', 'fees', 'meet_link']

    def first_name(self, obj):
        return obj.user.first_name
    
    def last_name(self, obj):
        return obj.user.last_name
admin.site.register(Doctor, DoctorAdmin)

# class ReviewAdmin(admin.ModelAdmin):
#     list_display = ['body', 'created_on', 'rating']

admin.site.register(Review)