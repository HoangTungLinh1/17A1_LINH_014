def kiem_tra_so_nguyen_to(x):
    if x < 2:
        print("False")
    else:
        for i in range(2,x):
            if x%i == 0:
                print("False")
            break
        else:
            print("True")
kiem_tra_so_nguyen_to(12)