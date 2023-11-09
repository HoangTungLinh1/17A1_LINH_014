N = int(input("Nhập số nguyên N: "))
tong = 0
for i in range(N):
    so_nguyen = int(input(f"Nhập số nguyên thứ {i + 1}: "))
    tong += so_nguyen
print(f"S = {tong}")