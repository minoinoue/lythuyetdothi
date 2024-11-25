# Hàm chuyển ma trận kề thành danh sách kề
def chuyen_matran_ke_sang_danhsach_ke(matran_ke):
    n = len(matran_ke)  # Số đỉnh trong đồ thị
    danhsach_ke = [[] for _ in range(n)]  # Khởi tạo danh sách kề rỗng cho mỗi đỉnh

    # Duyệt qua ma trận kề để xây dựng danh sách kề
    for i in range(n):
        for j in range(n):
            if matran_ke[i][j] == 1:  # Nếu có cạnh từ đỉnh i đến đỉnh j
                danhsach_ke[i].append(j + 1)  # Lưu đỉnh j vào danh sách kề của đỉnh i (chuyển sang đếm từ 1)
    
    return danhsach_ke

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

# Chuyển ma trận kề sang danh sách kề
danhsach_ke = chuyen_matran_ke_sang_danhsach_ke(matran_ke)

# In kết quả
print("Danh sách kề:")
for i in range(len(danhsach_ke)):
    print(f"Đỉnh {i+1}: {danhsach_ke[i]}")
