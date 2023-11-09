so_luong = int(input("Nhập số lượng phần tử của dãy số: "))
def dao_nguoc_va_hien_so_le(n):
    if n < 1:
        print("Vui lòng nhập một số nguyên dương.")
        return
    day_so = list(range(1, n + 1))
    day_so_dao_nguoc = list(reversed(day_so))
    day_so_le = [x for x in day_so_dao_nguoc if x % 2 != 0]
    print(f"Dãy số ban đầu: {day_so}")
    print(f"Dãy số đảo ngược và chỉ hiện số lẻ: {day_so_le}")