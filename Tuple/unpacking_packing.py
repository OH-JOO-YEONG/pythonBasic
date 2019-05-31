a, b =  1, 2
print(a)
c= (3, 4)
print(c)
d, e = c
print(d)
print(e)
f = d, e
print(f)
# 값 바꿔주는거 혁명 ...
x = 5
y = 10
x, y = y, x
print(x)
print(y)
def tuple_func():
    return 1, 2

q, w = tuple_func()
print(q)
print(w)