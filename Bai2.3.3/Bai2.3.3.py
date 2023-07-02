# Muc 2.3.3

import math

def ktNguyenTo(n) :
    if n <= 1 :
        return False
    for i in range(2, math.sqrt(n) + 1) :
        if n % i == 0 :
            return False
    return True
