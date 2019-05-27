def root(a, b, c): # a b c 매개인자
    r1 = (-b + (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)
    r2 = (-b - (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)

    return r1, r2 #쉼표로 구분해주면 return은 복수로 보낼 수 있다.

x = 1
y = 2
z = -8

r1, r2 = root(x, y, z)
print('근은 {} {}'.format(r1, r2))
