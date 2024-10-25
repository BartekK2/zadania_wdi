#Zadanie 7. 
# Proszę zmodyfikować wzór Newtona aby program z poprzedniego zadania obliczał pierwiastek stopnia 3.

'''
Wzór newtona można sobie wyobrazić jako stopniowe przekształcenie prostokątu w kwadrat.
To znaczy zaczynamy od prostokątu:
            b=S
    ----------------------
    |                    | a=1
    ----------------------

gdzie początkowe b jest równe S, gdzie S to nasza liczba do spierwiastkowania.

Stopniowo przekształcamy prostokąt w kwadrat, robiąc to w ten sposób żeby pole tych figur cały czas było te samo
ale boki coraz bardziej do siebie podobne, w ten sposób ostatecznie bo nieskończonej ilości kroków
dostaniemy kwadrat o boku a którego pole jest równe a^2=b*1 ==> a^2=S*1 ===> a^2=S, co jest podręcznikową definicją pierwiastka.

Wzór newtona na pierwiastek kwadratowy:
a(n) = (S/a(n-1)+a(n-1))/2 - co jakby sie zastanowić jest dokładnie tym samym opisanym na górze

Teraz musimy ten wzór przekształcić tak żeby otrzymać pierwiastek 3 stopnia. Czyli oczywiście nasuwa nam sie na myśl
prostopadłościan o jednej z krawędzi równej S, pozostałych dwóch równych 1 który chcemy zamienić w sześcian o tej samej objętości.
'''

def pierwiastek3(S, przyblizenie):
    a=S
    while True:
        an=(S/(a*a)+2*a)/3 # odsyłam do https://www.algorytm.edu.pl/algorytmy-maturalne/newton-raphson.html jeśli ktoś dalej nie rozumie
        if abs(a-an)<przyblizenie:
            break
        a=an
        print(a)

pierwiastek3(27, 1e-10)