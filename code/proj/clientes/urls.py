from django.urls import path
from .views import home,pesq

urlpatterns = [
    path('',home),
    path('scrap',pesq),
]