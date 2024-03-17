from django.db import models
from django.contrib.auth.models import User
from patient.models import Pateint
# Create your models here.

# specialization model 
class Specialization(models.Model):
    name = models.CharField(max_length=40)
    slug = models.SlugField(max_length=40)

    def __str__(self):
        return self.name

# designation model     
class Designation(models.Model):
    name = models.CharField(max_length=40)
    slug = models.SlugField(max_length=40)

    def __str__(self):
        return self.name

# available time model     
class AvailableTime(models.Model):
    time_slot = models.CharField(max_length=100)

    def __str__(self):
        return self.time_slot

# doctor model     
class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    image = models.ImageField(upload_to='doctor/images')
    specilization = models.ManyToManyField(Specialization)
    designation = models.ManyToManyField(Designation)
    available_time = models.ManyToManyField(AvailableTime)
    fees = models.IntegerField()
    meet_link = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'

# choices field add
STAR_CHOICES = [
    ('⭐', '⭐'),
    ('⭐⭐', '⭐⭐'),
    ('⭐⭐⭐', '⭐⭐⭐'),
    ('⭐⭐⭐⭐', '⭐⭐⭐⭐'),
    ('⭐⭐⭐⭐⭐', '⭐⭐⭐⭐⭐'),
]

# reviewer model 
class Review(models.Model):
    reviewer = models.ForeignKey(Pateint, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    rating = models.CharField(choices = STAR_CHOICES, max_length=100)

    def __str__(self):
        return f'Pateient: {self.reviewer.user.first_name} {self.reviewer.user.last_name} : Doctor: {self.doctor.user.first_name} {self.doctor.user.last_name}'
