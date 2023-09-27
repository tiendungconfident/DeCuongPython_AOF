"""14. Hiển thị danh sách các hóa đơn có tên máy giặt x và có số lượng bán từ y trở lên
gồm các thông tin: Số hóa đơn, tên mặt giặt và số lượng"""
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
        x = input("Nhập tên máy giặt: ")
        if not x.isalpha():
            print("Bạn chỉ được nhập ký tự chữ cái. Vui lòng nhập lại!")
            continue
        break

    while True:
        try:
            y = int(input("Nhập số lượng: "))
            if y < 0:
                print("Bạn không được nhập số âm. Vui lòng nhập lại!")
                continue
        except ValueError:
            print("Lỗi: Đây không phải là một số hợp lệ. Vui lòng nhập lại.")
            continue
        break

    write_log(f"[{timestamp}]: Danh sách các hóa đơn có tên máy giặt {x} và SL bán từ {y}:")
    found = False
    for i in content.split("\n"):
        if i!= "":
            if i.split(",")[2] == x and int(i.split(",")[5]) >= y:
                print(i.split(",")[1],",", i.split(",")[2],",", i.split(",")[5])
                write_log(f"{i.split(',')[1]},{i.split(',')[2]},{i.split(',')[5]}")
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