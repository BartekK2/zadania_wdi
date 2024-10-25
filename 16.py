#Zadanie 16. 
# Proszę napisać program wyznaczający najmniejszą wspólną wielokrotność 3 zadanych liczb naturalnych.

def nwd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# nww(x,y) to nic innego jak (x*y)/nwd(x,y)
def nww(a, b):
    return (a * b) // nwd(a, b)

def nww_trzech_liczb(x, y, z):
    return nww(nww(x, y), z)

print(nww(3,8))
print(nww_trzech_liczb(3,8,10))