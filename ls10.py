print('----------------- Inheritance :: -----------------')

print('----------- Person -----------')
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        print('Person is speaking')
    
    def func(self):
        print('Person Class')

personObj = Person('Bold', '28')
personObj.speak()

# Inheritance ::
print('----------- Student -----------')

class Student(Person):
    pass

studentObj = Student('Dorj', '15')
studentObj.speak()

print('----------- Singer -----------')
class Singer(Person):

    def __init__(self, song):
        self.song = song
        print(f'song = {self.song}')

    def sing(self):
        print('singer is singing')

singerObj = Singer('Red bones')
singerObj.sing()
singerObj.speak()

print('----------- Player -----------')
class Player(Person):

    def __init__(self, team):
        self.team = team
        print(f'team = {self.team}')

    def play(self):
        print('Player is playing')
    
    def speak(self):
        print('Player is speaking')

playerObj = Player('New York Yankees')
playerObj.speak()
playerObj.play()

class New(Person):

    def __init__(self,brand):
        self.brand = brand
    
    def speak(self):
        print('new function')

newObj = New('mouse')
newObj.speak()
newObj.func()

print("-------------------------------Polimorhism--------------------")

for obj in [personObj, playerObj, studentObj, singerObj]:
    obj.speak()

def speak(obj):
    obj.speak()

speak(personObj)
speak(playerObj)
speak(newObj)
speak(singerObj)


print("-------------------------------Special Method--------------------")

class specialClass():
    
    def __init__(self, var01, var02):
        self.a = var01
        self.b = var02
   
    def __str__(self):
        return(f'a = {self.a}, b = {self.b}')

    def __add__(self, other):
        total_a = self.a + other.a
        total_b = self.b + other.b
        return specialClass(total_a, total_b)


    def __mod__(self, other):
        total_a = self.a % other.a
        total_b = self.b % other.b
        return specialClass(total_a, total_b)
   
    def __sub__(self, other):
        total_a = self.a - other.a
        total_b = self.b - other.b
        return specialClass(total_a, total_b)
        
    def __mul__(self, other):
        total_a = self.a * other.a
        total_b = self.b * other.b
        return specialClass(total_a, total_b)

    def __floordiv__(self, other):
        total_a = self.a // other.a
        total_b = self.b // other.b
        return specialClass(total_a, total_b)

obj01 = specialClass(12, 17)
obj02 = specialClass(3, 4)
obj03 = obj01 + obj02
print('+ ::', obj03)

obj03 = obj01 % obj02
print('% ::', obj03)


obj03 = obj01 - obj02
print('- ::', obj03)

obj03 = obj01 * obj02
print('* ::', obj03)

obj03 = obj01 // obj02
print('// ::', obj03)

print("------------------@classmethond, @ staticmethod--------------------")

class Circle:
    geometry = True

    def __init__(self, radius = 10):
        self.radius = radius

    @classmethod
    def classCircle(cls, radius):
        cls.geometry = False
        return cls(radius)
    @staticmethod
    def staticCircle(cls, radius):
        print('Static Method')

print("Circle.geometry = ", Circle.geometry)

#True
circle01 = Circle(15)

print("circle01.geometry = ", circle01.geometry)
print("Circle.geometry = ", Circle.geometry)

circle02 = Circle.classCircle(20)

print("circle01.radius = ", circle01.radius)
print("circle02.radius = ", circle02.radius)


print("circle01.geometry = ", circle01.geometry)
print("circle02.geometry = ", circle02.geometry)
print("Circle.geometry = ", Circle.geometry)

print('----------------------- A -----------------------')

class A:
    name = 'Bold'

    @classmethod
    def changeName(cls):
        cls.name = 'Bat'
print('A.name =', A.name)
A.changeName()
print('A.name =', A.name)

print('----------------------- B -----------------------')

class B:
    name = 'Bold'

    @classmethod
    def changeName(cls, var):
        cls.name = var

print('B.name =', B.name)
B.changeName('Dorj')
print('B.name =', B.name)

print('----------------------- C -----------------------')

class C:
    var = 'class C'

    def __init__(self):
        pass

    def func01(self,par):
        self.var = par
        print('self.var = ', self.var)
    @classmethod
    def func02(cls, par):
        cls.var = par

print('C.var =', C.var)
print('\r')
C.func02('class Method')
print('C.var =', C.var)
print('\r')
cObj = C()
cObj.func01('Normal Method')
print('cObj.var', cObj.var)
print('\r')
print('C.var =', C.var)

print('----------------------- D -----------------------')

class D:
    var = 'class D'

    def __init(self, var):
        pass
    def func01(self):
        print('self.var = ', self.var)
    @classmethod
    def func02(cls, var, var1):
        cls.var = var + var1

dObj = D()
print(D.var)

dObj.func01()

print(dObj.var)
D.func02(3, 5)
dObj.func01()

print(dObj.var)
