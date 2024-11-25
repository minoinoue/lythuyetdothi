# Hàm chuyển ma trận kề thành danh sách cạnh
def chuyen_matran_ke_sang_danhsach_canh(matran_ke):
    n = len(matran_ke)  # Số đỉnh trong đồ thị
    danhsach_canh = []  # Danh sách cạnh ban đầu là rỗng
    k = 0  # Biến đếm số lượng cạnh

    # Duyệt qua tất cả các cặp (i, j) trong ma trận kề
    for i in range(n):
        for j in range(n):
            if matran_ke[i][j]:  # Nếu có cạnh giữa đỉnh i và đỉnh j
                k += 1
                # Thêm cạnh vào danh sách
                danhsach_canh.append((i + 1, j + 1))  # Lưu ý +1 vì đỉnh trong đồ thị thường bắt đầu từ 1
    
    return danhsach_canh

# Hàm nhập ma trận kề từ bàn phím
def nhap_matran_ke():
    n = int(input("Nhập số lượng đỉnh của đồ thị: "))  # Nhập số lượng đỉnh
    matran_ke = []
    
    print("Nhập ma trận kề:")
    for i in range(n):
        hang = list(map(int, input(f"Nhập hàng {i+1}: ").split()))  # Nhập từng hàng của ma trận
        matran_ke.append(hang)

    return matran_ke

# Nhập ma trận kề từ bàn phím
matran_ke = nhap_matran_ke()

# Chuyển ma trận kề sang danh sách cạnh
danhsach_canh = chuyen_matran_ke_sang_danhsach_canh(matran_ke)

# In kết quả
print("Danh sách cạnh:")
for canh in danhsach_canh:
    print(f"({canh[0]}, {canh[1]})")
