# Muc 6.1.4

def mulEgypt(a, b) : 
    if b == 0 : 
        return 0
    t = mulEgypt(a, int(b / 2)) 
    if b % 2 != 0 :
        return t + t + a
    return t + t