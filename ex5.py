class Circle:
    pi = 3.14
    #init :: Circle
    def __init__(self, argRadius):
        self.radius = argRadius
        self.area = (argRadius **2) * Circle.pi
        print('self.area:', self.area)
    
    # method 1 :: self, set radius
    def set_radius(self, newRadius):
        self.radius = newRadius
        self.area = (newRadius **2) * self.pi
        print('self.area: ', self.area)
    # method 2 :: return perimeter
    def get_perimeter(self):
        return self.radius*2 * self.pi

myCircle = Circle(8)
myCirclePer = myCircle.get_perimeter()
print(f'radius = {myCircle.radius}, perimeter = {myCirclePer}')
myCircle.set_radius(5)
myCirclePer = myCircle.get_perimeter()
print(f'radius = {myCircle.radius}, perimeter = {myCirclePer}')

print('--------------------Inheritance----------------------')

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def speak(self):
        print('person is speaking')

personObj = Person('Bold', '28')
personObj.speak()

# Inheritance

class Student(Person):
    pass
studentObj = Student('Dorj','15')
studentObj.speak()

print("---------------car--------------")
class Car:
    def __init__(self, types, transmission):
        self.types = types
        self.transmission = transmission
    def go(self):
        print('car and Lexus ')

carObj = Car('normal','2wheel')
carObj.go()

class Lexus(Car):
    pass
LexusObj = Lexus('sedan','4wheel')
LexusObj.go()

class Mazda(Car):
    def __init__(self, truck):
        self.truck = truck
        print(f'truck = {self.truck}')
    def des(self):
        print('truck is going')

mazdaObj = Mazda('BIG ONE')
mazdaObj.des()
mazdaObj.go()


print("---------------singer--------------")
class Singer(Person):
    def __init__(self, song):
        self.song = song
        print(f'song = {self.song}')
    def sing(self):
        print('singer is singing')
singerObj = Singer('Red bones')
singerObj.sing()
singerObj.speak()
