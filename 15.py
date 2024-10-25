# Zadanie 15. Proszę napisać program wyznaczający największy wspólny dzielnik 3 zadanych liczb naturalnych

# algorytm Euklidesa wyznaczania największego wspólnego dzielnika 
def nwd(a, b):
    while b != 0:
        a, b = b, a % b # ważne! lepiej używąć % (modulo) niż a-b, jak w oryginale. Garek mówił
    return a


# jeżeli chcemy znaleźć największy wspólny dzielnik 3 liczb
# to teoretycznie moglibyśmy wypisać do 3 list każdy z tych dzielników
# a potem sprawdzić które z nich pojawia sie w każdej z tych list
# a następnie wybrać najmniejszy
# może tego tutaj nie widać na pierwszy rzut oka ale mniej więcej to dzieje sie
# po zrobieniu nwd(nwd(x,y), z)
def nwd_trzech_liczb(x, y, z):
    return nwd(nwd(x, y), z) 