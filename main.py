import datetime as dt

now = dt.datetime.now()
print(now)
year = now.year
month = now.month
day = now.day
hour = now.hour
minute = now.minute
second = now.second
day_of_week = now.weekday()

print(day_of_week)


date_of_birth = dt.datetime(year=1999, month=8, day=27, hour=4)
print(date_of_birth)