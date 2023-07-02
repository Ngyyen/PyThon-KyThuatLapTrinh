# Muc 6.3.4

def LuyThua(x, n) :
    if n == 0 : 
        return 1
    t = LuyThua(x, int(n / 2))
    if n % 2 == 0 :
        return t * t
    return t * t * x

def power(a, b) :
    if b == 0 :
        return 1
    t = power(a, int(b / 2))
    if b % 2 == 0 : 
        return t * t
    return t * t * a