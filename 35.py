# Zadanie 35. 
# Proszę napisać program wczytujący liczbę naturalną i odpowiadający na pytanie, czy liczba
# ta zakończona jest unikalną cyfrą.

def sprawdz(liczba):
    ostatnia = liczba % 10
    liczba//=10
    while liczba>0:
        if liczba%10==ostatnia:
            return False
        liczba//=10
    return True

print(sprawdz(122))