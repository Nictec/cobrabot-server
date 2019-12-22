from django.urls import include, path
from rest_framework import routers
from . import views

urlpatterns = [
    path('verify/', views.verify),
    path('commands/', views.commands),
]