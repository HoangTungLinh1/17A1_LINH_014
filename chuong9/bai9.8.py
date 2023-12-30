def ham_kiem_tra_so_hoan_hao(x):
    if x < 0:
        print("x phai la so nguyen duong")
    else:
        if x == 0:
            print("0 khong phai la so hoan hao")
        tong = 0
        for i in range(1, x):
            if x%i==0:
                tong = tong + i
        if tong == x:
            print(f"{x} la so hoan hao")
        else:
            print(f"{x} khong phai so hoan hao")
ham_kiem_tra_so_hoan_hao(28)
