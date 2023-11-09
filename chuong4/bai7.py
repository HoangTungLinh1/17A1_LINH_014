N = int(input("Nhập số nguyên N: "))
def tinh_tong_chu_so(N):
    tong = 0
    while N > 0:
        tong += N % 10
        N //= 10
    return tong
ket_qua = tinh_tong_chu_so(N)
print(f"Tổng các chữ số của {N} là: {ket_qua}")