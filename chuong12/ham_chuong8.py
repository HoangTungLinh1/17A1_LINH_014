import math
def tinh_A(x,n):
    A=(x*x+x+1)**n+(x*x-x+1)**n

def kiem_tra_so_nguyen_to(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def tong_n_so_nguyen(N):
    tong = 0
    for i in range(N):
        so_nguyen = int(input(f"Nhập số nguyên thứ {i + 1}: "))
        tong += so_nguyen

def tong_cac_so_nguyen_nhap_vao(so_nguyen):
    tong = 0
    while True:
        if so_nguyen == 0:
            break
        tong += so_nguyen

def ucln(a,b):
    q=a/b
    r=a%b
    if r==0:
        uscln=b
    else:
        uscln=b
    ket_qua = uscln

def tim_bcnn(a, b):
    ucln = 1
    def uscln(x, y):
        while y:
            x, y = y, x % y
        return x

    if a != 0 and b != 0:
        ucln = uscln(a, b)
    bcnn = abs(a * b) // ucln
    return bcnn

def kiem_tra_so_hoan_hao(n):
    tong_uoc = 0
    for i in range(1, n):
        if n % i == 0:
            tong_uoc += i
    return tong_uoc == n

def dao_nguoc_va_hien_so_le(n):
    if n < 1:
        print("Vui lòng nhập một số nguyên dương.")
        return
    day_so = list(range(1, n + 1))
    day_so_dao_nguoc = list(reversed(day_so))
    day_so_le = [x for x in day_so_dao_nguoc if x % 2 != 0]
    print(f"Dãy số ban đầu: {day_so}")
    print(f"Dãy số đảo ngược và chỉ hiện số lẻ: {day_so_le}")

def tinh_gia_tri_e_mu_x(x, sai_so):
    n = 1
    ket_qua_truoc = 0
    ket_qua_hien_tai = 1 + x

    while abs(ket_qua_hien_tai - ket_qua_truoc) >= sai_so:
        ket_qua_truoc = ket_qua_hien_tai
        ket_qua_hien_tai += (x ** 2) / n
        n += 1

    return ket_qua_hien_tai

def tim_so_lon_nhat_va_so_nho_nhat(danhSachSo):
    so_lon_nhat = danhSachSo[0]
    so_nho_nhat = danhSachSo[0]
    for so in danhSachSo:
        if so > so_lon_nhat:
            so_lon_nhat = so
        elif so < so_nho_nhat:
            so_nho_nhat = so
    return so_lon_nhat, so_nho_nhat

def tim_gia_tri_tuyet_doi(x):
    if x>0:
        print("|",x,"|")
    else:
        s=x*(-1)
        print("|",s,"|")

def giai_pt_bac_nhat(a,b):
    if a == 0:
        if b == 0:
            print("Phương trình có vô số nghiệm.")
        else:
            print("Phương trình vô nghiệm.")
    else:
        x = -b / a
        print(f"Nghiệm của phương trình là x = {x}")    

def tinh_dien_tich_tam_giac(a,b,c):
    p=(a+b+c)/2
    dien_tich=math.sqrt(p*(p-a)*(p-b)*(p-c))
    print("Diện tích của tam giác là:", dien_tich)

def kiem_tar_nam_nhuan(nam):
    if (nam % 4 == 0 and nam % 100 != 0) or (nam % 400 == 0):
        print(f"{nam} là năm nhuận.")
    else:
        print(f"{nam} không phải là năm nhuận.")    

def tinh_cuoc_taxi(so_km,thoi_gian_cho,loai_xe):
    while True:
      
      if loai_xe == 4 or loai_xe==7:
            break
      print("Số nhập không hợp lệ. Vui lòng nhập lại!")
    if thoi_gian_cho <= 5:
        tien_cho=0
    else:
        tien_cho=thoi_gian_cho*800

    if loai_xe==7:
        if so_km>=31:
           tien_di_chuyen=13000*0.8+30*14100+(so_km-30)*12000
        else:
           tien_di_chuyen=13000*0,8+so_km*14100
        tien_cuoc=tien_cho+tien_di_chuyen

    elif loai_xe==4:
        if so_km>=21:
           tien_di_chuyen=11000*0.8+20*12100+(so_km-20)*10000
        else :
           tien_di_chuyen=11000*0,8+so_km*12100
        tien_cuoc =tien_cho+tien_di_chuyen 
    print("tiền chờ:", tien_cho)
    print("tiền di chuyển:", tien_di_chuyen)
    print("tiền cước:", tien_cuoc)

def tinh_tien_dien(so_dien):
    if so_dien >=401:
        tien_dien=50*1.678+50*1.734+100*2.014+2.536+100*2.834+(so_dien-400)*2.927
    elif so_dien>=301:
        tien_dien=50*1.678+50*1.734+100*2.014+2.536+(so_dien-300)*2.834
    elif so_dien>=201:
        tien_dien=50*1.678+50*1.734+100*2.014+(so_dien-200)*2.536
    elif so_dien>=101:
        tien_dien=50*1.678+50*1.734+(so_dien-100)*2.014
    elif so_dien>=51:
        tien_dien=50*1.678+(so_dien-51)*1.734
    else:
        tien_dien=so_dien*1678
    print(tien_dien)

def tinh_tien_thue_phong(so_dem,loai_phong):
    while True:
  
        if 1 <= loai_phong <= 8:
            break
        print("Số nhập không hợp lệ. Vui lòng nhập lại!")
    if loai_phong==1:
        if so_dem==1:
           so_tien=1260000
        elif so_dem>=2 and so_dem<=3:
            so_tien=945000*so_dem
        elif so_dem>=4:
            so_tien=882000*so_dem
    elif loai_phong==2:
        if so_dem==1:
            so_tien=1550000
        elif so_dem>=2 and so_dem<=3:
            so_tien=1162500*so_dem
        elif so_dem>=4:
            so_tien=1085000*so_dem
    elif loai_phong==3:
        if so_dem==1:
            so_tien=1830000
        elif so_dem>=2 and so_dem<=3:
            so_tien=1372500*so_dem
        elif so_dem>=4:
            so_tien=1281000*so_dem
    elif loai_phong==4:
        if so_dem==1:
            so_tien=1830000
        elif so_dem>=2 and so_dem<=3:
            so_tien=1372500*so_dem
        elif so_dem>=4:
            so_tien=1281000*so_dem
    elif loai_phong==5:
        if so_dem==1:
            so_tien=2120000
        elif so_dem>=2 and so_dem<=3:
            so_tien=1590000*so_dem
        elif so_dem>=4:
            so_tien=1484000*so_dem
    elif loai_phong==6:
        if so_dem==1:
            so_tien=2120000
        elif so_dem>=2 and so_dem<=3:
            so_tien=1590000*so_dem
        elif so_dem>=4:
            so_tien=1484000*so_dem
    elif loai_phong==7:
        if so_dem==1:
            so_tien=2540000
        elif so_dem>=2 and so_dem<=3:
            so_tien=1905000*so_dem
        elif so_dem>=4:
            so_tien=1778000*so_dem
    elif loai_phong==8:
        if so_dem==1:
            so_tien=4800000
        elif so_dem>=2 and so_dem<=3:
            so_tien=3600000*so_dem
        elif so_dem>=4:
            so_tien=3360000*so_dem
    print("số tiền:", so_tien)

def dem_nguoc(thoi_gian):
    while thoi_gian>0:
        print(thoi_gian)
        thoi_gian-=1
    print("Start!!!")

def tinh_bieu_thuc_A(n,x):
    S=(x*x+1)**n
    print(S)