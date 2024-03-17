from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .import views

router = DefaultRouter()

# router antena set here
router.register('specialization-list', views.SpecializationViewSet)
router.register('designation-list', views.DesignationViewSet)
router.register('available-time-list', views.AvailableTimeViewSet)
router.register('doctors-list', views.DoctorViewSet)
router.register('reviewer-list', views.ReviewViewSet)

# urls pattern set
urlpatterns = [
    path('', include(router.urls)),
]
