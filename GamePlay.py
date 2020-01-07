# дэлгэц
# дэлгэц харуулах
# Тоглоом
# Тоглогчыг илрүүлэх
# Ялсан уу
    # Мөрийг шалгах
    # Баганыг шалгах
    # Диагналыг шалгах
# Тэнцсэн үү
# Тоглогчийг солих

# дэлгэц
дэлгэц = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
# тоглож буй тоглогч
o_тоглогч = "x"
тоглож_байна_уу = True
ялагч = None

def дэлгэц_харуулах():
    print('{0:1} | {1:1} | {2:1}'.format(дэлгэц[0], дэлгэц[1], дэлгэц[2]))
    print('{0:1} | {1:1} | {2:1}'.format(дэлгэц[3], дэлгэц[4], дэлгэц[5]))
    print('{0:1} | {1:1} | {2:1}'.format(дэлгэц[6], дэлгэц[7], дэлгэц[8]))  

def тоглоом():
    дэлгэц_харуулах()
    while тоглож_байна_уу:
        тоглогчийг_илэрүүлэх(o_тоглогч)
        тоглоом_дууссан_уу()
        тэнцсэн_үү()
        тоглогчийг_солих()
    if ялагч == "o" or ялагч == "x":
       print(ялагч + " тоглогч яллаа")
    elif ялагч == None:
       print("тэнцлээ")
def тоглогчийг_илэрүүлэх(тоглогч):

    print(тоглогч + " -н ээлж")
    байрлал = input("Гараас 1-9 хооронд тоо оруулна уу: ")

    valid = False
    while not valid:
        while байрлал not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            байрлал = input("Гараас 1-9 хооронд тоо оруулна уу:")
        байрлал = int(байрлал)-1
        if дэлгэц[байрлал] == " ":
            valid = True
        else:
            print("Та дахиад оруулна уу.")
      
    дэлгэц[байрлал] = тоглогч
    дэлгэц_харуулах()

def тоглоом_дууссан_уу():
    ялсан_уу()
    тэнцсэн_үү()

    return    
def ялсан_уу():
    global ялагч
    мөр_ялагч = мөр_шалгах()
    багана_ялагч = багана_шалгах()
    диаг_ялагч = диаг_шалгах()

    if мөр_ялагч:
        ялагч = мөр_ялагч
    elif багана_ялагч:
        ялагч = багана_ялагч
    elif диаг_ялагч:
        ялагч = диаг_ялагч
    else:
        ялагч = None
    return

def мөр_шалгах():
    global тоглож_байна_уу
    мөр1  = дэлгэц[0] == дэлгэц[1] == дэлгэц[2] !=" " 
    мөр2  = дэлгэц[3] == дэлгэц[4] == дэлгэц[5] !=" "
    мөр3  = дэлгэц[6] == дэлгэц[7] == дэлгэц[8] !=" "
    if мөр1 or мөр2 or мөр3:
        тоглож_байна_уу = False
    if мөр1:
        return дэлгэц[0]
    elif мөр2:
        return дэлгэц[3]
    elif мөр3:
        return дэлгэц[6]
    return

def багана_шалгах():
    global тоглож_байна_уу
    багана1  = дэлгэц[0] == дэлгэц[3] == дэлгэц[6] !=" " 
    багана2  = дэлгэц[1] == дэлгэц[4] == дэлгэц[7] !=" "
    багана3  = дэлгэц[2] == дэлгэц[5] == дэлгэц[8] !=" "
    if багана1 or багана2 or багана3:
        тоглож_байна_уу = False
    if багана1:
        return дэлгэц[0]
    elif багана2:
        return дэлгэц[1]
    elif багана3:
        return дэлгэц[2]
    return

def диаг_шалгах():
    global тоглож_байна_уу
    диаг1  = дэлгэц[0] == дэлгэц[4] == дэлгэц[8] !=" " 
    диаг2  = дэлгэц[2] == дэлгэц[4] == дэлгэц[6] !=" "
    if диаг1 or диаг2:
        тоглож_байна_уу = False
    if диаг1:
        return дэлгэц[0]
    elif диаг2:
        return дэлгэц[2]
    return

def тэнцсэн_үү():
    return

def тоглогчийг_солих():
    global o_тоглогч 
    if o_тоглогч == "x":
       o_тоглогч = "o"
    elif o_тоглогч == "o":
         o_тоглогч = "x"
    return
тоглоом()




