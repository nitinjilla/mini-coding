import datetime
import pytz


#naive datetime and aware datetime

day = datetime.date.today()

print(day)

print(day.day) #prints only the year, same for month and day

print(day.weekday())
print(day.isweekday())

tdelta = datetime.timedelta(days=7)
print(day + tdelta)

date2 = date1 + timedelta
imedelta = date1 + date2

bday = datetime.date(2020, 1, 4)
age = bday - day
print(age.days)

time = datetime.time(10, 2, 45, 100000)
print(time.hour) #same for minutes, seconds and microseconds(no plural)

time_today = datetime.datetime.today()
time_now = datetime.datetime.now()
time2_utcnow = datetime.datetime.utcnow()

print(time2.date())
print(time2.time())

tdelta = datetime.timedelta(hours=4)
print(time_today)
print(time_now)
print(time2_utcnow)

#timezone aware datetime
time_now = datetime.datetime.now(tz=pytz.UTC)
print(time_now)

dt_mum = time_now.astimezone(pytz.timezone('Asia/Kolkata'))
print(dt_mum)

print(time_now.strftime('%B %d, %Y')) #python documentation
#               ^^ converts datetime to string

dt_str = 'October 14, 2019'
dt = datetime.datetime.strptime(dt_str, '%B %d, %Y')
#^                      ^converts string to datetime
print(dt)































