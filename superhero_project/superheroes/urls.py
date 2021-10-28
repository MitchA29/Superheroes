from django.urls import path
from django.urls import path

from . import views

app_name = 'superheroes'
URLPattern = [
    path('index/',views.index, name='index')
]

