"""3. Bổ sung thêm thông tin thành tiền cho mỗi hóa đơn bán máy giặt trong tập tin text, tính giá trị thành tiền cho mỗi hóa đơn
Biết rằng: Thành tiên = Số lượng x đơn giá"""
from datetime import datetime
timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def write_log(message):
    f = open("BanHang.txt", mode="a", encoding="UTF-8")
    f.write(f"{message}\n")
    f.close()

write_log(f"[{timestamp}]: Bổ sung thêm thông tin thành tiền")

f = open("DuLieuMayGiat.txt", mode="r",encoding="utf-8")
content = f.read()
f.close()

data = [i.strip().split(",") for i in content.split("\n") if i]

for row in data[0:]:
    if len(row) == 7:
        so_luong = int(row[5])
        don_gia = int(row[6])
        thanh_tien = so_luong * don_gia
        row.append(str(thanh_tien))

updated_content = "\n".join([",".join(row) for row in data])
f = open("DuLieuMayGiat.txt", mode="w",encoding="utf-8")
f.write(updated_content)
f.close()