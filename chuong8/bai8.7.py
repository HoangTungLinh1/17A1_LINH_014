so_dien=eval(input("nhap so dien"))
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