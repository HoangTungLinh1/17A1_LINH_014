list=[]
new_num = float(input("Nhập giá trị: "))
list.append(new_num) 
while True:
    try:
        num=float(input("Tiếp tục nhập giá trị? 1: Có, 0: Không "))
        if num==0:
            break
        elif num == 1:
            new_num = float(input("nhập giá trị: "))
            list.append(new_num)
        else:
            print("nhập không hợp lệ. 1: Có, 0: Không")
    except ValueError:
        print("vui lòng nhập số hợp lệ")
print("List: ", list)
tong=sum(list)
print("Tổng các giá trị trong list:", tong)
x= float(input("nhập số x: "))
print(x, "xuât hiện", list.count(x), "lần trong list")
if x> max(list):
    print(x, "lớn hơn tất cả các số trong list")
else:
    new_list=[element for element in list if element > x]
    print("các số lớn hơn", x, "trong list:",new_list)