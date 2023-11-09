a = int(input("Nhập số thứ nhất: "))
b = int(input("Nhập số thứ hai: "))
max_so = max(a, b)
boi_chung = max_so
while True:
    if boi_chung % a == 0 and boi_chung % b == 0:
        break
    boi_chung += max_so
print(f"Bội chung nhỏ nhất của {a} và {b} là: {boi_chung}")
