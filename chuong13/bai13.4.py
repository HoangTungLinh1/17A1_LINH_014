def ghi_noi_dung_vao_tap_tin(ten_tap_tin, noi_dung):
    try:
        with open(ten_tap_tin, 'a') as file:
            file.write('\n' + noi_dung)
            print(f"Đã ghi nội dung vào cuối tập tin '{ten_tap_tin}' thành công.")
    except FileNotFoundError:
        with open(ten_tap_tin, 'w') as file:
            file.write(noi_dung)
            print(f"Đã tạo tập tin '{ten_tap_tin}' và ghi nội dung vào thành công.")
    except PermissionError:
        print(f"Không có quyền ghi vào tập tin '{ten_tap_tin}'.")
    except Exception as e:
        print(f"Lỗi không xác định: {str(e)}")

def main():
    while True:
        ten_tap_tin = input("Nhập tên tập tin: ")
        noi_dung = input("Nhập nội dung: ")

        ghi_noi_dung_vao_tap_tin(ten_tap_tin, noi_dung)

        tiep_tuc = input("Bạn có muốn tiếp tục không? (Chọn 1: có, 0: không): ")
        if tiep_tuc != '1':
            break