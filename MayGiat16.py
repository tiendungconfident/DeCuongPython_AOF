#16. Có bao nhiêu loại máy giặt có tên khác nhau đã bán trong tháng x
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
            x = int(input("Nhập tháng x (1-12): "))
            if x < 1 or x > 12:
                print("Vui lòng nhập lại tháng!")
                continue
        except ValueError:
            print("Lỗi: Đây không phải là một số hợp lệ. Vui lòng nhập lại.")
            continue
        break

    list_tx = []
    for i in content.split("\n"):
        if i != "":
            if int(i.split(",")[4]) == x:
                list_tx.append(i.split(",")[2])
    
    print(f"Có {len(set(list_tx))} loại máy giặt có tên khác nhau đã bán trong tháng {x}")
    write_log(f"Có {len(set(list_tx))} loại máy giặt có tên khác nhau đã bán trong tháng {x}")

    tiep_tuc = input("Bạn có muốn tiếp tục? (y/n): ")
    while tiep_tuc.lower() not in ['y', 'n']:
        tiep_tuc = input("Lựa chọn không hợp lệ. Bạn có muốn tiếp tục? (y/n): ")
    if tiep_tuc.lower() == 'n':
        break