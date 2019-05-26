from django.shortcuts import render

def index(request):
    return render(request, 'timetable/timetable.html')
