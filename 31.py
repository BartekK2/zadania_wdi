# Zadanie 31. 
# Proszę napisać program wczytujący liczbę naturalną i odpowiadający na pytanie, czy liczba
# ta jest wielokrotnością dowolnego wyrazu ciągu danego wzorem An = 3 ∗ An−1 + 1, a pierwszy wyraz jest równy 2.


def sprawdz(liczba):
    a_n = 2
    while liczba>=a_n:
        if liczba%a_n==0:
            return True
        a_n=3*a_n+1
    return False

print(sprawdz(69))

#47,49,50,51,54,56,57,58,59