# Zadanie 23. Dane są ciągi: An+1 =√(An ∗ Bn ) oraz Bn+1 = (An + Bn)/2.0. 
# Ciągi te są zbieżne do wspólnej granicy nazywanej średnią arytmetyczno-geometryczną. 
# Proszę napisać program wyznaczający średnią arytmetyczno-geometryczną dwóch liczb naturalnych.

from math import sqrt
def srednia_aryt_geo(A,B, iteracje):
    for _ in range(iteracje):
        An = sqrt(A*B)
        Bn = (A+B)/2.0
        A, B = An, Bn
        print(An) # obojetne czy An, czy Bn

srednia_aryt_geo(3,5, 100000)