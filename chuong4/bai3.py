m = int(input("Nhập số tự nhiên m: "))
n = int(input("Nhập số tự nhiên n (n lớn hơn m): "))
if m >= n:
    print("nhập lại m sao cho m < n.")
else:
    print("Các số chia hết cho {m} trong khoảng từ 1 đến {n}:")
    for i in range(1, n + 1):
        if i % m == 0:
            print(i)