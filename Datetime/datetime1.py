import datetime

a = datetime.datetime.now()
print(a)
b = a.replace(year= 2017, month = 2, day = 1)
start_time = datetime.datetime(2019, 8, 1)
print(b)

how_long = start_time - datetime.datetime.now()
print(type(how_long))
print(how_long.days)
print(how_long.seconds)
print("8월 1일까지는 {}일 {}시간이 남았습니다.".format(how_long.days, how_long.seconds//3600))