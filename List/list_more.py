list1 = [135, 462, 3241, 234, 634]
print(list1.index(135))

list2 = [1, 2, 3] + [4, 5, 6]
print(list2)
list2.extend([9, 10, 11])
print(list2)
list1.insert(2, 999)
print(list1)
list1.sort()
print(list1)

my_list = [1, 2, 3, 4, 5, 6]
print(my_list[0])
characters = list("abcdefg")
print(characters)

word = "Hello world 인생은 아름다워"
words_list = word.split()
print(words_list)
time_str = "04:32:23"
time_list = time_str.split(":")
print(time_list)
time_char = ":".join(time_list)
print(time_char)
words = " ".join(words_list)
print(words)