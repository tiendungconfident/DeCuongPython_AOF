#11. Hiển thị danh sách các hóa đơn có thành tiền từ 12 đến 15 trđ bán trong T4/2023
from datetime import datetime
timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def write_log(message):
    f = open("BanHang.txt", mode="a", encoding="UTF-8")
    f.write(f"{message}\n")
    f.close()

write_log(f"[{timestamp}]: Các hóa đơn có thành tiền từ 12 đến 15 trđ bán trong T4/2023:")

f = open("DuLieuMayGiat.txt", mode="r",encoding="utf-8")
content = f.read()
f.close()

found = False
for i in content.split("\n"):
    if i != "":
        if 12 <= int(i.split(",")[-1]) <= 15 and int(i.split(",")[4]) == 4:
            print(i)
            write_log(i)
            found = True
if not found:
    kq = "Không có hóa đơn nào thỏa mãn"
    print(kq)
    write_log(kq)