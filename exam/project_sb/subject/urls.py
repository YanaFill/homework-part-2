from django.urls import path
from . import views

urlpatterns = [
    path('', views.subject_list, name='subject_list'),
    path('subject/<int:pk>/', views.subject_detail, name='subject_detail'),
    path('subject/new/', views.subject_create, name='subject_create'),
    path('subject/<int:pk>/edit/', views.subject_edit, name='subject_edit'),
    path('subject/<int:pk>/delete/', views.subject_delete, name='subject_delete'),
]
