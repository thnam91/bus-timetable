from datetime import datetime
from django.shortcuts import render
from bus_timetable_var import *


def time_to_int(time):
    (h, m, s) = time.split(':')
    return int(h) * 3600 + int(m) * 60 + int(s)


def index(request):
    # 0: 월, 1: 화, 2: 수, 3: 목, 4: 금, 5: 토, 6: 일
    days = ['월', '화', '수', '목', '금', '토', '일']
    day = datetime.today().weekday()
    today = datetime.today().strftime("지금은 %Y년 %m월 %d일 (" + days[day] + "),  %H시 %M분 %S초 입니다.")
    if day < 5: # 월요일 ~ 금요일
        bus = [
            BUS19_WEEKDAY,
            BUS58_WEEKDAY_SOLMOI,
            BUS582_WEEKDAY_SOLMOI,
            BUS582_WEEKDAY_SUJI]
    elif day == 5: # 토요일
        bus = [
            BUS19_WEEKDAY,
            BUS58_WEEKEND_SOLMOI,
            BUS582_WEEKEND_SOLMOI,
            BUS582_WEEKEND_SUJI]
    else: # 일요일
        bus = [
            BUS19_WEEKEND_SOLMOI,
            BUS19_WEEKEND_ORI,
            BUS58_WEEKEND_SOLMOI,
            BUS582_WEEKEND_SOLMOI,
            BUS582_WEEKEND_SUJI]

    # bus19 = [time_to_int(i) for i in bus19]
    # print(bus19)
    # now = time_to_int(datetime.datetime.now().strftime('%H:%M:%S'))
    # remain_time = 0
    # for i in bus19:
    #    if now <= i:
    #        remain_time = datetime.timedelta(seconds=int(i-now))
    #        break
    # h, m, s = str(remain_time).split(':')

    return render(request, 'nowbus/index.html', {
        'day': today,
        'h': 1,
        'm': 2,
        's': 3,
    })
