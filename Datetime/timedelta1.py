import datetime
hundred = datetime.timedelta(days = 100)
a = datetime.datetime.now() - hundred
print(a)

hundred_before = datetime.timedelta(days = -100)
b = datetime.datetime.now() + hundred_before
print(b)