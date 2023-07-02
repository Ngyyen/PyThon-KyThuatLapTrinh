def Nhap() :
    list1 = []
    list2 = []
    n1 = int(input("Nhap so luong phan tu trong danh sach thu 1: "))
    n2 = int(input("Nhap so luong phan tu trong danh sach thu 2: "))
    print("Nhap cac muc trong danh sach thu 1: ")
    for i in range(1, n1 + 1) :
        muc = str(input())
        list1.append(muc)
    print("Nhap cac muc trong danh sach thu 2: ")
    for i in range(1, n2 + 1) :
        muc = str(input())
        list2.append(muc)
    return list1, list2

def KiemTraMucBiTrung(list1, list2) :
    listMucTrung = []
    for muc1 in list1 :
        for muc2 in list2 :
            if muc1 == muc2 :
                listMucTrung.append(muc1)
    if len(listMucTrung) == 0 :
        return "Hai danh sach khong co muc bi trung"
    return "Cac muc bi trung: ", listMucTrung

list1, list2 = Nhap()
print(KiemTraMucBiTrung(list1, list2))