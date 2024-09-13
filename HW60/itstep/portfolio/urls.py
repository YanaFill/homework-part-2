from django.urls import path
from .views import about, main, contact


urlpatterns = [
    path('', main, name='main'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact')
]