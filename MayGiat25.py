#25. Xác định số hóa đơn và tên máy giặt có thành tiền lớn nhất
from datetime import datetime
timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def write_log(message):
    f = open("BanHang.txt", mode="a", encoding="UTF-8")
    f.write(f"{message}\n")
    f.close()

write_log(f"[{timestamp}]: Số hóa đơn và tên máy giặt có thành tiền lớn nhất:")

f = open("DuLieuMayGiat.txt", mode="r",encoding="utf-8")
content = f.read()
f.close()

max_tt = max(int(i.split(",")[-1]) for i in content.split("\n") if i)
for i in content.split("\n"):
    if i != "":
        if int(i.split(",")[-1]) == max_tt:
            print(i.split(",")[1],",", i.split(",")[2])
            write_log(f"{i.split(',')[1]},{i.split(',')[2]}")