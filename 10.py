# Zadanie 10. Proszę napisać program sprawdzający czy zadana liczba jest pierwszą.

from math import isqrt
def czy_pierwsza(liczba):
    # ponownie, jak w poprzednim zadaniu ograniczamy sie do pierwiastka 
    # z liczby bo dzielnik nie może być od tego pierwiastka większy
    # isqrt to pierwiastek całkowity, a +1 dodaje tylko dlatego że nie jestem pewny czy zaokrąglając w dół niczego nie strace
    pierwsza = True
    for i in range(2, isqrt(liczba)+1):
        if liczba %i==0:
            pierwsza = False
            break
    print(pierwsza)

czy_pierwsza(271)