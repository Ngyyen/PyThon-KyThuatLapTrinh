# Muc 5.1.3

def Fibonancci(n) :
    if n == 0 :
        return 0
    if n == 1 :
        return 1
    return Fibonancci(n - 1) + Fibonancci(n - 2)

