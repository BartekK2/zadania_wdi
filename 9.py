#Zadanie 9. Proszę napisać program wczytujący liczbę naturalną i odpowiadający na pytanie, czy liczba
# ta jest iloczynem dowolnych dwóch kolejnych wyrazów ciągu Fibonacciego.

# Skopiujmy sobie znowu z zad 2 funkcje fib_maks, i troche ją poprzekształcajmy

from math import sqrt
def fib(liczba):
    a=b=1
    jest_iloczynem = False
    while a<=sqrt(liczba): # Szukamy do a=sqrt(x), bo sqrt(x)*b > x, dla b>sqrt(x) 
        if a*b == liczba:
            jest_iloczynem = True
        c=a+b
        a=b
        b=c
    print(jest_iloczynem)
