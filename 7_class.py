class Person:
    def hello(self):
        print('Hello')

person = Person()
person.hello()
person1 = Person()
person1.hello()

class Person:
    def __init__(self):
        self.hi = 'Hello'

    def hello(self):
        print(self.hi)

person = Person()
person.hello()
print(person.hi)

class Person:
    def __init__(self, n, a):
        self.name = n
        self.age = a

    def hello(self):
        print('Hello {}'.format(self.name))
        print('당신은 {}살 입니다.'.format(self.age))

person = Person('홍길동', 20)
person.hello()

class Student:
    def __init__(self, grade, ban, name):
        self.grade = grade
        self.ban = ban
        self.name = name
    
    def introduce(self):
        print('{}학년 {}반 {}입니다.'.format(self.grade, self.ban, self.name))

student = Student(3, 4, '홍길동')
student.introduce()

class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age

    def hello(self):
        print('Hello {}'.format(self.name))
        print('당신은 {}살 입니다.'.format(self.__age))

person = Person('홍길동', 20)
person.hello()
#print(person.__age) #에러
#person.__age = 100 #에러

class Person:
    def __init__(self, name, age):
        self.name = name
        if 0 <= age <= 20: self.__age = age
        else: age = 0

    def inc_age(self):
        self.__age += 1

    def info(self):
        print(self.__age)

person = Person('홍길동', 20)
person.inc_age()
person.info() 

class Math:
    @staticmethod
    def add(a, b):
        return a + b
    
    @staticmethod
    def sub(a, b):
        return a - b

print(Math.add(4, 5))
print(Math.sub(9, 5))

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        
    def info(self):
        return self.width * self.height
    
    def double(self):
        self.width *= 2
        self.height *= 2
    
rect = Rectangle(10, 20)
print(rect.info())
rect.double()
print(rect.width, rect.height)

class Vehicle:
    def __init__(self, speed):
        self.speed = speed

    def speed_up(self):
        self.speed += 10
    
    def speed_dn(seld):
        seld.speed -= 10

class Car(Vehicle):
    def __init__(self, speed, wheels, seats):
        Vehicle.__init__(self, speed)
        self.wheels = wheels
        self.seats = seats

    def info(self):
        print(self.speed, self.wheels, self.seats)

car = Car(100, 4, 4)
car.speed_up()
car.info()

class Truck(Car):
    def __init__(self, speed, wheels, seats, loadage):
        Car.__init__(self, speed, wheels, seats)
        self.loadage = loadage

    def load(self):
        print('load')

    def unload(self):
        print('unload')

    def info(self):
        print(self.speed, self.wheels, self.seats, self.loadage)

truck = Truck(100, 4, 4, 30)
truck.load()
truck.unload()
truck.info()