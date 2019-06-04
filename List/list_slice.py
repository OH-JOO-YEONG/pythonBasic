text = "hello world"
text_list = text[1:5]
print(text_list)
print(text[1:len(text)])
print(text[1:])

# list[ 시작값:끝값:step ]
list1 = list(range(20))
print(list1)
print(list1[5:15])
print(list1[5:15:3])
print(list1[17:5:-4])

numbers = list(range(10))
del numbers[0]
print(numbers)
print(numbers[0:5])
del numbers[:5]
print(numbers)
numbers[1:3] = [77, 88, 99]
print(numbers)
numbers[1:3] = [8]
print(numbers)