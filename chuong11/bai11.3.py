list_animals=['ant','bear','cat','dog','elephat','fish','goat','hippo']
print('List of animals:', list_animals)
so_con_vat=len(list_animals)
print("Number of animals:", so_con_vat)

def tim_con_vat(danh_sach, con_vat_can_tim):
    if con_vat_can_tim in danh_sach:
        print(f"There is {con_vat_can_tim} in list of animals")
    else:
        print("Không tìm thấy con vật trong danh sách.")
con_vat_can_tim = input("I want to find: ")
tim_con_vat(list_animals, con_vat_can_tim)
