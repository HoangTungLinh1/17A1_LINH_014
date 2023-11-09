so = int(input("Nhập một số: "))
def kiem_tra_so_nguyen_to(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
if kiem_tra_so_nguyen_to(so):
    print(f"{so} là số nguyên tố.")
else:
    print(f"{so} không phải là số nguyên tố.")
