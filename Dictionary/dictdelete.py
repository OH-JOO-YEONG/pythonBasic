list = [1, 2, 3, 4, 5]
list[2] = 33
print(list)

dict = {
    'one' : 1,
    'two' : 2
}

print(dict)
dict['one'] = 11
print(dict)
dict['three'] = 3
print(dict)
del(list[2])
print(list)
del (dict['one'])
print(dict)
dict['one'] = 1
print(dict)
print(dict.pop('two'))
print(dict)