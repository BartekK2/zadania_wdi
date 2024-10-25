#Zadanie 30. 
# Proszę napisać program, który oblicza pole figury pod wykresem funkcji y = 1/x w przedziale
# od 1 do k, metodą prostokątów.

def f(x):
    return 1/x

def pole(k, eps):
    suma = 0
    i = 1
    while i<=k:
        suma += eps*f(i)
        i+= eps

    return suma

print(pole(3, 1e-6))