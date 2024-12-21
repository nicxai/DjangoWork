from django.urls import path
from main.views import *

urlpatterns = [
    path('main/', main, name='main'),
    path('', benner, name='benner'),
]
