#Zadanie 27. 
# Proszę napisać program wczytujący liczbę naturalną i odpowiadający na pytanie, czy liczba
# naturalna jest palindromem, a następnie czy jest palindromem w systemie dwójkowym.

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
    return True 

print(czy_palindrom(131))

def czy_palindrom_w_bin(liczba):
    liczba_cyfr = 0
    while 2**liczba_cyfr-1<liczba:
        liczba_cyfr += 1

   # Sprawdzanie, czy binarna reprezentacja liczby jest palindromem
    for i in range(liczba_cyfr // 2):
        # Wyciągamy bit z lewej strony
        bit_lewy = (liczba // (2 ** (liczba_cyfr - i - 1))) % 2
        
        # Wyciągamy bit z prawej strony
        bit_prawy = (liczba // (2 ** i)) % 2
        
        # Jeżeli bity się różnią, to liczba nie jest palindromem
        if bit_lewy != bit_prawy:
            return False
    
    return True

print(czy_palindrom_w_bin(9))