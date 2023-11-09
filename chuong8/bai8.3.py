a = float(input("Nhập hệ số a: "))
b = float(input("Nhập hệ số b: "))

# Kiểm tra nếu a = 0, phương trình không còn là phương trình bậc nhất
if a == 0:
    if b == 0:
        print("Phương trình có vô số nghiệm.")
    else:
        print("Phương trình vô nghiệm.")
else:
    # Giải phương trình bậc nhất
    x = -b / a
    print(f"Nghiệm của phương trình là x = {x}")