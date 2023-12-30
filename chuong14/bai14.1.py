def kiem_tra_tam_giac(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        return True
    return False
def nhap_canh(prompt):
    while True:
        try:
            giatri = float(input(prompt))
            if giatri <= 0:
                raise ValueError("Độ dài cạnh phải là số dương và lớn hơn 0.")
            return giatri
        except ValueError as e:
            print("Lỗi:", e)
def chinh():
    print("Nhập độ dài ba cạnh của tam giác:")
    while True:
        try:
            a = nhap_canh("Nhập độ dài cạnh a: ")
            b = nhap_canh("Nhập độ dài cạnh b: ")
            c = nhap_canh("Nhập độ dài cạnh c: ")

            if not kiem_tra_tam_giac(a, b, c):
                raise ValueError("Độ dài ba cạnh không thỏa mãn điều kiện tồn tại tam giác.")
            break
        except ValueError as e:
            print("Lỗi:", e)

    print(f"Các cạnh {a}, {b}, {c} tạo thành một tam giác.")           