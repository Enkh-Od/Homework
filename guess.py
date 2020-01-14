print("Үг таадаг тоглоом") 
class аbb:

    def __init__(self, a, b, c):

        self.a = a
        self.b = b
        self.c = c

    def check(self):
        index = self.a
        self.c = len(self.a) * self.c
        d = ''
        print(self.c)
        for x in self.a:
            d[x] = index(x)
        print(d) 
    
ab = аbb("wow", input(" Гараас үсэг оруулна уу: ")," _ ")
ab.check()

"""

letter.upper() in word:
			index = word.index(letter.upper())
			guessed[index] = letter.upper()
			word[index] = '_'
"""