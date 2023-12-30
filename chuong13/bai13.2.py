def thong_ke_dong_tap_tin(ten_tap_tin):
    try:
        with open(ten_tap_tin, 'r') as file:
            so_dong = 0
            so_tu = 0
            so_ky_tu = 0

            for line in file:
                so_dong += 1
                tu = line.split()
                so_tu += len(tu)
                so_ky_tu += len(line)

            return so_dong, so_tu, so_ky_tu
    except FileNotFoundError:
        return None, None, None
    except PermissionError:
        return None, None, None
    except Exception as e:
        print(f"Lỗi không xác định: {str(e)}")
        return None, None, None
    
ten_tap_tin = 'ten_tap_tin.txt' 
so_dong, so_tu, so_ky_tu = thong_ke_dong_tap_tin(ten_tap_tin)
if so_dong is not None:
    print(f"Số dòng: {so_dong}")
    print(f"Số từ: {so_tu}")
    print(f"Số ký tự: {so_ky_tu}")
else:
    print(f"Không thể thống kê tập tin '{ten_tap_tin}'")