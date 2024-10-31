'''
Zadanie 50. Pewnych liczb nie można przedstawić jako sumy elementów spójnych fragmentów ciągu
Fibonacciego, np. 9, 14, 15, 17, 22. Proszę napisać program, który wczytuje liczbę naturalną n, wylicza i
wypisuje następną taką liczbę większą od n. Można założyć, że 0 < n < 1000.
'''

def sum_fib(n):
    s = 1
    a=b=1
    test = set() # test
    wieksza = n+1
    while a<100:
        #print(s, a)
        a1=a
        b1=b
        s1=s
        c=a+b
        a=b
        b=c
        s += a
        while s1>1:
            s1=s1-a1
            test.add(s-s1) # test
            if s-s1==wieksza:
                wieksza += 1
            c1=b1-a1
            b1=a1
            a1=c1
            #print("\t",s1, a1)
    print(set(range(100))-test) # test
    print(wieksza)
sum_fib(30)