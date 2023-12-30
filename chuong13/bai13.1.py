def mo_doc_tap_tin(ten_tap_tin):
    try:
        with open(ten_tap_tin, 'r') as file:
            du_lieu = file.read()
            return du_lieu
    except FileNotFoundError:
        return f"Tập tin '{ten_tap_tin}' không tồn tại."
    except PermissionError:
        return f"Không có quyền truy cập tập tin '{ten_tap_tin}'."
    except Exception as e:
        return f"Lỗi không xác định: {str(e)}"
    
ten_tap_tin = 'ten_tap_tin.txt'
noi_dung = mo_doc_tap_tin(ten_tap_tin)
print(noi_dung)

