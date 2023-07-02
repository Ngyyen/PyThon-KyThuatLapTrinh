# Muc 3.5.2

import math

def uscln_2(a, b) :
    a = abs(a)
    b = abs(b)
    while a != 0 and b != 0 :
        if a > b :
            a = a % b
        else : 
            b = b % a
    return a + b

