﻿# Mục 3.3.4

def countDivisors_4(n) :
    minprime = []
    for p in range(0, n + 1) :
        minprime.append(p)  
    p = 2
    while p * p <= n:
        if minprime[p] == p:
            for i in range(p * p, n + 1, p):
                if(minprime[i] != i) :
                    minprime[i] = p
        p += 1

    T = 1
    while n > 1 : 
        minp = minprime[n]
        count = 0
        while n % minp == 0 : 
            count += 1
            n = n / minp
        T = T * (count + 1)
    return T


