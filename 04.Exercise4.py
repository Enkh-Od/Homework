print("--------------------Дасгал 101--------------------")

class ex101:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def reverse(self):
        
        for x in self.a:
            self.b = x + self.b
        print(f'Үр дүн: {self.b}')
newObj = ex101(input("Гараас тэмдэгт өгнө үү:"), ' ')
newObj.reverse()

print("--------------------Дасгал 102--------------------")
class ex102:
    def __init__(self, a, k, l):

        self.a = a
        self.k = k
        self.l = l
    def find(self):
        for x in self.a:
            if x % 2 != 0:
                self.k += 1 
            else:
                self.l +=1
        print(f'Сондгой тоо: {self.k} Тэгш тоо: {self.l}')
newObj = ex102((1, 2, 3, 4, 5, 6, 7, 8, 9), 0, 0)
newObj.find()

print("--------------------Дасгал 103:--------------------")
class ex103:
    def __init__(self, a):
        self.a = a
    def search(self):      
        for x in self.a:
            if x / 5 == 1:
                self.a.remove(x)
            elif x / 2 == 1:
                self.a.remove(x)
        print(f'Үр дүн: {self.a}')

newObj = ex103([0, 1, 2, 3, 4 ,5 ,6])
newObj.search()

print("--------------------Дасгал 104:--------------------")   
class ex104:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    def look(self):
        for x in self.a:
            if x.isdigit():
                self.b += 1
            else:
                x.isalpha 
                self.c += 1
        print(f'Тоо: {self.b} Үсэг: {self.c}')
newObj = ex104("Books 6.7", 0, 0)
newObj.look()

print("--------------------Дасгал 105:--------------------")   

class ex105:
    def __init__(self, a):
        self.a = a
    def see(self):
        for x in range(1, 6):
            for y in range(1, x+1):
                print("*", end = " " )
            print()
        for x in range(1, 6):
            for y in range(1, self.a):
                print("*", end = " " )
            self.a -= 1 
            print()
newObj = ex105(5)
newObj.see()

print("---------------------- Гэрийн Даалгавар 201 ---------------------- ")
# Гараас өгсөн 3 тооны хамгийн ихийг буцаах функц бичнэ үү!
class ex201:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    def maximum(self):

        if(self.a >= self.b) and (self.a >= self.c):
            max = self.a 
        elif (self.b >= self.a) and (self.b >= self.c):
            max = self.b
        else:
            max = self.c        
        print("Хамгийн их тоо бол:", max)
newObj = ex201(int(input("Та эхний тоог оруулана уу: ")),int(input("Та дараагийн тоог оруулана уу: ")), int(input("Та сүүлийн тоог оруулана уу: ")))
newObj.maximum()

print("---------------------- Гэрийн Даалгавар 202 ---------------------- ")
# Өгөгдсөн list дэхь тоонуудын нийлбэрийг буцаах функц бичнэ үү!
class ex202:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def sum(self):
        for item in self.a:
            self.b = self.b + item
        print(f'Нийлбэр:{self.b}')
    
newObj = ex202([1, 2, 3, 4, 5, 6], 0)
newObj.sum()

print("---------------------- Гэрийн Даалгавар 203 ---------------------- ")
# Өгөгдсөн тооны factorial - ыг олох функц бичнэ үү!
class ex203:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def factorial(self):
        for num in range(1, self.a+1):
            self.b= self.b * num
        print(f'factorial бол: {self.b}')
newObj = ex203(int(input("Гараас зөвхөн тоо оруулна уу: ")), 1)
newObj.factorial()

print("---------------------- Гэрийн Даалгавар 204 ---------------------- ")
#04. Өгөгдсөн текстэд том үсэг болон жижиг үсэг тус тус хэд байгааг олоод dictionary байдлаар үр дүнг буцаах функц бичнэ үү!

class ex204:
    def __init__(self, a, b, k1, k2):
        self.a = a    
        self.b = b 
        self.k1 = k1
        self.k2 = k2  
    def Dictionary(self):
        for x in self.a:
            if x.isupper():
               self.k1 += 1
               self.b = {"Том Үсэг": self.k1, "Жижиг Үсэг": self.k2}
            elif x.islower():
               self.k2 += 1    
               self.b = {"Том Үсэг": self.k1, "Жижиг Үсэг": self.k2}
        print(self.b)

newObj = ex204(input("Гараас зөвхөн текст оруулна уу: "),{}, 0, 0)
newObj.Dictionary()


print("---------------------- Гэрийн Даалгавар 205 ---------------------- ")
#05. Өгөгдсөн list - ээс давхардсан элемэнтүүдийг арилгасан элемэнт тус бүр нэг удаа орсон шинэ list буцаах функц бичнэ үү!

class ex205:
    def __init__(self, a, b):
        self.a = a      
        self.b = b
    def newFunc(self):
        for x in self.a:
            if x not in self.b:
                self.b.append(x)
        print(self.b)
newObj = ex205([1,'hi', 'hello', 2, 3, 5, 11, 11, 12, 12, 58, 58,],[])
newObj.newFunc()


print("---------------------- Гэрийн Даалгавар 206 ---------------------- ")
# Өгөгдсөн тоо анхны тоо мөн эсэхийг шалгах функц бичнэ үү!
class ex205:
    def __init__(self, a):
        self.a = a      

    def FirstNum(self):
        for x in range(2, self.a):
            if self.a % x == 0:
               self.a = False
            else:
               self.a = True 
        print(self.a)
        
newObj = ex205(int(input("Гараас тоо оруулна уу: ")))
newObj.FirstNum()

print("---------------------- Гэрийн Даалгавар 301 ---------------------- ")

class ex301:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c    
        
    def main(self):        
        while self.a not in self.c:
            self.a = int(input("Гараас эхний тоог дахин оруулна уу: "))
        self.c.remove(self.a) 
        while self.b not in self.c:
            self.b = int(input("Гараас хоёр дахь тоог дахин тоо оруулна уу: "))            
        self.c.remove(self.b)      
        print(f'Үр дүн: {self.c}')         
newObj = ex301(int(input("Гараас эхний тоог оруулна уу: ")),int(input("Гараас дараагийн тоог оруулна уу: ")),[1,2,3,4,5,6,7,8,9])   
newObj.main()

print("---------------------- Гэрийн Даалгавар 302 ---------------------- ")
"""
02. Гараас өгсөн string ийн бүх тэмдэгт хэд байгааг dict төрлөөр А. хэвлэх үйлдэл хийнэ үү,
                                                                 Б. буцаах функц бичнэ үү, 
"""
class ex302:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def didi(self):
        self.b = {len(self.a)}

        print(f"{self.b}")

newObj = ex302(input("Текст оруулна уу? "),{})
newObj.didi()

print("---------------------- Гэрийн Даалгавар 303 ---------------------- ")

"""
03. Давталт ашиглан string ийн урвуу утгийг А. хэвлэх үйлдэл хийнэ үү,
                                            Б. буцаах функц бичнэ үү,  
"""
class ex303:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def STR(self):
        
        for x in self.a:
            self.b = x + self.b
        print(self.b)
newObj = ex303(input("Текст оруулна уу? ")," ")
newObj.STR()

print("---------------------------- Дасгал 304:---------------------------- ")
"""
04. Гараас өгсөн string хувьсагч palindrome мөн эсэх ийг А. хэвлэх үйлдэл хийнэ үү,
                                                         Б. буцаах функц бичнэ үү,      
"""
class ex304:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def Pal(self):
        for x in self.a:
            self.b = x + self.b
        if self.a == self.b:
            print("Энэ бол Palindrome мөн байна: ", self.b)
        else:
            print("Энэ бол Palindrome биш байна: ", self.a)
          
newObj = ex304(input("Текст оруулна уу? "),'')
newObj.Pal()
