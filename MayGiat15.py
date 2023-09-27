#15. Có bao nhiêu hóa đơn bán trong tháng x năm 2023
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
            x = int(input("Nhập tháng x: "))
            if x < 1 or x > 12:
                print("Bạn phải nhập tháng từ 1-12. Vui lòng nhập lại!")
                continue
        except ValueError:
            print("Lỗi: Đây không phải là một số hợp lệ. Vui lòng nhập lại.")
            continue
        break

    count = 0
    for i in content.split("\n"):
        if i!= "":
            if int(i.split(",")[4]) == x:
                count += 1

    print(f"Số hóa đơn bán trong tháng {x}: {count}")
    write_log(f"Số hóa đơn bán trong tháng {x}: {count}")

    tiep_tuc = input("Bạn có muốn tiếp tục? (y/n): ")
    while tiep_tuc.lower() not in ['y', 'n']:
        tiep_tuc = input("Lựa chọn không hợp lệ. Bạn có muốn tiếp tục? (y/n): ")
    if tiep_tuc.lower() == 'n':
        break