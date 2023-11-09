Python 3.12.0 (tags/v3.12.0:0fb18b0, Oct  2 2023, 13:03:39) [MSC v.1935 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #Gom cac loai tien: 500000, 200000, 100000, 50000
>>> tien_muon_doi = 1375000
>>> so_to_1 = tien_muon_doi//500000
>>> tien_con_lai = tien_muon_doi%500000
>>> so_to_2 = tien_con_lai//200000
>>> tien_con_lai = tien_con_lai%200000
>>> so_to_3 = tien_con_lai//100000
>>> tien_con_lai = tien_con_lai%100000
>>> so_to_4 = tien_con_lai//50000
>>> tien_con_lai = tien_con_lai%50000
>>> print(so_to_1,so_to_2,so_to_3,so_to_4,tien_con_lai)
2 1 1 1 25000
>>> print('so to 1 la',so_to_1,'so to 2 la',so_to_2,'so to 3 la',so_to_3,'so to 4 la',so_to_4,'so tien con lai la',tien_con_lai)
so to 1 la 2 so to 2 la 1 so to 3 la 1 so to 4 la 1 so tien con lai la 25000
>>> print('so to 1 la',so_to_1,'va','so to 2 la',so_to_2,'va','so to 3 la',so_to_3,'va','so to 4 la',so_to_4,'va','so tien con lai la',tien_con_lai)
so to 1 la 2 va so to 2 la 1 va so to 3 la 1 va so to 4 la 1 va so tien con lai la 25000
