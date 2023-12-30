def nhap_so_nguyen_duong():
    while True:
        try:
            so = int(input("Nhập một số nguyên dương (nhập 0 để kết thúc): "))
            if so < 0:
                raise ValueError("Lỗi số âm!!!")
            return so
        except ValueError as e:
            print("Lỗi:", e)
        except KeyboardInterrupt:
            raise KeyboardInterrupt
        except:
            print("Lỗi nhập số!!!")

def main():
    so_lan_lap = 0
    so_lan_nhau = 1
    so_truoc = None
    so_chan = 0

    try:
        while True:
            so = nhap_so_nguyen_duong()

            if so == 0:
                break

            if so == so_truoc:
                so_lan_nhau += 1
                if so_lan_nhau == 4:
                    raise ValueError("Lỗi nhập lặp lại!!!")
            else:
                so_lan_nhau = 1

            if so % 2 == 0:
                so_chan += 1
                if so_chan == 5:
                    raise ValueError("Lỗi nhập chẵn!!!")
            else:
                so_chan = 0

            so_truoc = so
            so_lan_lap += 1

    except ValueError as e:
        print("Lỗi:", e)
    except KeyboardInterrupt:
        print("\nNgừng nhập do người dùng yêu cầu.")

    print(f"Số lần nhập: {so_lan_lap}")