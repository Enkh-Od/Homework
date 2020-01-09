
print("--------------------Дасгал 101--------------------")

class HW101:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    def хэвлэ(self):
        for x in range(self.a, self.b):
            for y in range(self.a, x+1):
                print(self.c, end = " ")
            self.c += 1
            print()
    def хэвлэ1(self):           
        for x in range(self.a, self.b):
            self.c = 1 
            for y in range(self.a, x+1):
                print(self.c, end = " ")
                self.c += 1
            print()
newObj = HW101(1, 6, 1)
newObj.хэвлэ()
newObj.хэвлэ1()

print("--------------------Дасгал 102--------------------")


#Өгөгдсөн 2 List ийг нэгтгэх. Нэгтгэхдээ эхний List -ээс зөвхөн тэгш тоог, 2 дахь List -ээс сондгой тоог нь авна.

    #List01 = [1, 2, 5, 15, 6]
    #List02 = [3, 4, 7, 11, 18]
    #mergedList = [2, 6, 3, 7, 11]

class HW102:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    def lst(self):
        for x in self.a:
            if x % 2 == 0:
                self.c.append(x)
        for x in self.b:
            if x % 2 != 0:
                self.c.append(x)
        print(self.c)

newObj = HW102([1, 2, 5, 15, 6], [3, 4, 7, 11, 18], [])
newObj.lst()

print("--------------------Дасгал 103--------------------")
#03. 1-50 хүртэлх тоон цувааг эхнээс нь хэвлэнэ. Ингэхдээ 5-д хуваагддаг тоонуудын оронд 'FIVE', 3-д хуваагддаг тоонуудын оронд 'THREE' гэж бичнэ.

class HW103:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    def ser(self):
        for x in range(1, self.a):
            if x % 3 == 0:
                x = self.b
                pass
            elif x % 5 == 0:
                x = self.c
                pass
            print(x)
newObj = HW103(50,'FIVE', 'THREE')
newObj.ser()


print("------------------- Гэрийн даалгавар дасгал 201:-------------------")

#01. Гараас өгсөн 3 тооны хамгийн бага гийг буцаах функц бичнэ үү!

class HW201:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    def minnum(self):
        if self.b >= self.a and self.c >= self.a:
            minni = self.a
        elif self.a >= self.b and self.c >= self.b:    
            minni = self.b
        else:    
            minni = self.c 
        print(f'Хамгийн бага тоо бол:{minni}')

newObj = HW201(int(input("Та эхний тоог оруулна уу: ")), int(input("Та дараагийн тоог оруулна уу: ")), int(input("Та сүүлийн тоог оруулна уу: ")))
newObj.minnum()    

print("------------------- Гэрийн даалгавар дасгал 202:-------------------")
#02. Өгөгдсөн list дэхь тоонуудын үржвэрийг буцаах функц бичнэ үү!
class HW202:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def Mul(self):
        for x in self.a:
            self.b = self.b * x 
        print(self.b)
   
newObj = HW202([1, 2, 3, 4, 5, 6, 7, 8, 9], 1)
newObj.Mul()    

print("------------------- Гэрийн даалгавар дасгал 203:-------------------")
#03. Өгөгдсөн list дэхь тоонуудын хамгийн их тоог буцаах функц бичнэ үү!

class HW203:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def Max(self):
        for x in self.a:
            if self.b < x:
                self.b = x
        print(f'Хамгийн их тоо бол: {self.b}')
newObj = HW203([1, 2, 3, 4, 5, 6, 7, 8, 9], 1)
newObj.Max()

print("------------------- Гэрийн даалгавар дасгал 204:-------------------")

class HW204:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def Fid(self):
        for x in range(1, self.a+1):
            if self.a % x == 0:
               self.b.append(x)
        print(self.b)
newObj = HW204(int(input("Гараас тоо оруулна уу: ")), [])
newObj.Fid()


print("------------------- Гэрийн даалгавар дасгал 205:-------------------")
class HW205:
    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
    def isPalindrome(self):
        self.d = self.a
        while self.d > 0:
            self.b = self.d % 10
            self.d = int(self.d/10)
            self.c = self.c*10 + self.b
        if (self.a == self.c):
            print('Палиндром тоо мөн банйа')
        else:
            print('Палиндром тоо биш банйа')
    
newObj = HW205(int(input("Гараас тоо оруулна уу: ")), 0, 0, 1)
newObj.isPalindrome()

print("------------------- Гэрийн даалгавар дасгал 206:-------------------")
class HW206:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def Fid(self):
        for x in range(1, self.a):
            if self.a % x == 0:
               self.b = x + self.b    
        if self.b == self.a:
            print('Төгс тоо мөн байна')
        else:
            print('Төгс тоо биш байна')
        
newObj = HW206(int(input("Гараас тоо оруулна уу: ")),0)
newObj.Fid()
