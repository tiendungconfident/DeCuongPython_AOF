#20. Hiển thị các hóa đơn không trùng tên máy giặt trong t1 và t3
from datetime import datetime
timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def write_log(message):
    f = open("BanHang.txt", mode="a", encoding="UTF-8")
    f.write(f"{message}\n")
    f.close()

write_log(f"[{timestamp}]: Các hóa đơn không trùng tên máy giặt trong T1 và T3:")

f = open("DuLieuMayGiat.txt", mode="r",encoding="utf-8")
content = f.read()
f.close()

list_t1 = []
list_t3 = []
for i in content.split("\n"):
    if i != "":
        if int(i.split(",")[4]) == 1:
            list_t1.append(i.split(",")[2])
        if int(i.split(",")[4]) == 3:
            list_t3.append(i.split(",")[2])

found = False
for i in content.split("\n"):
    if i != "":
        if int(i.split(",")[4]) in [1,3] and i.split(",")[2] not in list(set(list_t1) & set(list_t3)):
            print(i)
            write_log(i)
            found = True
if not found:
    kq = "Không có hóa đơn nào thỏa mãn"
    print(kq)
    write_log(kq)