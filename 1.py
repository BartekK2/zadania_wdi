#Zadanie 1. 
# Proszę napisać program poszukujący trójkątów Pitagorejskich w których długość przekątnej
# jest mniejsza od liczby N wprowadzonej z klawiatury.


'''
Trójkąt pitagorejski to trójkąt prostokątny, w którym długości wszystkich boków są liczbami naturalnymi.
'''
from math import isqrt, sqrt 
def pitagorejskie(N):
    N = int(N)
    # najmniejszy trojkat pitagorejski to 3,4,5, także nie ma sensu ich szukać dla przekątnej mniejszej od 5
    if N<5:
        return
    
    # z tw. pitagorasa a^2+b^2=c^2 => b^2=c^2-a^2
    # więc szukamy "a" dla którego pierwiastek z c^2-a^2 (czyli z b^2) jest całkowity
    for c in range(5, N):
        for a in range(1,c):
            b = sqrt(c**2-a**2)
            if int(b) == b:
                print(f"a={a}, b={b}, c={c}") # to po prostu ladniej zapisany print niżeli print("a=",a,"b="",b) itd.


n = input("Podaj maksymalną długość przekątnej: ")
pitagorejskie(n)
# przykladowy wynik dla N=12, co prawda wyniki sie powtarzają ale polecenie nie zabrania tego
'''
a=3, b=4.0, c=5
a=4, b=3.0, c=5
a=6, b=8.0, c=10
a=8, b=6.0, c=10
'''