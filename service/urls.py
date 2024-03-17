from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .import views

router = DefaultRouter()

# router antena create with services 
router.register('services', views.ServiceViewSet)

# url pattern set here
urlpatterns = [
    path('', include(router.urls)),
]