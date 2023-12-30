list_number2=[]
new_num = float(input("Nhập giá trị: "))
list_number2.append(new_num) 
while True:
    try:
        num=float(input("Tiếp tục nhập giá trị? 1: Có, 0: Không "))
        if num==0:
            break
        elif num == 1:
            new_num = float(input("nhập giá trị: "))
            list_number2.append(new_num)
        else:
            print("nhập không hợp lệ. 1: Có, 0: Không")
    except ValueError:
        print("vui lòng nhập số hợp lệ")
print("List: ", list_number2)
def la_so_nguyen_to(x):
    if x<=1:
        return False
    for i in range(2,int(x**0.5)+1):
        if x%i==0:
            return False
    return True
so_nguyen_to=[num for num in list_number2 if la_so_nguyen_to(num)]
print("Các số nguyên tố trong list:", so_nguyen_to)
so_am=[num for num in list_number2 if num <0 ]
print("Các phần tử âm trong list:", so_am)
tb_so_am=sum(so_am)/len(so_am)
print("Trung bình cộng các phần tử âm:", tb_so_am)
so_duong=[num for num in list_number2 if num >0 ]
print("Các phần tử dương trong list:", so_duong)
tb_so_duong=sum(so_duong)/len(so_duong)
print("Trung bình cộng các phần tử dương:", tb_so_duong)
max=max(list_number2)
print("Giá trị max trong list", max)
min=min(list_number2)
print("Giá trị min trong list", -4)
list_number2.sort()
print("List sắp tăng dần", list_number2)