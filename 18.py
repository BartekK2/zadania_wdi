# Zadanie 18. 
# Nieskończony iloczyn pierwiastek(0.5) * pierwiastek(0.5 + 0.5*pierwiastek(0.5)) * ... ma wartość 2/pi
# proszę napisać program korzystający z tej zależności i wyznaczający wartość pi

# cóż naszym głównym pytaniem jest jak zrobić tak żeby te pierwiastki były "zagnieżdżone"
# na myśl przychodzi mi rekurencja, nie wiem czy ją omawialiśmy jeszcze
# w każdym razie rekurencja to wywoływanie funkcji przez samą siebie
# ja to sobie tłumaczyłem wyobrażając sobie 2 lustra stojące naprzeciwko siebie

from math import sqrt

# Funkcja rekurencyjna do obliczania zagnieżdżonych pierwiastków
# pozycja skladnika wplywa tez na ilosc zagniezdzen
def skladnik(pozycja_skladnika, max_pozycja):
    if pozycja_skladnika == max_pozycja: 
        return sqrt(0.5)
    else:
        # Rekurencyjnie wywołujemy funkcję z pierwiastkiem dodającym zagnieżdżenie
        return sqrt(0.5 + 0.5 * skladnik(pozycja_skladnika + 1, max_pozycja))

# Funkcja do obliczenia przybliżonej wartości pi na podstawie iloczynu składników
def oblicz_pi(ilosc_skladnikow):
    iloczyn = 1
    for i in range(ilosc_skladnikow):
        iloczyn *= skladnik(0, i)
    
    # Na końcu korzystamy z zależności pi = 2 / iloczyn
    pi_przyblizenie = 2 / iloczyn # wiadomo  ---- 2/(2/pi) = 2*pi/2 = pi
    return pi_przyblizenie

iteracje = 100  # Liczba iteracji dla dokładności (iteracje w tym przypadku są tym samym co ilość składników)
pi_przyblizenie = oblicz_pi(iteracje)

print(f"Przybliżona wartość pi po {iteracje} iteracjach: {pi_przyblizenie}")
