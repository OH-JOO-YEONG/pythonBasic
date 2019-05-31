list = [1, 2, 3, 4, 5]
for a in enumerate(list): #enumerate 인덱스값과 자료를 나타내줌
    print('{}번째 값 : {}'.format(*a))

for a in enumerate(list):
    print('{}번째 값은 {}'.format(a[0],a[1]))

    #*변수는 튜플을 쪼개라

ages = {'Tod':35, 'Jane':23, 'Paul':62}
for b in ages.items():
    print('{}의 나이는 : {}'.format(b[0], b[1]))