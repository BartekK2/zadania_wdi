# Zadanie 5. Pierwiastek całkowitoliczbowy z liczby naturalnej to część całkowita z pierwiastka z tej liczby.
# Proszę napisać program obliczający taki pierwiastek korzystając z zależności 1 + 3 + 5 + ... = n^2


def pierwiastek_calkowity(n):
    suma = 0
    i = 0
    # w skrócie, dodajemy do siebie kolejne elementy 1+2+3+... aż dotrzemy do punktu że dodanie kolejnej liczby 
    # wyszło by poza n, ilość dodanych liczb to nasz pierwiastek całkowitoliczbowy
    while True:
        suma += 2*i + 1
        if suma<=n:
            i += 1
        else:
            break
    print(i)



liczba = int(input("Podaj liczbę do spierwiastkowania całkowitego: "))
pierwiastek_calkowity(liczba)