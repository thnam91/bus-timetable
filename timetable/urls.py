from django.urls import path, include
from . import views

app_name = 'timetable'

urlpatterns = [
    path('', views.index, name='index'),
]
