#task1
from datetime import date, timedelta

print(date.today() - timedelta(5))

#task2
from datetime import date, timedelta

print(date.today() - timedelta(1), date.today(), date.today() + timedelta(1))

#task3
import datetime

print(datetime.datetime.today().replace(microsecond=0))
#task4
from datetime import datetime, time

date1 = datetime.strptime('2024-02-18 10:32:25', '%Y-%m-%d %H:%M:%S')
date2 = datetime.now()
td = date2 - date1
print(td.days * 24 * 3600 + td.seconds)
