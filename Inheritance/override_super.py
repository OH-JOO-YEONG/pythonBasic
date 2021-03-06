class Animal():

    def __init__(self, name):
        self.name = name

    def walk(selfs):
        print("걷는다")

    def eat(self):
        print("먹는다")

    def greet(self):
        print("{}이/가 인사한다".format(self.name))

class Human(Animal): #클래스안에 클래스를 넣으면 상속한다는 것

    def __init__(self, name, hand):
        super().__init__(name)
        self.hand = hand

    def wave(self):
        print("{}을 흔들면서".format(self.hand))

    def greet(self):
        self.wave()
        super().greet()

person = Human("사람", "오른손")
person.greet()
