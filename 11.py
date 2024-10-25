#Zadanie 11. Proszę napisać program wypisujący podzielniki liczby.

def podzielniki(liczba):
    for i in range(1, liczba+1):
        if liczba %i==0:
            print(i)

podzielniki(27)
# można w teorii zamiast liczba+1 w pętli for myśleć o liczba/2
# no bo dzielnik liczby nie będzie większy niż jej połowa (chyba że
# dzielnik który jest równy tej liczbie, ale to obojętne bo i tak 
# złożoność liniowa)