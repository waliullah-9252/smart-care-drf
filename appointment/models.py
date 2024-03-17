from django.db import models
from patient.models import Pateint
from doctor.models import Doctor, AvailableTime
# Create your models here.

APPOINTMENT_STATUS = [
    ('Completed', 'Completed'),
    ('Pending', 'Pending'),
    ('Running', 'Running'),
]

APPOINTMENT_TYPES = [
    ('Offline', 'Offline'),
    ('Online', 'Online'),
]

# appointments models created
class Appointment(models.Model):
    pateint = models.ForeignKey(Pateint, on_delete = models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete = models.CASCADE)
    appointment_types = models.CharField(choices = APPOINTMENT_TYPES, max_length = 15)
    appointment_status = models.CharField(choices = APPOINTMENT_STATUS, max_length = 15, default = 'Pending')
    symptom = models.TextField()
    time = models.ForeignKey(AvailableTime, on_delete = models.CASCADE)
    cancel = models.BooleanField(default = False)

    def __str__(self):
        return f'Doctor : {self.doctor.user.first_name} : Pateint : {self.pateint.user.first_name}'
