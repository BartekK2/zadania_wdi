# Zadanie 4. 
# Proszę napisać program sprawdzający czy istnieje spójny podciąg ciągu Fibonacciego o zadanej sumie.

# Myśle że dobrym pomysłem było by tu użycie bisekcji
def znajdz_podciag_fib(suma_docelowa):
    # te kombinowanie z liczbą elementów w liście to tylko dlatego że garek zabronił używania funkcji
    # wbudowanej która dodaje elementy do listy więc najpierw dowiedzmy sie jaki ma rozmiar żeby ją stworzyć
    ilosc_el = 0

    # to co w zad. 2 czyli generowanie ciagu fib - teraz tylko po to by wiedziec ile elementow
    a=b=1
    while a< suma_docelowa:
        c=a+b
        a=b
        b=c
        ilosc_el += 1
    lista_elementow = [0 for _ in range(ilosc_el)]
    # teraz mamy odpowiednio dużą liste żeby zawrzeć wszystkie elementy ciągu aż do takiego który jest >= suma 
    
    # to co w zad. 2 czyli generowanie ciagu fib - teraz po to by miec je w liscie
    a=b=1
    i = 0
    while a< suma_docelowa:
        lista_elementow[i] = a
        i += 1

        c=a+b
        a=b
        b=c

    # i możemy zacząć z metodą bisekcji (czyli tak jakby kres dolny i górny który odpowiednio 
    # zwiększamy i zmniejszamy aż dostaniemy sume lub okaże sie że takowa nie istnieje)
    i=j=0
    while True:
        suma_podciagu = 0
        # sumujemy sobie każdy element z podciągu od elementu o indeksie i aż do elementu o indeksie j
        for k in range(i,j):
            suma_podciagu += lista_elementow[k]

        if suma_podciagu<suma_docelowa: # suma za mała, zwiększamy kres górny
            j += 1
        elif suma_podciagu>suma_docelowa: # suma za duża, zwiększamy kres dolny
            i += 1
        else:
            print("Istnieje", i,j)
            break

        if i>j or i>ilosc_el or j>ilosc_el:
            print("Nie istnieje")
            break
        

znajdz_podciag_fib(10) # Istnieje 2 5