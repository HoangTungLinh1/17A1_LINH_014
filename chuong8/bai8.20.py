x = float(input("Nhập giá trị x: "))
sai_so = 1e-4
def tinh_gia_tri_e_mu_x(x, sai_so):
    n = 1
    ket_qua_truoc = 0
    ket_qua_hien_tai = 1 + x

    while abs(ket_qua_hien_tai - ket_qua_truoc) >= sai_so:
        ket_qua_truoc = ket_qua_hien_tai
        ket_qua_hien_tai += (x ** 2) / n
        n += 1

    return ket_qua_hien_tai
ket_qua = tinh_gia_tri_e_mu_x(x, sai_so)
print(f"Gần đúng giá trị e^{x} với sai số {sai_so} là: {ket_qua}")