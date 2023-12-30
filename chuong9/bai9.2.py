def ham_tinh_nam_am_lich_tu_nam_duong_lich(nam):
    can=nam%10
    if can==0:
        can = "Canh"
    if can==1:
        can= "Tan"
    if can==2:
        can="Nham"
    if can==3:
        can="Quy"
    if can==4:
        can="Giap"
    if can==5:
        can="At"
    if can==6:
        can="Binh"
    if can==7:
        can="Dinh"
    if can==8:
        can="Mau"
    if can==9:
        can="Ky"
    chi=nam%12
    if chi==0:
        chi="Than"
    if chi==1:
        chi="Dau"
    if chi==2:
        chi="Tuat"
    if chi==3:
        chi="Hoi"
    if chi==4:
        chi="Ty"
    if chi==5:
        chi="Suu"
    if chi==6:
        chi="Dan"
    if chi==7:
        chi="Mao"
    if chi==8:
        chi="Thin"
    if chi==9:
        chi="Ty"
    if chi==10:
        chi="Ngo"
    if chi==11:
        chi="Mui"
    print("Năm",nam,"lịch âm là",can,chi)

ham_tinh_nam_am_lich_tu_nam_duong_lich(2017)