from datetime import datetime

def write_dulieu(Mode, message):
    f = open("DuLieuMayGiat.txt", mode=Mode, encoding="UTF-8")
    f.write(f"{message}\n")
    f.close()

def write_log(Mode, message):
    f = open("BanHang.txt", mode=Mode, encoding="UTF-8")
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    f.write(f"[{timestamp}]: {message}\n")
    f.close()

while True:
    while True:
        try:
            k = int(input("Số lượng hóa đơn bán máy giặt: "))
            if k <= 0:
                print("Giá trị nhập phải > 0. Hãy nhập lại!")
                continue
        except ValueError:
            print("Giá trị nhập sai kiểu dữ liệu!")
            continue
        break

    for i in range(k):
        while True:
            try:
                stt = int(input(f"Nhập STT ({i+1}): "))
                if stt <= 0:
                    print("Vui lòng nhập lại STT > 0.")
                    continue
            except:
                print("Giá trị nhập sai kiểu dữ liệu!")
                continue
            break

        while True:
            try:
                so_hd = int(input(f"Nhập Số hóa đơn ({i+1}): "))
                if so_hd <= 0:
                    print("Vui lòng nhập lại Số hóa đơn > 0.")
                    continue
            except:
                print("Giá trị nhập sai kiểu dữ liệu!")
                continue
            break

        while True:
            ten = input(f"Nhập tên máy giặt ({i+1}): ")
            if not ten.isalpha():
                print("Vui lòng nhập lại. Tên máy giặt chỉ chứa ký tự chữ cái")
                continue
            break
    
        while True:
            try:
                ngay_ban = int(input(f"Nhập Ngày bán ({i+1}): "))
                if ngay_ban < 1 or ngay_ban > 31:
                    print("Vui lòng nhập lại ngày bán.")
                    continue
            except:
                print("Giá trị nhập sai kiểu dữ liệu!")
                continue
            break

        while True:
            try:
                thang_ban = int(input(f"Nhập Tháng bán ({i+1}): "))
                if thang_ban < 1 or thang_ban > 12:
                    print("Vui lòng nhập lại tháng bán.")
                    continue
            except:
                print("Giá trị nhập sai kiểu dữ liệu!")
                continue
            break

        while True:
            try:
                so_luong = int(input(f"Nhập Số lượng ({i+1}): "))
                if so_luong <= 0:
                    print("Vui lòng nhập lại Số lượng > 0.")
                    continue
            except:
                print("Giá trị nhập sai kiểu dữ liệu!")
                continue
            break

        while True:
            try:
                don_gia = int(input(f"Nhập Đơn giá ({i+1}): "))
                if don_gia <= 0:
                    print("Vui lòng nhập lại Đơn giá > 0.")
                    continue
            except:
                print("Giá trị nhập sai kiểu dữ liệu!")
                continue
            break
    
        write_dulieu("a",str(stt)+","+str(so_hd)+","+ten+","+str(ngay_ban)+","+str(thang_ban)+","+str(so_luong)+","+str(don_gia))
        write_log("a",f"{str(stt)},{str(so_hd)},{ten},{str(ngay_ban)},{str(thang_ban)},{str(so_luong)},{str(don_gia)}")
    
    tiep_tuc = input("Bạn có muốn tiếp tục? (y/n): ")
    while tiep_tuc.lower() not in ['y', 'n']:
        tiep_tuc = input("Lựa chọn không hợp lệ. Bạn có muốn tiếp tục? (y/n): ")
    if tiep_tuc.lower() == 'n':
        break