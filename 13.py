'''
Zadanie 13. Liczba doskonała to liczba równa sumie swoich podzielników właściwych (mniejszych od
jej samej), na przykład 6 = 1 + 2 + 3. Proszę napisać program wyszukujący liczby doskonałe mniejsze od
miliona
'''
from math import sqrt

def suma_dzielnikow_wlasciwych(liczba):
    suma = 1 # bo 1 jest dzielnikiem zawsze
    for i in range(2, int(sqrt(liczba)+1)):
        if liczba %i ==0:
            suma += i
            if i != liczba // i:
                suma += liczba//i # bo skoro x dziely y to y/x = z, gdzie z to też całkowita i y/z=x, zatem z to też dzielnik
    return suma

def znajdz_liczby_doskonale(limit):
    for liczba in range(2, limit):
        if liczba == suma_dzielnikow_wlasciwych(liczba):
            print(liczba)

znajdz_liczby_doskonale(4_000_000)