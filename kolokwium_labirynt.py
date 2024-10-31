'''
Zadanie 2A, 2024-01-04
Ogród składa sie z 𝑁^2
 jednakowych kwadratowych działek. Posiada on dwa wejścia, jedno w lewym
górnym rogu od strony północnej, drugie w prawym dolnym rogu od strony południowej. Dokładnie
na środkach niektórych działek ustawiono obustronne lustra pod katem 45° albo 135° tak, że patrzący
przez wejście północne widzi osobę stojącą przy wejściu południowym.

'''

'''
Do ogrodu przyszedł zły człowiek i przekręcił dwa lustra, każde o 90°. Proszę napisać funkcję
napraw(ogrod) poprawiającą położenie luster, tak aby przywrócić widoczność pomiędzy oboma
wejściami. Ogród jest reprezentowany jako dwuwymiarowa tablica wypełniona spacjami. Lustra
reprezentowane sa odpowiednio jako znaki: / i \.
'''

from time import sleep
import curses

window = curses.initscr()


def promien_swiatla(lustro, kierunek):
    if lustro==2:
        match kierunek:
            case 2:
                return 1
            case 1:
                return 2
            case 3:
                return 4
            case 4:
                return 3
    if lustro == 1:
        match kierunek:
            case 2:
                return 3
            case 1:
                return 4
            case 3:
                return 2
            case 4:
                return 1

def krok(miejsce, kierunek):
    match kierunek:
        case 2:
            return [miejsce[0], miejsce[1]-1]
        case 1:
            return [miejsce[0]-1, miejsce[1]]
        case 3:
            return [miejsce[0]+1, miejsce[1]]
        case 4:
            return [miejsce[0], miejsce[1]+1]

zmien_znak = {1: "🟦", 2: "🟪", 0: "🟧"}
def print_labirynt(labirynt, miejsce):
    result = ""

    for i in range(len(labirynt)):
        result += "".join(list(map(lambda n: zmien_znak[n[1]] if miejsce != [n[0],i] else "🟩", enumerate(labirynt[i])))) + "\n"
    window.clear()
    window.addstr(0, 0, result)
    sleep(0.4)
    window.refresh()

def labirynt():
    przyklad = [
        [0,0,0,0,0],
        [0,2,0,2,0],
        [0,0,0,0,0],
        [2,0,0,2,0],
        [0,2,0,0,2]
    ]
    miejsce = [4,4]
    kierunek = 2 # 1-lewo, 2-gora, 3-prawo, 4,dol
    poprzedni_punkt = miejsce # w sensie poprzednie lustro od ktorego szlismy
    poprzedni_kierunek = 2 # poprzedni kierunek zanim lustro nas zwiodło i trafiliśmy w ściane ogrodu
    while miejsce != [0,0]:
        print_labirynt(przyklad, miejsce)

        if przyklad[miejsce[1]][miejsce[0]] in [1,2]:
            poprzedni_punkt = miejsce
            poprzedni_kierunek = kierunek
            kierunek = promien_swiatla(przyklad[miejsce[1]][miejsce[0]], kierunek)
        # print(miejsce,kierunek)
        miejsce = krok(miejsce, kierunek)
        if miejsce[0] not in list(range(0,len(przyklad))):
            miejsce = poprzedni_punkt
            kierunek = poprzedni_kierunek
            przyklad[miejsce[1]][miejsce[0]] = 1 if przyklad[miejsce[1]][miejsce[0]] == 2 else 1
        if miejsce[1] not in list(range(0,len(przyklad))):
            miejsce = poprzedni_punkt
            kierunek = poprzedni_kierunek
            przyklad[miejsce[1]][miejsce[0]] = 1 if przyklad[miejsce[1]][miejsce[0]] == 2 else 1
    print_labirynt(przyklad, miejsce)
    miejsce = [0,0]
    sleep(3)
labirynt()