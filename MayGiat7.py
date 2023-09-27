"""7. Hiển thị danh sách các hóa đơn có thành tiền dưới z triệu đồng gồm các thông tin:
Số hóa đơn, tên máy giặt, thành tiền"""
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
            z = int(input("Nhập thành tiền z: "))
            if z <= 0:
                print("Bạn phải nhập số dương. Vui lòng nhập lại!")
                continue
        except ValueError:
            print("Lỗi: Đây không phải là một số hợp lệ. Vui lòng nhập lại.")
            continue
        break

    write_log(f"[{timestamp}]: Danh sách các hóa đơn có thành tiền dưới {z} triệu đồng")
    found = False
    for i in content.split("\n"):
        if i!= "":
            if int(i.split(",")[-1]) < z:
                print(i.split(",")[1],",", i.split(",")[2],",", i.split(",")[-1])
                write_log(f"{i.split(',')[1]},{i.split(',')[2]},{i.split(',')[-1]}")
                found = True
    if not found:
        kq = "Không có hóa đơn nào thỏa mãn"
        print(kq)
        write_log(kq)

    tiep_tuc = input("Bạn có muốn tiếp tục? (y/n): ")
    while tiep_tuc.lower() not in ['y', 'n']:
        tiep_tuc = input("Lựa chọn không hợp lệ. Bạn có muốn tiếp tục? (y/n): ")
    if tiep_tuc.lower() == 'n':
        break