#Zadanie 34. 
# Proszę napisać program wczytujący liczbę naturalną i odpowiadający na pytanie, czy liczba ta zawiera cyfrę równą liczbie swoich cyfr.


def czy_zawiera(liczba):
    ilosc_cyfr = 0
    # nie chcialo mi sie tego juz ladniej zapisywac
    # w skrocie sprawdzamy dla kolejnych poteg 10 czy liczba jest dalej jakkolwiek
    # podzielna całkowicie np 243 podzielna dla 1, 10, 100 więc 3 cyfry 
    while liczba//(10**ilosc_cyfr) !=0:
        ilosc_cyfr += 1
    

    while liczba!=0:
        cyfra = liczba%10
        liczba = liczba//10
        if cyfra==ilosc_cyfr:
            return True
    return False

print(czy_zawiera(1245)) # tak bo 4 ma 