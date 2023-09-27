#30. Tra cứu thông tin của 1 hóa đơn theo số hóa đơn
from datetime import datetime
timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def write_log(message):
    f = open("BanHang.txt", mode="a", encoding="UTF-8")
    f.write(f"{message}\n")
    f.close()

f = open("DuLieuMayGiat.txt", mode="r",encoding="utf-8")
content = f.read()
f.close()

while True:
    while True:
        try:
            so_hd = int(input("Nhập Số hóa đơn: "))
            if so_hd <= 0:
                print("Vui lòng nhập lại Số hóa đơn > 0.")
                continue
        except:
            print("Giá trị nhập sai kiểu dữ liệu!")
            continue
        break

    write_log(f"[{timestamp}]: Tra cứu thông tin của 1 hóa đơn theo số hóa đơn {so_hd}:")
    for i in content.split("\n"):
        if i!= "":
            if int(i.split(",")[1]) == so_hd:
                write_log(f"STT: {i.split(',')[0]}")
                write_log(f"Số hóa đơn: {i.split(',')[1]}")
                write_log(f"Tên máy giặt: {i.split(',')[2]}")
                write_log(f"Ngày bán: {i.split(',')[3]}")
                write_log(f"Tháng bán: {i.split(',')[4]}")
                write_log(f"Số lượng: {i.split(',')[5]}")
                write_log(f"Đơn giá: {i.split(',')[6]}")
                write_log(f"Thành tiền: {i.split(',')[-1]}")

    tiep_tuc = input("Bạn có muốn tiếp tục? (y/n): ")
    while tiep_tuc.lower() not in ['y', 'n']:
        tiep_tuc = input("Lựa chọn không hợp lệ. Bạn có muốn tiếp tục? (y/n): ")
    if tiep_tuc.lower() == 'n':
        break