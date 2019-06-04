class Human():
    '''인간'''
    def __init__(self, name, weight): # 인스턴스를 만들때 실행되는 함수
        '''초기화'''
        # print("___init___실햄")
        self.name = name
        self.weight = weight
        # print("이름은 {}, 몸무게는 {}".format(name, weight))

    # def create(name, weight):
    #     person = Human()
    #     person.name = name
    #     person.weight = weight
    #     return person

    def __str__(self): #인스턴스 자체를 출력할 때의 형식을 지정해주는 함수
        '''문자열화 함수'''
        return "{} (몸무게 {} kg)".format(self.name, self.weight)

    def eat(self):
        self.weight += 0.1
        print("{}가 먹어서 {} kg이 되었습니다.".format(self.name, self.weight))

    def walk(self):
        self.weight -= 0.1
        print("{}가 먹어서 {} kg이 되었습니다.".format(self.name, self.weight))

    def speak(self, message):
        print(message)

person = Human("철수", 60.5)
print(person)
print(person.name)
print(person.weight)
person.eat()