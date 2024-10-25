from math import isqrt

def suma_dzielnikow_wlasciwych(liczba):
    suma = 1  # Zaczynamy od 1, bo jest to dzielnik każdej liczby
    for i in range(2, isqrt(liczba) + 1):
        if liczba % i == 0:
            suma += i
            if i != liczba // i:  # Dodajemy również parę dzielników
                suma += liczba // i
    return suma

def znajdz_zaprzyjaznione_liczby(limit):
    zaprzyjaznione_pary = []

    for a in range(2, limit):
        b = suma_dzielnikow_wlasciwych(a)  # Suma dzielników a
        if b > a:  # Aby uniknąć duplikatów i porównać tylko różne liczby
            if suma_dzielnikow_wlasciwych(b) == a:  # Sprawdzamy, czy b jest zaprzyjaźnione z a
                zaprzyjaznione_pary.append((a, b))

    return zaprzyjaznione_pary

# Szukamy liczb zaprzyjaźnionych mniejszych niż 1 milion
zaprzyjaznione = znajdz_zaprzyjaznione_liczby(1_000_000)

# Wypisujemy wyniki
print("Liczby zaprzyjaźnione mniejsze niż milion:")
for para in zaprzyjaznione:
    print(para)
