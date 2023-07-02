# Muc 7.6

def mulBigNum(x, y) :
    carry = 0
    temp = ""
    for i in range(len(x)-1, -1, -1) :
        xx = int(x[i])
        ss = xx * y + carry
        temp = str(ss % 10) + temp
        carry = int (ss / 10)
    if carry > 0 :
        temp = str(carry) + temp
    return temp

