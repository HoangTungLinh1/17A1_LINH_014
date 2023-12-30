import math
a = float(input("Nhập hệ số a: "))
b = float(input("Nhập hệ số b: "))
c = float(input("Nhập hệ số c: "))
delta=(pow(b,2) - 4*a*c)
if a==0:
    print("x = ", -c/b)
if delta <0:
    print("pt vo nghiem")
elif delta ==0:
    print('pt co nghiem kep')
    print('x = ',b/2*a)
else:
    print("pt co 2 nghiem phan biet")
    print("x1 = ",(-b+ math.sqrt(delta))/(2*a))
    print("x2 = ",(-b- math.sqrt(delta))/(2*a))




