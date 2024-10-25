#Zadanie 3.
# Proszę znaleźć wyrazy początkowe ciągu zamiast 1,1 o najmniejszej sumie, aby w ciągu
# analogicznym do ciągu Fibonacciego wystąpił wyraz równy numerowi bieżącego roku.

# Proponowałbym to zrobić w taki sposób że zaczynamy od k-tego wyrazu ciągu fibbonaciego równemu 2024
# a następnie sprawdzamy każdy możliwy (k-1)-ty element przed nim tzn:

def znajdz_poczatek(rok=2024):
    # robimy sobie coś w stylu odwrotnego ciągu fibbonaciego

    # ustawmy sobie na start maksymalną sume elementów taką jaką rok ponieważ 2 poprzednie elementy
    # zsumowane, muszą nam dać trzeci element czyli rok
    min_suma = rok 
    # Na razie puste miejsca na pary takich liczb które dają tą najmniejszą sumę
    min_1 = None
    min_2 = None
    for before in range(0,rok): # dla każdego możliwego (k-1)-tego elementu (przed 2024 - k elementem)
        a=b=before
        c = rok
        while True: 
            a = c-b
            c = b
            b = a # a to wszystko to po prostu to co w zad.2 czyli ciąg fibbonaciego ale tak jakby "od tyłu"
            if a<0 or b<0: #co prawda w zadaniu nie ma powiedziane ze poczatkowe wyrazy mają być dodatnie, ale inaczej zad. nie ma sensu
                break
            elif c+b < min_suma:
                min_suma = c+b
                min_1 = b
                min_2 = c
    print(min_1, min_2)
znajdz_poczatek()

# Metoda pójścia od końca ułatwia nam sprawe, bo wiemy już że napewno 2024 się 
# pojawi w naszym ciągu, co nie jest przecież oczywiste dla każdych dwóch pierwszych elementów