import csv
def ghi_so_dien_thoai_vao_tap_tin(ten_tap_tin, danh_sach_so_dien_thoai):
    try:
        with open(ten_tap_tin, 'a', newline='') as file:
            writer = csv.writer(file)
            for so_dien_thoai in danh_sach_so_dien_thoai:
                writer.writerow([so_dien_thoai])
            print(f"Đã ghi số điện thoại vào cuối tập tin '{ten_tap_tin}' thành công.")
    except FileNotFoundError:
        print(f"Tập tin '{ten_tap_tin}' không tồn tại.")
    except PermissionError:
        print(f"Không có quyền ghi vào tập tin '{ten_tap_tin}'.")
    except Exception as e:
        print(f"Lỗi không xác định: {str(e)}")

ten_tap_tin_csv = 'file.csv'
so_dien_thoai_moi = ['0913 756352', '0989 753951', '0903 123456']
ghi_so_dien_thoai_vao_tap_tin(ten_tap_tin_csv, so_dien_thoai_moi)