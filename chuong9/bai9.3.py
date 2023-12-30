import math
def tinh_bmi(can_nang,chieu_cao):
    bmi = can_nang/math.pow(chieu_cao,2)
    print("chi so BMI cua ban la %0.2f"%bmi)
    if bmi<18.5:
        print("kết quả đánh giá của bạn là gầy")
    if bmi>=25:
        print("kết quả đánh giá của bạn là thừa cân")
    else:
        print("kết quả đánh giá của bạn là binh thuong")
    
bmi=tinh_bmi(70,1.7)
