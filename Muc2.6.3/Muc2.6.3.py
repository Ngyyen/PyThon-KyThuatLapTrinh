# Mục 2.6.3, cải tiến lần 2

def Eratosthenes(n):
    isprime = [True] * (n + 1)
    isprime[0] = False
    isprime[1] = False
    
    p = 2
    while p * p <= n:
        if isprime[p] == True:
            for i in range(2 * p, n + 1, p):
                isprime[i] = False
        p += 1
    
    prime = []
    for p in range(2, n + 1):
        if isprime[p] == True:
            prime.append(p)
    
    return prime

