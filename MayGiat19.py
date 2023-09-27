#19. Hiển thị các hóa đơn có trùng tên máy giặt trong t2 và t4
from datetime import datetime
timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def write_log(message):
    f = open("BanHang.txt", mode="a", encoding="UTF-8")
    f.write(f"{message}\n")
    f.close()

write_log(f"[{timestamp}]: Các hóa đơn có trùng tên máy giặt trong T2 và T4:")

f = open("DuLieuMayGiat.txt", mode="r",encoding="utf-8")
content = f.read()
f.close()

list_t2 = []
list_t4 = []
for i in content.split("\n"):
    if i != "":
        if int(i.split(",")[4]) == 2:
            list_t2.append(i.split(",")[2])
        if int(i.split(",")[4]) == 4:
            list_t4.append(i.split(",")[2])

found = False
for i in content.split("\n"):
    if i != "":
        if int(i.split(",")[4]) in [2,4] and i.split(",")[2] in list(set(list_t2) & set(list_t4)):
            print(i)
            write_log(i)
            found = True
if not found:
    kq = "Không có hóa đơn nào thỏa mãn"
    print(kq)
    write_log(kq)