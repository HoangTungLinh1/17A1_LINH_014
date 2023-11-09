so_km=eval(input("nhập số km"))
thoi_dian_cho=eval(input("nhập số phút"))
while True:
      loai_xe=int(input("nhập loại xe"))
      if loai_xe == 4 or loai_xe==7:
            break
      print("Số nhập không hợp lệ. Vui lòng nhập lại!")
if thoi_dian_cho <= 5:
        tien_cho=0
else:
        tien_cho=thoi_dian_cho*800

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
