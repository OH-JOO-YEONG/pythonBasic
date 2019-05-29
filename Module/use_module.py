import mymodule, datetime

selected = mymodule.random_rsp()
print(selected)
print('가위', mymodule.SCISSOR == selected)

now = datetime.datetime.now()
print(now.year, now.month, now.day)