from django.db import models

# Create your models here.

# contact us model
class ContactUs(models.Model):
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=11)
    description = models.TextField()

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Contact Us"
    
