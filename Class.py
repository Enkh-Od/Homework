print("-------------------Class-----------------")

class exercise01:
    def __init__(self):
        pass
    def exer01(self):
        #01. Хэрэглэгчээс орж ирсэн тэмдэгт мөрийг урвуугаар хөрвүүлэх код бичнэ үү!
        a = input("Гараас тэмдэгт өгнө үү:")
        b = ''
        for x in a:
            b = x + b
        print(b)
#өөрчлөх
    def exer02(self):
        a = (1, 2, 3, 4, 5, 6, 7, 8, 9)
        k = 0
        l = 0 
        for x in a:
            if x % 2 != 0:
                k += 1 
            else:
                l +=1
        
        print("Сондгой тоо", k, "Тэгш тоо", l)
#өөрчлөх
    def exer03(self):
        #03. 0-6 хүртэлх тоон цуваанаас 2 болон 5-аас бусад тоог хэвлэх код бичнэ үү!
        a = [0, 1, 2, 3, 4 ,5 ,6]       
        for x in a:
            if x / 5 == 1:
                a.remove(x)
            elif x / 2 == 1:
                a.remove(x)
        print(a)
#өөрчлөх
    def exer04(self):
        a = "Books 6.7"
        count = 0
        count1 = 0
        for x in a:
            if x.isdigit():
                count += 1
            else:
                x.isalpha 
                count1 += 1
        print("Үсэг", count1, "Тоо", count)
    def exer05(self):
        l = 5
        for x in range(1, 6):
            for y in range(1, x+1):
                print("*", end = " " )
            print()
        for x in range(1, 6):
            for y in range(1, l):
                print("*", end = " " )
            l -= 1 
            print()
    def exer06(self):

        a = int(input("Та эхний тоог оруулана уу: "))
        b = int(input("Та дараагийн тоог оруулана уу: "))
        c = int(input("Та сүүлийн тоог оруулана уу: "))

        def maximum(a, b, c):

            if(a >= b) and (a >= c):
                largest = a
            elif (b >= a) and (b >= c):
                largest = b
            else:
                largest = c
            return largest

        print(maximum(a, b, c))
#өөрчлөх
    def exer07(self):
        l = [1, 2, 3, 4, 5, 6]
        def sumo(l):
            sum = 0
            for item in l:
                sum += item
            return sum
        print("Нийлбэр : ", sumo(l))

    def exer08(self):
        n = int(input("Гараас зөвхөн тоо оруулна уу: "))

        def factorial(n):
            fact = 1
            for num in range(1, n+1):
                fact *= num
            return fact
        print(factorial(n))

    def exer09(self):
        
        n = str(input("Текст: "))

        a = 0
        b = 0

        def Dictionary(a,b):
            myDictionary = {'Том үсэг':a, 'Жижиг үсэг':b}
            for x in n:
                if x.isupper():
                    a +=1
                    myDictionary['Том үсэг'] = a
                elif x.islower():
                    b +=1
                    myDictionary['Жижиг үсэг'] = b
            return myDictionary
        print(Dictionary(a,b))
#өөрчлөх
    def exer10(self):
        l = [1,'hi', 'hello', 2, 3, 5, 11, 11, 12, 12, 58, 58,]
        def newFunc(listPar):
            s = []
            for x in listPar:
                if x not in s:
                    s.append(x)
            return s
        print(newFunc(l))

    def exer11(self):

        # Өгөгдсөн тоо анхны тоо мөн эсэхийг шалгах функц бичнэ үү!
        k = int(input("Гараас тоо оруулна уу: "))

        def FirstNum(Para01):
            for x in range(2, Para01):
                if k % x == 0:
                    return False
                else:
                    return True
        print(" :", FirstNum(k))
    def exer12(self):
        def Call(a, c):
            a = int(input("Та 10 дотор тоо оруулна уу : "))
            c = int(input("Та 10 дотор тоо оруулна уу : "))
            b = []
            for x in range(0, 10):
                b.append(x)
            if  a >= 0 and a < 10 and a != c:
                b.remove(a)
                c > 0 and c < 10
                b.remove(c)
                print(b) # ДАСГАЛ А
            else:
                Call(a, c) # ДАСГАЛ Б
        (Call(100, 200))

    def exer13(self):
        def Didi():
            k = str(input("Текст оруулна уу? "))
            b = len (k)
            c = {k:b}
            print(c)# ДАСГАЛ А

        Didi()# ДАСГАЛ Б

    def exer14(self):
        def STR(k):
            b = ''
            for x in k:
                b = x + b
            print(b)
        k = (input("Гараас string text оруулна уу: "))
        print(k)       
        STR(k)       
    def exer15(self):

        def Pal(check):
            bb = ''
            for x in check:
                bb = x + bb
            if check == bb:
                print("Энэ бол Palindrome мөн байна: ", bb)
            else:
                print("Энэ бол Palindrome биш байна: ", check)
                
        check = input("Гараас текст оруулна уу: ")
        Pal(check)

        
newobject = exercise01()
newobject.exer01()
#өөрчлөх
newobject.exer02()
newobject.exer03()
newobject.exer04()

newobject.exer05()
newobject.exer06()
#өөрчлөх
newobject.exer07()
newobject.exer08()
newobject.exer09()
#өөрчлөх
newobject.exer10()
newobject.exer11()
#exer3
newobject.exer12()
newobject.exer13()
newobject.exer14()
newobject.exer15()
