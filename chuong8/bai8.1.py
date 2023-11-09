def tim_so_lon_nhat_va_so_nho_nhat(danhSachSo):
    so_lon_nhat = danhSachSo[0]
    so_nho_nhat = danhSachSo[0]
    for so in danhSachSo:
        if so > so_lon_nhat:
            so_lon_nhat = so
        elif so < so_nho_nhat:
            so_nho_nhat = so
    return so_lon_nhat, so_nho_nhat
danhSachSo = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
so_lon_nhat, so_nho_nhat = tim_so_lon_nhat_va_so_nho_nhat(danhSachSo)
print(so_lon_nhat, so_nho_nhat)