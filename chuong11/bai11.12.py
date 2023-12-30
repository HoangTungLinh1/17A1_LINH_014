tuple_a=()
bon_so_dau= 4
for i in range(bon_so_dau):
    so=input(f"Nhập phần tử thứ {i+1}:")
    tuple_a +=(so, )
tuple_b=()
bon_so_cuoi=4
for n in range(bon_so_cuoi):
    phan_tu=input(f"nhập phần tử thứ {n+1}:")
    tuple_b +=(phan_tu, )
print('Tuple a:', tuple_a)
print('Tuple b:', tuple_b)
tuple_c=tuple_a + tuple_b
print("Tuple c:", tuple_c)
new= list(tuple_c)
new.sort()
tuple_d=tuple(new)
print("Tupel d:", tuple_d)
print("3 phần tử cuối cùng của tuple d", tuple_d[5:])