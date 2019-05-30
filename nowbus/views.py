from itertools import zip_longest
from datetime import datetime, timedelta
from django.shortcuts import render
from bus_timetable_var import *

def time_to_int(time):
    (h, m, s) = time.split(':')
    return int(h) * 3600 + int(m) * 60 + int(s)

def ret_remain(timetable):
    now = time_to_int(datetime.now().strftime('%H:%M:%S')) # 현재 시간
    for j in [time_to_int(i) for i in timetable]:
        if now <= j: return str(timedelta(seconds=int(j-now))).split(':')

def index(request):
    # 0: 월, 1: 화, 2: 수, 3: 목, 4: 금, 5: 토, 6: 일
    days = ['월', '화', '수', '목', '금', '토', '일']
    day = days[datetime.today().weekday()] # 오늘 요일 : days[day]

    if day in '월화수목금':
        h19s, m19s, s19s = ret_remain(BUS19_WEEKDAY_SOLMOI)
        h19o, m19o, s19o = ret_remain(BUS19_WEEKDAY_ORI)
        h58s, m58s, s58s = ret_remain(BUS58_WEEKDAY_SOLMOI)
        h582s, m582s, s582s = ret_remain(BUS582_WEEKDAY_SOLMOI)
        h582g, m582g, s582g = ret_remain(BUS582_WEEKDAY_GOOCHEONG)
    if day == '토':
        h19s, m19s, s19s = ret_remain(BUS19_WEEKDAY_SOLMOI)
        h19o, m19o, s19o = ret_remain(BUS19_WEEKDAY_ORI)
        h58s, m58s, s58s = ret_remain(BUS58_WEEKEND_SOLMOI)
        h582s, m582s, s582s = ret_remain(BUS582_WEEKEND_SOLMOI)
        h582g, m582g, s582g = ret_remain(BUS582_WEEKEND_GOOCHEONG)
    if day == '일':
        h19s, m19s, s19s = ret_remain(BUS19_WEEKEND_SOLMOI)
        h19o, m19o, s19o = ret_remain(BUS19_WEEKEND_ORI)
        h58s, m58s, s58s = ret_remain(BUS58_WEEKEND_SOLMOI)
        h582s, m582s, s582s = ret_remain(BUS582_WEEKEND_SOLMOI)
        h582g, m582g, s582g = ret_remain(BUS582_WEEKEND_GOOCHEONG)

    return render(request, 'nowbus/index.html', {
        'day': day,
        'h19s': h19s, 'm19s': m19s, 's19s': s19s,
        'h19o': h19o, 'm19o': m19o, 's19o': s19o,
        'h58s': h58s, 'm58s': m58s, 's58s': s58s,
        'h582s': h582s, 'm582s': m582s, 's582s': s582s,
        'h582g': h582g, 'm582g': m582g, 's582g': s582g,
    })
