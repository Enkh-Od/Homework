print("-------------------Class-----------------")

class exercise01:    
#өөрчлөх
    def __init__(self, a, k, l ):
        self.a = a
        self.k = k
        self.l = l 
        print(f'{self.a}, {self.k}')
        for x in self.a:
            if x % 2 != 0:
                self.k += 1 
            else:
                self.l +=1

    def exer02(self):    
        print(f'Сондгой тоо {self.k} Тэгш тоо {self.l}')



newobject = exercise01([1, 2, 3], 0, 0)
newobject.exer02()
