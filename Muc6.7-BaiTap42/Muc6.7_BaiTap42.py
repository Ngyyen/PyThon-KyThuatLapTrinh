# Mục 6.7, Bài tập 42

def Tong(n) :
    s = 1
    for i in range(1, n + 1) :
        if i % 2 != 0 :
            s = s - (3*i-1) + (3*i) - (3*i+1)
        else :
            s = s + (3*i-1) - (3*i) + (3*i+1)
    return s

# Mục 6.7, Bài tập 42, Hàm cài đặt Vicky

def Tong(n) :
    s = 0
    for i in range(1, 3 * n + 2) :
        if i % 2 != 0 :
            s += i
        else :
            s -= i
    return s