# Muc 6.5.5.1

def TongChan(n) :
    s = 0
    for i in range(2, 2 * n + 1, 2) :
        s += i
    return s