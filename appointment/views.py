from django.shortcuts import render
from rest_framework import viewsets
from .import models
from .import serializers
from rest_framework.permissions import IsAuthenticatedOrReadOnly

# Create your views here.
# Appointment view set crate here
class AppointmentViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = models.Appointment.objects.all()
    serializer_class = serializers.AppointmentSerializer

    # coustom query kortaci
    def get_queryset(self):
        queryset = super().get_queryset() # ager je all queryset cilo sai ta re inharet korlam
        # print(self.request.query_params, '##')
        pateint_id = self.request.query_params.get('pateint_id') # patainet id ke select korlam
        doctor_id = self.request.query_params.get('doctor_id')
        # print(pateint_id, '@@@')
        if pateint_id:
            queryset = queryset.filter(pateint_id=pateint_id)
        if doctor_id:
            queryset = queryset.filter(doctor_id=doctor_id)
        return queryset
    
    