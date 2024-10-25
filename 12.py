#Zadanie 12. Proszę napisać program wypisujący rozkład liczby na czynniki pierwsze.

def rozklad(liczba):
    l = liczba
    i = 2
    while True:
        if i>l:
            break
        if l % i==0:
            print(i)
            l = l/i
            i = 2
        else:
            i += 1

rozklad(180)