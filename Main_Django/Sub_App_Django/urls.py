from django.urls import path 
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('Sub_App_Django/', views.Sub_App_Django, name='Sub_App_Django'),
    path('Sub_App_Django/details/<int:id>', views.details, name='details'),
    path('testing/', views.testing, name='testing'), 
]