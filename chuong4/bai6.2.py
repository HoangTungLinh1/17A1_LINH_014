thang = int(input("Nhập tháng (1-12): "))
nam = int(input("Nhập năm: "))
if thang < 1 or thang > 12:
    print("Tháng không hợp lệ.")
else:
    if thang in [1, 3, 5, 7, 8, 10, 12]:
        so_ngay = 31
    elif thang in [4, 6, 9, 11]:
        so_ngay = 30
    else:
        if (nam % 4 == 0 and nam % 100 != 0) or (nam % 400 == 0):
            so_ngay = 29
        else:
            so_ngay = 28
    print(f"Số ngày của tháng {thang} năm {nam} là: {so_ngay}")    

  
    
