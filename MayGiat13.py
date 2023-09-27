"""13. Hiển thị danh sách các hóa đơn có thành tiền dưới 10trđ bán trong T1/2023
và các hóa đơn có thành tiền trên 50trđ bán trong T2/2023"""
from datetime import datetime
timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def write_log(message):
    f = open("BanHang.txt", mode="a", encoding="UTF-8")
    f.write(f"{message}\n")
    f.close()

write_log(f"[{timestamp}]: Các hóa đơn có thành tiền dưới 10 (T1) và trên 50 (T2):")

f = open("DuLieuMayGiat.txt", mode="r",encoding="utf-8")
content = f.read()
f.close()

found = False
for i in content.split("\n"):
    if i != "":
        if (int(i.split(",")[-1]) < 10 and int(i.split(",")[4]) == 1) or (int(i.split(",")[-1]) > 50 and int(i.split(",")[4]) == 2):
            print(i)
            write_log(i)
            found = True
if not found:
    kq = "Không có hóa đơn nào thỏa mãn"
    print(kq)
    write_log(kq)