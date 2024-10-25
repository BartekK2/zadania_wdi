#Zadanie 21. 
# Proszę napisać program wyznaczający wartość do której zmierza iloraz dwóch kolejnych
# wyrazów ciągu Fibonacciego. Wyznaczyć ten ilorazy dla różnych wartości dwóch początkowych wyrazów ciągu.

# funkcja z zad 2. (tylko przeniosłem sobie 2 wyrazy początkowe do argumentów funkcji)
def fib(iteracje=1000, a=1,b=1):
    i = 0
    while i< iteracje:
        c=a+b
        a=b
        b=c
        i += 1
    print(b/a)

fib()  # 1.618
fib(iteracje=1000, a=10, b=779) # 1.618

# swoją drogą 1.618 to złota liczba, złoty podział - poczytajcie sobie