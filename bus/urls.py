from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect


urlpatterns = [
    path('admin/', admin.site.urls),
    path('timetable/', include('timetable.urls', namespace='timetable')),
    path('', lambda r: redirect('timetable:index')),
]
