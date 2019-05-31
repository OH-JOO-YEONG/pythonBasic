# selected = None
# while selected not in ['가위', '바위', '보']: #가위 바위 보가 아니면 다시 while문으로 가서 입력을 받음
#     selected = input('가위, 바위, 보 중에 선택하세요 : ')
#
# print('선택된 값은 : ', selected)
patterns = ['가위', '바위', '보']
length = len(patterns)
i = 0
while i < length:
    print(patterns[i])
    i = i + 1