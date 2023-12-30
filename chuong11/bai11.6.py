list_number_3=[74,74,72,72,73,69,69,71,76,71]
doi_inch_sang_m=[chieu_cao*0.0254 for chieu_cao in list_number_3]
print("3 chieu cao dau tien là:", doi_inch_sang_m[:3])
print("3 chieu cao cuoi cung là:", doi_inch_sang_m[-3:])
doi_inch_sang_m.sort()
print("theo giá trị tăng dần:",doi_inch_sang_m)
doi_inch_sang_m.sort(reverse=True)
print("theo giá trị giảm dần:",doi_inch_sang_m)
