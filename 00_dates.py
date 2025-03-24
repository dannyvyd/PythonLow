from datetime import datetime

now = datetime.now()

def print_date(date):
    print(date.year)
    print(date.month)
    print(date.day)
    print(date.hour)
    print(date.minute)
    print(date.second)
    print(date.timestamp())

print_date(now)

## Solo puede funcionar si utilizas las 3 asignaciones del datetime (1,2,3 +) Si utilizas uno o dos no arranca.

year_2025 = datetime(2025, 3, 23, 19, 27)

print_date(year_2025)


from datetime import time

current_time = time(19,35,10)

print(current_time.hour)
print(current_time.minute)
print(current_time.second)


from datetime import date

current_date = date.today()

print(current_date.year)
print(current_date.month)
print(current_date.day)

current_date = date(2025, 3, 23)

print(current_date.year)
print(current_date.month)
print(current_date.day)

current_date = date(current_date.year + 2, current_date.month, current_date.day)
current_date = date(current_date.year, current_date.month + 1, current_date.day)
current_date = date(current_date.year, current_date.month, current_date.day + 3)
print (current_date.year)
print (current_date.month)
print (current_date.day)

current_date = date(current_date.year - 10, current_date.month, current_date.day)

print(current_date.year)

diff = year_2025 - now
print(diff)

diff = year_2025.date() - current_date
print(diff)

from datetime import timedelta

start_timedelta = timedelta(230, 200, 300 , weeks= 30)
end_timedelta = timedelta(23, 100, 100 , weeks= 10)

print(start_timedelta - end_timedelta)
print(end_timedelta - end_timedelta)

