Tuple=('red', 'green', 'yellow', 'blue', 'black', 'white', 'pink', 'orange', 'red', 'blue')
index_duong= int(input("Nhập số từ 0 đến 9: "))
index_am= int(input("Nhập số từ -1 đến -9: "))
print("Tuple: ",Tuple)
if 0 <= index_duong < 9:
     print(f"Tuple [{index_duong}]= {Tuple[index_duong]}")
else:
    print("Index dương không hợp lệ.")
if -9<=index_am <=-1:
    print(f"Tuple [{index_am}]= {Tuple[index_am]}")
else:
    print("Index dương không hợp lệ.")
s_find = input("Nhập chuỗi cần tìm: ")
count_s_find =Tuple.count(s_find)
print(f"'{s_find}' xuất hiện trong tuple {count_s_find}")