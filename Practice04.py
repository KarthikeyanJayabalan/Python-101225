import datetime
from datetime import timedelta
from dateutil.relativedelta import relativedelta

x = datetime.datetime.now()
print(x)


print(f"{x.month}-{x.day}-{x.year}-"+x.strftime("%X"))



formatted_date = x.strftime("%m%d%y/%H%M%S")
print(formatted_date)

tomorrowDate = x + timedelta(days=1)
nextMonth = x + relativedelta(months=1)
print(tomorrowDate.strftime("%m%d%y"))
print(tomorrowDate.strftime("%d%b%y"))
print(tomorrowDate.strftime("%d%b%y").upper())
print(nextMonth.strftime("%m%d%y"))
