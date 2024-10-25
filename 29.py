# Zadanie 29. 
# Proszę napisać program wczytujący liczbę naturalną i odpowiadający na pytanie, czy liczba
# ta jest wielokrotnością dowolnego wyrazu ciągu danego wzorem A_n = n ∗ n + n + 1.

# liczba = k(n*n+n+1)

def sprawdz(liczba):
    i = 1
    while liczba>=(i*i+i+1):
        if liczba%(i*i+i+1)==0:
            return True
        i += 1
    return False


print(sprawdz(31))