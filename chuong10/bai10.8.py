from datetime import datetime
day = int(input("Nhập ngày: "))
month = int(input("Nhập tháng: "))
year = int(input("Nhập năm: "))
ngay_thang_nam=datetime(year, month, day)
dmy=ngay_thang_nam.strftime("%d - %m - %y")
print("Ngày Tháng năm vừa nhập: ", dmy)
import calendar
if calendar.isleap(year) ==True:
    print("năm", year, "là năm thuận")
else:
    print("năm", year, "không phải là năm thuận")
if calendar.weekday(year,month,day)==0:
    print(dmy, "là Thứ Hai")
if calendar.weekday(year,month,day)==1:
    print(dmy, "là Thứ Ba")
if calendar.weekday(year,month,day)==2:
    print(dmy, "là Thứ Tư")
if calendar.weekday(year,month,day)==3:
    print(dmy, "là Thứ Năm")
if calendar.weekday(year,month,day)==4:
    print(dmy, "là Thứ Sáu")
if calendar.weekday(year,month,day)==5:
    print(dmy, "là Thứ Bảy")
if calendar.weekday(year,month,day)==6:
    print(dmy, "là Chủ Nhật")
def days_in_month(month, year):
    days_count = calendar.monthrange(year, month)[1]
    return days_count
days_count = days_in_month(month, year)
if isinstance(days_count, str):
    print(days_count)
else:
    print(f"Tháng {month} có {days_count} ngày.")