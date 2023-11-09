so_dem=int(input("nhập số đêm:"))
while True:
  loai_phong = int(input("Nhập mã phòng từ 1 đến 8: "))
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