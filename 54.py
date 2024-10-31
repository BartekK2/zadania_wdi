#Zadanie 54. 
# Proszę napisać program wczytujący dwie liczby naturalne a, b i wypisujący rozwinięcie dziesiętne ułamka a/b uwzględniając ułamki okresowe. Na przykład 2/3 = 0.(6), 1/5 = 0.2, 1/6 = 0.1(6), 1/7 =
# 0.(142857)

# a = int(input("Podaj a: "))
# b = int(input("Podaj b: "))

def rozwiniecie(a,b):
    rozw = 0
    licznik = a%b # zacznijmy od razu od reszty z dzielenia bo calkowite dodamy pozniej
    i = 0 # kolejne potegi 10 (10**i), do dodawania n-tych cyfr
    while True:
        if licznik//b==0: # na przykład przy 2/3 pisemnie robimy 0. + 20/3 (6) = 0.6...
            licznik *= 10
            i += 1
        rozw += licznik//b/10**i # dodajemy reszte z dzielenia np. 20/3=6 ale na konkretnym miejscu po przecinku
        licznik = licznik % b
        
        if licznik==a%b:
            if licznik==0:
                return rozw+a//b
            return f"{a//b}.({int(rozw*10**i)})"
        
print(rozwiniecie(1,7))