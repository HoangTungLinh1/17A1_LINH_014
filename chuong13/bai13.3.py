def ghi_noi_dung_vao_tap_tin(ten_tap_tin, noi_dung):
    try:
        with open(ten_tap_tin, 'w') as file:
            file.write(noi_dung)
        print(f"Đã ghi nội dung vào tập tin '{ten_tap_tin}' thành công.")
    except FileNotFoundError:
        print(f"Tập tin '{ten_tap_tin}' không tồn tại.")
    except PermissionError:
        print(f"Không có quyền ghi vào tập tin '{ten_tap_tin}'.")
    except Exception as e:
        print(f"Lỗi không xác định: {str(e)}")

ten_tap_tin = 'ten_tap_tin.txt' 
noi_dung = "Đây là nội dung cần ghi vào tập tin.\nCó thể là nhiều dòng."
ghi_noi_dung_vao_tap_tin(ten_tap_tin, noi_dung)