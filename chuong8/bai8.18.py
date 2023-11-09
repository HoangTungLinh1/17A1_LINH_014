so = int(input("Nhập một số: "))
def kiem_tra_so_hoan_hao(n):
    tong_uoc = 0
    for i in range(1, n):
        if n % i == 0:
            tong_uoc += i
    return tong_uoc == n
if kiem_tra_so_hoan_hao(so):
    print(f"{so} là số hoàn hảo.")
else:
    print(f"{so} không phải là số hoàn hảo.")