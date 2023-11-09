a = int(input("Nhập số a: "))
b = int(input("Nhập số b: "))
def tim_bcnn(a, b):
    ucln = 1
    def uscln(x, y):
        while y:
            x, y = y, x % y
        return x

    if a != 0 and b != 0:
        ucln = uscln(a, b)
    bcnn = abs(a * b) // ucln
    return bcnn
ket_qua = tim_bcnn(a, b)
print(f"Bội chung lớn nhất của {a} và {b} là: {ket_qua}")
