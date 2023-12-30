import csv
def doc_tap_tin_csv(ten_tap_tin):
    try:
        with open(ten_tap_tin, 'r', newline='') as file:
            doc_csv = csv.reader(file)
            for hang in doc_csv:
                print(hang)  # In từng hàng trong tập tin CSV
    except FileNotFoundError:
        print(f"Tập tin '{ten_tap_tin}' không tồn tại.")
    except PermissionError:
        print(f"Không có quyền truy cập tập tin '{ten_tap_tin}'.")
    except Exception as e:
        print(f"Lỗi không xác định: {str(e)}")

ten_tap_tin_csv = 'file.csv'
doc_tap_tin_csv(ten_tap_tin_csv)