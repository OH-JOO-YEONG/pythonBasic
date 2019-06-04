class Animal():
    def walk(selfs):
        print("걷는다")

    def eat(self):
        print("먹는다")

    def greet(self):
        print("인시한다")

class Human(Animal): #클래스안에 클래스를 넣으면 상속한다는 것

    def wave(self):
        print("손을 흔든다")

    def greet(self):
        self.wave()

class Cow(Animal):
    '''소'''

class Dog(Animal):

    def wag(self):
        print("꼬리를 흔든다")

    def greet(self):
        self.wag()

cow = Cow()

cow.greet()

person = Human()
person.greet()


dog = Dog()
dog.greet()
