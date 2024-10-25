#Zadanie 25. 
# Proszę napisać program wczytujący liczbę naturalną i odpowiadający na pytanie, czy liczba 
# ta jest iloczynem dowolnych dwóch wyrazów ciągu Fibonacciego.
from math import sqrt
def fib(ilosc):
    tab = [None for _ in range(ilosc)] # puste sloty na liczby
    tab[0]=tab[1]=1
    i = 2
    while i<ilosc:
        tab[i]=tab[i-1]+tab[i-2]
        i += 1
    print(tab)
    return tab

def sprawdz_czy(liczba):
    liczby_fib = fib(100) # dobrze byloby to ograniczyc od liczby np fib(sqrt(x)) no ale przeciez appenda nie mozna uzywac wiec lipa wtedy
    for i in range(1000):
        if liczby_fib[i]>liczba/2: # calkowity czynnik iloczynu 2 skladnikow nie moze byc wiekszy niz polowa wyniku
            break # czyli po prostu zamykamy pętle dla optymalizacji
        for j in range(i, 1000):
            if liczby_fib[j]>liczba/2:
                break
            if liczby_fib[i]*liczby_fib[j] == liczba:
                print(liczby_fib[i],liczby_fib[j])
                return True
    return False
sprawdz_czy(10)