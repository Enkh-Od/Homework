print('--------------lesson11---------------')

"""
Everything is object

"""
#int var, int class
var = 1
print(type(var))

#isinstance()
print(isinstance(var, object))
print(isinstance(var, int))

print('--------------- super()---------------')

class A:
    def __init__(self):
        self.a = 'Class A, Parent class'
    def change(self):
        self.a = 'changed_A'
class B(A):
    def __init__(self):
        self.b = 'Class B, Child Class'

class C:
    def __init__(self):
        self.c = 'Class C, Parent Class'
    def change(self):
        self.c = 'changed_C'
class D(C):
    def __init__(self):
        super().__init__()
        self.d = 'Class D, Child Class'
dObj = D()
print('dObj.c = ', dObj.c)

class E:
    def __init__(self, par):
        self.e = 'Class E, Parent Class'
        self.atr = par
    def change(self):
        self.e = 'changed_E'
class F(E):
    def __init__(self):
        super().__init__('F Class')
        self.f = 'Class F, Child Class'
fObj = F()
print('fObj.e =', fObj.e)
print('fObj.atr =', fObj.atr)


class G:
    def __init__(self, par01, par02):
        self.name = par01
        self.age = par02
    
class H(G):
    def __init__(self, par01, par02):
        super().__init__(par01, par02)
        self.par = 'Class H, Child Class'

hObj = H('bat', 29)
#print('hObj.h =', gObj.a)
print('hObj.atr =', hObj.name)
print('hObj.atr =', hObj.age)


class J:
    def __init__(self, par01, par02):
        self.name = par01
        self.age = par02
class K(J):
    def __init__(self, par01, par02):
        J.__init__(self, par01, par02) 

kObj = K('Dorj', 19)
print('kObj.name', kObj.name)      
print('kObj.name', kObj.age)      
        
class A:
    aArg = 'AAA'

    def __init__(self):
        self.a = 'a'
    def aMethod(self):
        return 'a Method'

class B(A):
    bArg = 'BBB'
    def bMethod(self):
        return 'b Method'


class C(A):
    cArg = 'CCC'
    def cMethod(self):
        return 'c Method'

class D(B, C):
    pass

print('D.aArg', D.aArg)
print('D.aArg', D.bArg)
print('D.aArg', D.cArg)

print('D().aMethod() =', D().aMethod())
print('D().bMethod() =', D().bMethod())
print('D().cMethod() =', D().cMethod())

dObj =D()
print('dObj.aMethod() =', dObj.aMethod())
print('dObj.bMethod() =', dObj.bMethod())
print('dObj.cMethod() =', dObj.cMethod())

print("---------------------------- MRO(Method resolution oreder)--------------------")

print('D.mro() = ', D.mro())
print('\r')
print('D.__mro__ = ', D.__mro__)
print('dir(dObj)', dir(dObj))

print("---------------------------- Functional Programming : : --------------------")

print("---------------------------- map() : --------------------")

def mulByTwo(item):
    return item*2
print(list(map(mulByTwo, [1, 2, 3, 4,])))
print(set(map(mulByTwo, [1, 2, 3, 4,])))
print(tuple(map(mulByTwo, [1, 2, 3, 4,])))

def mulBy():
    a = [1, 2, 3, 4]
    b =[]
    for x in a:
        c = x*2 
        b.append(c)
    print(b)
mulBy()

print("---------------------------- filter() : --------------------")

def findOddFind(item):
    return item % 2 == 1
print(list(filter(findOddFind, [1, 2, 3, 4, 5, 6, 7, 8, 9])))

def findOdd():
    a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    b = []
    for x in a:
        if x % 2 == 1:
            b.append(x)
    print(b)
findOdd()

def findOdd1(item):
    a = []
    for x in item:
        if x % 2 == 1:
            a.append(x)
    return a
print(findOdd1([1, 2, 3, 4, 5, 6, 7, 8, 9]))

def new(item):
    return item**2 <= 25
print(list(filter(new, [1, 2, 3, 4, 5, 6, 7, 8, 9])))



