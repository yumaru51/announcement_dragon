from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('top/', views.top, name='top'),
    # path('user_name/category1/category2/', views.detail, name='detail'),
    path('yumaru51/<str:category1>/', views.detail, name='detail'),
    path('yumaru51/', views.detail2, name='detail2'),
    path('prime/', views.prime, name='prime'),

]
