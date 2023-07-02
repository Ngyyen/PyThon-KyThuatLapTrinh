# Muc 1.3.2, Bai tap 6

def toChar(n) :
    Letter = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
    return Letter[n]

def DecimalToHexa(n) :
    temp = ""
    while n > 0 : 
        temp += toChar(n % 16)
        n = int(n / 16)
    return temp

def main() :
    n = int(input("Nhap n (n <= 10^9): "))
    print("Bieu dien so thap phan",n,"co he co so 16 la: ", DecimalToHexa(n))
    print("Ket thuc !!!")

if __name__ == "__main__":
    main()



