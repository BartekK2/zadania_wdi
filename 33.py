#Zadanie 33. 
# Proszę napisać program wczytujący liczbę naturalną i odpowiadający na pytanie, czy jej cyfry stanowią ciąg geometryczny.

def czy_cyfry_geo(liczba):
    ostatnia_cyfra = None
    iloraz = None
    while liczba!=0:
        cyfra = liczba%10
        liczba = liczba//10

        if iloraz and ostatnia_cyfra:
            if cyfra/ostatnia_cyfra != iloraz:
                return False
        if ostatnia_cyfra:
            iloraz = cyfra/ostatnia_cyfra
        ostatnia_cyfra = cyfra


    return True

print(czy_cyfry_geo(248))