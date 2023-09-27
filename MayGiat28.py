#28. Xác định số hóa đơn và tên máy giặt có thành tiền nhỏ nhất đã bán trong tháng x
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
            x = int(input("Nhập tháng x (1-12): "))
            if x < 1 or x > 12:
                print("Vui lòng nhập lại tháng!")
                continue
        except ValueError:
            print("Lỗi: Đây không phải là một số hợp lệ. Vui lòng nhập lại.")
            continue
        break

    write_log(f"[{timestamp}]: Số hóa đơn và tên máy giặt có thành tiền nhỏ nhất đã bán trong tháng {x}:")
    min_tt = min(int(i.split(",")[-1]) for i in content.split("\n") if i and int(i.split(",")[4]) == x)
    for i in content.split("\n"):
        if i != "":
            if int(i.split(",")[4]) == x and int(i.split(",")[-1]) == min_tt:
                print(i.split(",")[1],",", i.split(",")[2])
                write_log(f"{i.split(',')[1]},{i.split(',')[2]}")
    
    tiep_tuc = input("Bạn có muốn tiếp tục? (y/n): ")
    while tiep_tuc.lower() not in ['y', 'n']:
        tiep_tuc = input("Lựa chọn không hợp lệ. Bạn có muốn tiếp tục? (y/n): ")
    if tiep_tuc.lower() == 'n':
        break