from django.shortcuts import render
from rest_framework import viewsets
from .import serializers
from .import models
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework import filters, pagination

# Create your views here.
# speacilization serializer class bases views
class SpecializationViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = models.Specialization.objects.all()
    serializer_class = serializers.SpecializationSerializer

# Designation serializer class bases views
class DesignationViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = models.Designation.objects.all()
    serializer_class = serializers.DesignationSerializer

#spacific doctor available time filtering
class AvailableTiemSpacificDoctor(filters.BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        doctor_id = request.query_params.get('doctor_id')
        if doctor_id:
            return queryset.filter(doctor = doctor_id)
        return queryset

# Available Time serializer class bases views
class AvailableTimeViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = models.AvailableTime.objects.all()
    serializer_class = serializers.AvailableTimeSerializer
    filter_backends = [AvailableTiemSpacificDoctor]

# pagination add doctor list
class DoctorPagination(pagination.PageNumberPagination):
    page_size = 1 # items per page
    page_size_query_param = page_size
    max_page_size = 100

# doctor serializer class bases views
class DoctorViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = models.Doctor.objects.all()
    serializer_class = serializers.DoctorSerializer
    filter_backends = [filters.SearchFilter]
    pagination_class = DoctorPagination

# reviewer serializer class bases views
class ReviewViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = models.Review.objects.all()
    serializer_class = serializers.ReviewSerializer

    def get_queryset(self):
        queryset = super().get_queryset() # ager je all queryset cilo sai ta re inharet korlam
        # print(self.request.query_params, '##')
        reviewer_id = self.request.query_params.get('reviewer_id') # patainet id ke select korlam
        print(reviewer_id, '##')
        doctor_id = self.request.query_params.get('doctor_id')
        # print(pateint_id, '@@@')
        if reviewer_id:
            queryset = queryset.filter(reviewer_id=reviewer_id)
        if doctor_id:
            queryset = queryset.filter(doctor_id=doctor_id)
        return queryset