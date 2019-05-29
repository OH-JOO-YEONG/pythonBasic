ages = {
    'Tod' : 35,
    'Jane' : 23,
    'Paul' : 62
}
#순서와 상관없이 for문 사용하고 순서를 중요시하지 않음 값이 랜덤으로 나옴
# for key in ages.keys(): #keys() 생략가능

for key, value in ages.items():
    print('{}의 나이는 {} 입니다.'.format(key, value))

# for value in ages.values():
#     print(value)