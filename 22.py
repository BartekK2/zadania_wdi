#Zadanie 22. 
# Proszę napisać program wyznaczający wartość liczby e korzystając z zależności: e = 1/0! + 1/1! + 1/2! + 1/3! + ...

def silnia(n):
    wynik = 1
    if n<1:
        return 1
    else:
        for i in range(1,n+1):
            wynik *= i
    return wynik

def e_wyznacz(iteracje):
    suma = 0
    for i in range(iteracje):
        suma += 1/silnia(i)
    return suma

print(e_wyznacz(100))

# na ćwiczeniach robiliśmy tu jakieś dziwne rzeczy w sensie
# korzystaliśmy z tego że 1/(2)! / 3 = 1(3)! .... 
# można by tak zrobić i nie tworzyć dodatkowo specjalnie funkcji silni
# imo gorszy sposob i nieczytelnie to wyglada ale kim ja jestem zeby sie z tym klocic XD
# to poniżej sposób z zajęć

def e_wyznacz2(iteracje):
    suma = 0
    ostatni_element = 1
    for i in range(1,iteracje): # pozbywamy sie zera z rendża bo mianownik mamy jako i
        suma += ostatni_element
        ostatni_element = ostatni_element/i
    return suma

print(e_wyznacz2(100))
# no i wychodzi to samo 