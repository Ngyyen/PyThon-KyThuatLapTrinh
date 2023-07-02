
def toChar(n) :
    Letter = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
    return Letter[n]

# Muc 1.3.2

def DecimalToHexa(n) :
    temp = ""
    while n > 0 : 
        temp += toChar(n % 16)
        n = int(n / 16)
    return temp

s = DecimalToHexa(12)
print(s)
