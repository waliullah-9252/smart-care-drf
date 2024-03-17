from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .import views

router = DefaultRouter()

# router antena create here
router.register('appointment-list', views.AppointmentViewSet)

# url pattern set here
urlpatterns = [
    path('', include(router.urls)),
]
