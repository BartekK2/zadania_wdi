#Zadanie 32. 
# Proszę napisać program wczytujący liczbę naturalną i odpowiadający na pytanie, czy jej cyfry stanowią ciąg rosnący.

def cyfry_rosna(liczba):
    # tu sobie zrobie taki myk żeby było mi łatwiej
    # to zamiast sprawdzać czy kolejne są rosnące (od przodu)
    # to sprawdze sobie czy kolejne są malejące (od tyłu)
    i = 1
    ostatnia_cyfra = None # na poczatku nie mamy z czym porownac (None to tyle co nic, pusta zmienna)
    while liczba!=0:
        cyfra = liczba%10 # reszta z dzielenia kolejnych poteg liczby 10, to kolejne cyfry 
        liczba = liczba//10
        print(cyfra)

        i += 1
        if ostatnia_cyfra:
            if cyfra>=ostatnia_cyfra:
                return False
        ostatnia_cyfra=cyfra
    return True

print(cyfry_rosna(123579)) # True
print(cyfry_rosna(12318))