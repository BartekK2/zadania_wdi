#Zadanie 8. 
# Proszę napisać program rozwiązujący równanie x^x = 2024 metodą bisekcji.

def x_do_x(rowne=2024, przyblizenie=1e-5): # tak sie zapisuje domyślne wartości parametrów funkcji
    i = 0
    j = 10 # zaczne sobie od pierwszej lepszej liczby x: x**x > 2024, którą znam (jakbym zaczął od 2024 to by sie pamięć na cyfry skończyła XD)
    
    # bisekcja (której użyłem również w poprzednim zadaniu 4)
    # polega na zmniejszaniu i zwiększaniu kresów dolnych i górnych (chyba tylko ja je tak nazywam idk) aż one nam dadzą odpowiedź
    # może lepiej będzie mi to obrazowo opisać. Graliście kiedyś w pytania? Ciepło, zimno?
    # Albo wyobraźcie sobie że musicie zgadnąć o jakiej liczbie myśli wasz znajomy z zakresu 1-100
    # na początku strzelacie potem za każdym razem możecie być 2 razy bliżej odpowiedzi
    # Swoją drogą wzór Newtona z poprzedniego zadania 6 i 7 to też bisekcja.

    while True:
        srodek = (i+j)/2
        if abs(2024 - srodek**srodek) < przyblizenie: # jeżeli jestesmy wystarczajaco blisko to przerywamy algorytm
            break
        else:
            if srodek**srodek > 2024:
                j = srodek
            else:
                i = srodek

    print(i)

x_do_x()
