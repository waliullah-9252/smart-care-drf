from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .import views 

router = DefaultRouter()

# router antena crate with patient 
router.register('patient/list', views.PatientViewSet)

# url pattern set here
urlpatterns = [
    path('', include(router.urls)),
    path('register/', views.RegistrationApiView.as_view(), name = 'register'),
    path('login/', views.UserLoginApiView.as_view(), name = 'login'),
    path('logout/', views.UserLogoutView.as_view(), name = 'logout'),
    path('active/<uid64>/<token>/', views.activete, name = 'active'),
]
