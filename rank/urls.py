from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('top/', views.top, name='top'),
]