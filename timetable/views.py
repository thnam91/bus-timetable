from django.shortcuts import render
from datetime import datetime


def index(request):
    # 0: 월, 1: 화, 2: 수, 3: 목, 4: 금, 5: 토, 6: 일
    days = ['월', '화', '수', '목', '금', '토', '일']
    day = datetime.today().weekday()
    today = datetime.today().strftime("지금은 %Y년 %m월 %d일 (" + days[day] + "),  %H시 %M분 %S초 입니다.")
    return render(request, 'timetable/timetable.html', {
        'day': today,
    })