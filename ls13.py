print("-------------------------  Functional Programming:: -------------------------")



print("-------------------------  zip():: -------------------------")
names = ['Bat','Dorj', 'Dulam', 'Dagva' ] #list
ages = (22, 20, 19, 57, 41, 26) #tuple
genders = {'Male', 'Female', 'Female', 'Female', 'male' }#set

print(list(zip(names, ages, genders)))
print(set(zip(names, ages, genders)))
print(tuple(zip(names, ages, genders)))




#function()

def newFunc(temp):return temp + 10
print('function ::', newFunc(10))
#20
#lambda()

var = lambda temp : temp + 10
print('lambda ::', var(10))

var = lambda par01, par02: par01 + par02
print('lambda ::', var(25, 47))

#72

def myFunc(par):
    return lambda temp: temp*par
lambdaVar = myFunc(5) #lambdaVar = lambda temp: temp
print('lambdaVar :', lambdaVar)
print(lambdaVar(2)) # return 2 * 5
print(lambdaVar(3)) # return 3 * 5
print(lambdaVar(4)) # return 4 * 5

def new(par01, par02):
    return lambda temp1:temp1 * par01 * par01
lambdaVar1 = new(5, 6)
print(lambdaVar1(5))
print(lambdaVar1(4))
print(lambdaVar1(3))

print("-------------------------  Comperehension:: -------------------------")

# set, dict, list
#01. List:: for, loop
items = []
for n in range(10):
    items.append(n)
print('for loop ::', items)

#02. List:: map()
def mapFunc(item):
    return item
print('map::', list(map(mapFunc, range(10))))

 #03. List:: Comprehension
items = [i for i in range(10)]
print('Comerenhension::', items)

# set:: Comperhension

items = {i for i in range(10)}
print('Comerenhension::', items)

# Dict:: Comprehension

myDict ={i: i + 1 for i in range(10)}
print('Dict Comprehension::', myDict)

oldDict = {'bold':21, 'bat':31,'nyamaa':41}

newDict = {k: v*2 for (k,v) in oldDict.items()}
print('Dict Comprehension::', newDict)

newDict = {k * 2: v + 1 for (k,v) in oldDict.items()}
print('Dict Comprehension::', newDict)

print("-------------------------  Decorators :: -------------------------")

def my_wtrapper(func):
    def inner_func():
        print('inside wrapper')
        func()
    return inner_func
def print_it():
    print('print_it function')

var = my_wtrapper(print_it)
var()

@my_wtrapper
def print_it():
    print('print_it function 2')
print_it()

print("-------------------------  Error Handling :: -------------------------")

#try, except, else, finally

#print("Hello, python")

try: 
    print(a)
except:
    print('Exception #1')

try: 
    age = int(input('Age = '))
    100 /age

except ValueError as val_err:
    print(f'Exception:: {val_err}')

except ZeroDivisionError as zero_err:
    print(f'Exception:: {zero_err}')
else: 
    print('no exception')
finally:
    print("It's Final")

