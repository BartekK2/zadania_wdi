#Zadanie 6. Proszę napisać program wyznaczający pierwiastek kwadratowy ze wzoru Newtona.

def pierwiastek(S, przyblizenie):
    a=S
    while True:
        an=(S/a+a)/2 # wzór wytłumaczony w zadaniu 7
        if abs(a-an)<przyblizenie:
            break
        a=an
    print(a)

pierwiastek(117, 1e-10) # naszym przybliżeniem jest 1e-10, co jest zapisane w notacji matematycznej i jest równe 0.0000000001
