from django.contrib import admin
from django.urls import path, include
from . import views

app_name = "films"

urlpatterns = [
    path('', views.main, name='main'),
    path('<int:id>/', views.about_film, name='about_film'),
    path('filter/', views.filter_film, name='filter_film'),
    path('filter_form/', views.filter_form, name='filter_form')
]