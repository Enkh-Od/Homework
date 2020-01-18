word = "REVITAPI"
word = list(word)
guess ='_' * len(word)
guess= list(guess)

def index():
    for x in range(len(word)):
        if word[x] == a.upper():
            guess[x] = a.upper()

def toString():
    string = ''
    for x in guess:
        string = string + x
    for x in string:
        print(x, end = ' ')
    print()

while word != guess:
    a = input("Та гараас үсэг оруулна уу: ")
    index()
    toString()
print("Баяр хүргэе та зөв таалаа:")

