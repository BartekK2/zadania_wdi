# Zadanie 17. 
# Proszę napisać program obliczający wartości cos(x) z rozwinięcia w szereg Maclaurina.
'''
szereg Maclaurina: (nie mam jak tego inaczej zapisać, macie w treści zadania)
cos(x) = suma od n=0--->n=niesk. (-1)^n/(2n)! * x^2n 
'''

# pamiętajcie o tym że warto dzielić kod na funkcje jeśli mowa o innej funkcjonalności
# jest czytelniejszy i to będzie ważne w ocenie
def silnia(n):
    wynik = 1
    if n==0:
        return 1
    else:
        for i in range(1,n+1):
            wynik *= i
        return wynik

def cosinus(x, iteracje):
    suma = 0
    for n in range(0, iteracje+1):
        suma += ((-1)**n)/silnia(2*n) * x**(2*n)
    return suma
# dla testu
from math import pi
print(cosinus(pi/3, 100)) 
# 0.50000000001 - wynik
# (czasami wychodzi brzydki jak dla pi/2=-1.296829575562107e-17 ale to kwestia zaokrąglenia)
