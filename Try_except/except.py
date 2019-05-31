try:
    # list = []
    # print(list[0])

    text = 'abc'
    number = int(text)
except Exception as ex: #에러의 이름을 모르는 경우 처리하는 법  Exception as ex 없어도 됨
    print('에러가 발생했습니다.', ex)