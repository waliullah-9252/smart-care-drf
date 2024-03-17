from django.contrib import admin
from .models import Appointment
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
# Register your models here.

class AppointmentAdmin(admin.ModelAdmin):
    list_display = ['doctor_name', 'pateint_name', 'appointment_status', 'appointment_types', 'symptom', 'time', 'cancel']

    def doctor_name(self, obj):
        return obj.doctor.user.first_name
    
    def pateint_name(self, obj):
        return obj.pateint.user.last_name
    
    def save_model(self, request, obj, form, change):
        obj.save()
        if obj.appointment_status == 'Running' and obj.appointment_types == 'Online':
            email_subject = "Your Online Appointment is running now."
            email_body = render_to_string('admin_email.html', {
                'user': obj.pateint.user, 'doctor': obj.doctor
            })
            email = EmailMultiAlternatives(email_subject, '', to=[obj.pateint.user.email])
            email.attach_alternative(email_body, 'text/html')
            email.send()

        if obj.appointment_status == 'Completed' and obj.appointment_types == 'Online':
            email_subject = "Your Online Appointment is Completed now."
            email_body = render_to_string('complete_email.html', {
                'user': obj.pateint.user,
            })
            email = EmailMultiAlternatives(email_subject, '', to=[obj.pateint.user.email])
            email.attach_alternative(email_body, 'text/html')
            email.send()
    
admin.site.register(Appointment, AppointmentAdmin)