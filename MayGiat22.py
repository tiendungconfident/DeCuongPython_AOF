"""22. Hiển thị danh sách tên các máy giặt đã bán trong T2
mà không bán trong tháng 1"""
from datetime import datetime

def write_log(message):
    f = open("BanHang.txt", mode="a", encoding="UTF-8")
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    f.write(f"[{timestamp}]: {message}\n")
    f.close()

f = open("DuLieuMayGiat.txt", mode="r",encoding="utf-8")
content = f.read()
f.close()

list_t1 = []
list_t2 = []
for i in content.split("\n"):
    if i != "":
        if int(i.split(",")[4]) == 1:
            list_t1.append(i.split(",")[2])
        if int(i.split(",")[4]) == 2:
            list_t2.append(i.split(",")[2])

print(f"Tên các máy giặt đã bán trong tháng 2/2023 mà không bán trong tháng 1/2023: {list(set(list_t2) - set(list_t1))}")
write_log(f"Tên các máy giặt đã bán trong tháng 2/2023 mà không bán trong tháng 1/2023: {list(set(list_t2) - set(list_t1))}")