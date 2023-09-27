"""29. Hiển thị danh sách các hóa đơn có thành tiền lớn hơn 
giá trị tiền trung bình theo từng hóa đơn"""
from datetime import datetime
timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def write_log(message):
    f = open("BanHang.txt", mode="a", encoding="UTF-8")
    f.write(f"{message}\n")
    f.close()

write_log(f"[{timestamp}]: Danh sách các hóa đơn có thành tiền lớn hơn giá trị tiền trung bình theo từng hóa đơn:")

f = open("DuLieuMayGiat.txt", mode="r",encoding="utf-8")
content = f.read()
f.close()

count = 0
total = 0
for i in content.split("\n"):
    if i!= "":
        count += 1
        total += int(i.split(",")[-1])
average_tt = total / count

for i in content.split("\n"):
    if i!= "":
        if int(i.split(",")[-1]) > average_tt:
            print(i)
            write_log(i)