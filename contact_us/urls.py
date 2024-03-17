from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()

# antena create with contact us
router.register('contact_us', views.ContactUsViewSet)

# url pattern set here
urlpatterns = [
    path('', include(router.urls)),
]
