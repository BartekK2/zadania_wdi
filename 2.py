# Zadanie 2. 
# Proszę napisać program wypisujący elementy ciągu Fibonacciego mniejsze od miliona

# Cóż większej filozofii tu nie ma, wypisujemy kolejne elementy ciągu fibbonaciego
# Dopóki któryś nie przekroczy miliona

# Oczywiście ciąg fib. definiujemy jako f1=f2=1, fn=f(n-1)+f(n-2)

def fib(maks):
    a=b=1
    while a< maks:
        print(a)
        c=a+b
        a=b
        b=c

fib(1_000_000) # te podkreslenia to sie stosuje tylko po to żeby ładniej zapisywać duże liczby