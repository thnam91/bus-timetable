from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect


urlpatterns = [
    path('admin/', admin.site.urls),
    path('timetable/', include('timetable.urls', namespace='timetable')),
    path('nowbus/', include('nowbus.urls', namespace='nowbus')),
    path('', lambda r: redirect('nowbus:index')),
]
