"""17. Có bao nhiêu hóa đơn có thành tiền từ x trở lên đã bán trong tháng y"""
from datetime import datetime

def write_log(message):
    f = open("BanHang.txt", mode="a", encoding="UTF-8")
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    f.write(f"[{timestamp}]: {message}\n")
    f.close()

f = open("DuLieuMayGiat.txt", mode="r",encoding="utf-8")
content = f.read()
f.close()

while True:
    while True:
        try:
            x = int(input("Nhập thành tiền x: "))
            if x < 0:
                print("Bạn không được nhập số âm. Vui lòng nhập lại!")
                continue
        except ValueError:
            print("Lỗi: Đây không phải là một số hợp lệ. Vui lòng nhập lại.")
            continue
        break

    while True:
        try:
            y = int(input("Nhập tháng y: "))
            if y < 1 or y > 12:
                print("Vui lòng nhập lại tháng từ 1-12 !")
                continue
        except ValueError:
            print("Lỗi: Đây không phải là một số hợp lệ. Vui lòng nhập lại.")
            continue
        break

    count = 0
    for i in content.split("\n"):
        if i!= "":
            if int(i.split(",")[-1]) >= x and int(i.split(",")[4]) == y:
                count += 1

    print(f"Số hóa đơn có thành tiền từ {x} trở lên đã bán trong tháng {y}: {count}")
    write_log(f"Số hóa đơn có thành tiền từ {x} trở lên đã bán trong tháng {y}: {count}")

    tiep_tuc = input("Bạn có muốn tiếp tục? (y/n): ")
    while tiep_tuc.lower() not in ['y', 'n']:
        tiep_tuc = input("Lựa chọn không hợp lệ. Bạn có muốn tiếp tục? (y/n): ")
    if tiep_tuc.lower() == 'n':
        break