# Hàm chuyển danh sách kề thành ma trận kề
def chuyen_danhsach_ke_sang_matran_ke(danhsach_ke, n):
    # Khởi tạo ma trận kề với tất cả các giá trị là 0
    matran_ke = [[0] * n for _ in range(n)]
    
    # Duyệt qua danh sách kề để cập nhật ma trận kề
    for i in range(n):
        for j in danhsach_ke[i]:  # Danh sách kề của đỉnh i
            matran_ke[i][j - 1] = 1  # Cập nhật ma trận kề, chuyển j sang chỉ số từ 0 (vì danh sách kề dùng chỉ số bắt đầu từ 1)

    return matran_ke

# Hàm nhập danh sách kề từ bàn phím
def nhap_danhsach_ke():
    n = int(input("Nhập số lượng đỉnh của đồ thị: "))  # Nhập số lượng đỉnh
    danhsach_ke = []
    
    print("Nhập danh sách kề:")
    for i in range(n):
        canh = list(map(int, input(f"Nhập các đỉnh kề với đỉnh {i+1}: ").split()))  # Nhập danh sách kề của đỉnh i
        danhsach_ke.append(canh)

    return danhsach_ke

# Nhập danh sách kề từ bàn phím
danhsach_ke = nhap_danhsach_ke()

# Tính toán số đỉnh của đồ thị
n = len(danhsach_ke)

# Chuyển danh sách kề sang ma trận kề
matran_ke = chuyen_danhsach_ke_sang_matran_ke(danhsach_ke, n)

# In kết quả
print("Ma trận kề:")
for row in matran_ke:
    print(" ".join(map(str, row)))
