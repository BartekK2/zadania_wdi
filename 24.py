# Zadanie 24.
'''Pewne liczby pierwsze są palindromami i pozostają liczbami pierwszymi pomimo pozbawiania
ich skrajnych cyfr. Na przykład: 71317 → 131 → 3. Proszę napisać program, który wypisuje wszystkie takie
liczby mniejsze od N.'''

# polecam zaczac czytanie kodu od funkcji znajdz_liczby
# wiem że ostro nakomplikowałem ale myślałem nad optymalizacją i mnie poniosło a to pewnie
# nawet nie jest najlepszy najkrótszy sposób

def sito(n):
    tab = list(range(n+1)) # uzupełniam listę zerami 

    tab[0] = tab[1] = 0 # liczby 0 i 1 nie są pierwsze
    i = 2 # liczba 2 jest pierwszą liczbą pierwszą
    while i*i <= n: # (**)
        if tab[i] != 0: # jeżli liczba i jest pierwsza
            for j in range(i*i, n+1, i):
                tab[j] = 0 # wykreślamy wielokrotności liczby i
        i += 1 
    return tab # zwracamy listę z sitem

# cóż najprościej byłoby zrobić if str(l)==str(l)[::-1] ale trzeba udowodnic ze 
# potrafi sie zrobic to algorytmicznie, bez uzycja str itd
def czy_palindrom(liczba):
    # nie mozemy uzywac str itd. zatem musimy inaczej sobie wyznaczać cyfry...
    liczba_cyfr = 0
    i = 0
    while liczba//10**i != 0: # dopóki liczba dzieli sie całkowicie przez kolejne potęgi 10 (by szukać cyfr)
        liczba_cyfr += 1
        i += 1
    # mamy liczbe cyfr teraz mozemy porownywac je bezposrednio albo przez elementy w liscie, ja zrobie drugim sposobem
    lista_cyfr = [None for _ in range(liczba_cyfr)] # tworzymy pustą tablice z miejscami na cyfry
    i = 0
    while liczba//10**i != 0:
        lista_cyfr[liczba_cyfr-i-1] = (liczba % (10**(i+1)))//(10**(i)) # od konca dodajemy kolejne cyfry (reszty z dzielenia przez potegi 10)
        i += 1
    
    # teraz gdy mamy liste cyfr sprawdzamy od poczatku (i konca jednoczesnie) czy sa sobie rowne az dojdziemy do srodka
    i,j=0,liczba_cyfr-1
    while i<j: # dopóki nie dojdziemy do środka (nie będziemy porównywać środkowej cyfry samej ze sobą)
        if lista_cyfr[i] != lista_cyfr[j]:
            return False # kiedy liczba np 2 od poczatku i 2 od konca jest rozna to nie jest to palindrom
        else:
            i +=1
            j -=1
    return liczba_cyfr 
    # jezeli spelniono kazdy wymog mozemy potwierdzic ze to palindrom, zwrocmy od razu ilu cyfrowy (przyda sie)
    # a kazda liczba inna niz 0 jest traktowana jako True wiec to to samo co return True


def znajdz_liczby(N_max = 100_000):
    # jest tu duzo miejsca na optymalizacje
    # 1. Można zacząć od najpierw - wyszukania liczb pierwszych x znakowych a dopiero potem dodania 2k znakow do uzupelnienia palindromu
    # OPTYMALIZACJA JEST WAŻNA JEŚLI CHCE SIE UZYSKAĆ MAX PUNKTÓW

    # zacznijmy od dowiedzenia sie ile cyfr maksymalnie mozemy miec dla N_max
    maks_cyfr = 0
    i = 1
    while N_max//(10**i) !=0:
        maks_cyfr += 1
        i += 1

    maks_liczba = 10**(maks_cyfr) - 1 # np. 999, 99999
    # możemy użyć sita eratostenesa, żeby dostać tablice liczb pierwszych (oczywiście definiujemy ją w innej funkcji ;)
    
    pierwsze = sito(maks_liczba)
    # print(pierwsze)
    # print(list(filter(czy_palindrom, pierwsze)))
    
    # szukamy palindromów 1,2,3,4...maks_cyfrowych
    for ilosc_cyfr in range(1,maks_cyfr+1):
        for pierwsza in pierwsze:
            if czy_palindrom(pierwsza)>ilosc_cyfr:
                break
            if czy_palindrom(pierwsza):
                if czy_palindrom(pierwsza)==ilosc_cyfr: # tak wiem ze chujowy zapis ale czy_palindrom(j) zwraca liczbe cyfr XD
                    print(pierwsza, czy_palindrom(pierwsza), ilosc_cyfr)
                # mozemy dopisac liczby na poczatku i koncu by dopelnic ilosc cyfr tylko wtedy kiedy dodajac symetrycznie tyle samo
                # otrzymamy oczekiwana ilosc cyfr
                elif abs(czy_palindrom(pierwsza)-ilosc_cyfr) % 2 ==0:
                    ile_dopisac = int(abs(czy_palindrom(pierwsza)-ilosc_cyfr)/2) # ile cyfr dopisac z przodu/z tylu
                    liczba_do_wypisania = 10**(ile_dopisac)*pierwsza # zaczynamy od postawienia pierwszej po srodku
                    for k in range(ile_dopisac):
                        for j in range(1,10):
                            liczba_do_wypisania+=10**(ilosc_cyfr-k-1)
                            liczba_do_wypisania+=10**k
                            # nie chcemy wypisywac 2 razy tych samych liczb, np gdzie dopisujemy na poczatku i koncu
                            # 1 do liczby pierwszej 3, gdzie 131 też zostanie (drugi raz) wypisana jako 131 - pierwsza
                            # bez dopisanych liczb na koncu
                            # mozemy sprawdzac czy wypisywana przez nas liczba zostanie wypisana jeszcze raz
                            # (czy zawiera sie w pierwszych) w taki sposob jak ponizej poniewaz
                            # tablica pierwsze przechowuje dla kazdej liczby od 0 do n albo 0 (kiedy nie pierwsza)
                            # albo wlasnie ta pierwsza co w latwy sposob pozwala nam to sprawdzac
                            # zamiast uzywac liczba_do_wypisania in pierwsze (co zajelo by dluzej i sprawdzalo kazdy element)
                            if not pierwsze[liczba_do_wypisania]: 
                                print(liczba_do_wypisania,czy_palindrom(pierwsza), pierwsza, ile_dopisac, ilosc_cyfr, k, j)

znajdz_liczby(1_000_000)