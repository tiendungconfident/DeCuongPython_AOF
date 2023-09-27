#10. Hiển thị danh sách các hóa đơn có thành tiền x trđ bán trong tháng y và z(1-9)
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
            x = int(input("Nhập thành tiền x: "))
            if x <= 0:
                print("Bạn phải nhập số dương. Vui lòng nhập lại!")
                continue
        except ValueError:
            print("Lỗi: Đây không phải là một số hợp lệ. Vui lòng nhập lại.")
            continue
        break
    while True:
        try:
            y = int(input("Nhập tháng y: "))
            if y < 1 or y > 12:
                print("Vui lòng nhập lại tháng y!")
                continue
        except ValueError:
            print("Lỗi: Đây không phải là một số hợp lệ. Vui lòng nhập lại.")
            continue
        break
    while True:
        try:
            z = int(input("Nhập tháng z (1-9): "))
            if z <= 0 or z >= 10:
                print("Vui lòng nhập lại tháng z!")
                continue
        except ValueError:
            print("Lỗi: Đây không phải là một số hợp lệ. Vui lòng nhập lại.")
            continue
        break

    write_log(f"[{timestamp}]: Danh sách các hóa đơn có thành tiền {x} bán trong tháng {y} và {z}:")
    found = False
    for i in content.split("\n"):
        if i!= "":
            if int(i.split(",")[-1]) == x and (int(i.split(",")[4]) == y  or int(i.split(",")[4]) == z):
                print(i)
                write_log(i)
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