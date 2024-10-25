#Zadanie 28. 
# Proszę napisać program wczytujący liczbę naturalną i rozkładający ją na iloczyn 2 liczb o
# najmniejszej różnicy. Na przykład: 30 = 5 ∗ 6, 120 = 10 ∗ 12.

from math import isqrt

def rozloz(liczba):
    for i in range(isqrt(liczba)+1, 0, -1):
        if liczba%i==0:
            print(i,", ", liczba//i)
            return

rozloz(124)
