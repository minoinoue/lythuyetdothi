class DoThi:
    def __init__(self, kichThuoc):
        # Khởi tạo ma trận kề với kích thước cho trước
        self.maTranKe = [[0] * kichThuoc for _ in range(kichThuoc)]
        self.kichThuoc = kichThuoc
        self.duLieuDinh = [''] * kichThuoc  # Dữ liệu của các đỉnh

    def themCanh(self, u, v, trongSo):
        # Thêm cạnh có trọng số vào đồ thị
        if 0 <= u < self.kichThuoc and 0 <= v < self.kichThuoc:
            self.maTranKe[u][v] = trongSo
            # self.maTranKe[v][u] = trongSo  # Đối với đồ thị vô hướng

    def themDuLieuDinh(self, dinh, duLieu):
        # Gán dữ liệu cho một đỉnh cụ thể
        if 0 <= dinh < self.kichThuoc:
            self.duLieuDinh[dinh] = duLieu

    def bellman_ford(self, duLieuDinhBatDau):
        # Tìm kiếm khoảng cách từ đỉnh bắt đầu đến các đỉnh khác bằng thuật toán Bellman-Ford
        dinhBatDau = self.duLieuDinh.index(duLieuDinhBatDau)
        khoangCach = [float('inf')] * self.kichThuoc  # Khởi tạo mảng khoảng cách
        khoangCach[dinhBatDau] = 0  # Khoảng cách từ đỉnh bắt đầu đến chính nó là 0

        # Lặp qua các đỉnh để thư giãn các cạnh
        for i in range(self.kichThuoc - 1):
            for u in range(self.kichThuoc):
                for v in range(self.kichThuoc):
                    if self.maTranKe[u][v] != 0:  # Nếu có cạnh giữa u và v
                        if khoangCach[u] + self.maTranKe[u][v] < khoangCach[v]:
                            khoangCach[v] = khoangCach[u] + self.maTranKe[u][v]
                            # In ra quá trình thư giãn cạnh
                            print(f"Thư giãn cạnh {self.duLieuDinh[u]}-{self.duLieuDinh[v]}, Cập nhật khoảng cách đến {self.duLieuDinh[v]}: {khoangCach[v]}")

        return khoangCach

# Khởi tạo đồ thị với 5 đỉnh
g = DoThi(5)

# Thêm dữ liệu cho các đỉnh
g.themDuLieuDinh(0, 'A')
g.themDuLieuDinh(1, 'B')
g.themDuLieuDinh(2, 'C')
g.themDuLieuDinh(3, 'D')
g.themDuLieuDinh(4, 'E')

# Thêm các cạnh với trọng số
g.themCanh(3, 0, 4)  # D -> A, trọng số 4
g.themCanh(3, 2, 7)  # D -> C, trọng số 7
g.themCanh(3, 4, 3)  # D -> E, trọng số 3
g.themCanh(0, 2, 4)  # A -> C, trọng số 4
g.themCanh(2, 0, -3) # C -> A, trọng số -3
g.themCanh(0, 4, 5)  # A -> E, trọng số 5
g.themCanh(4, 2, 3)  # E -> C, trọng số 3
g.themCanh(1, 2, -4) # B -> C, trọng số -4
g.themCanh(4, 1, 2)  # E -> B, trọng số 2

# Chạy thuật toán Bellman-Ford bắt đầu từ đỉnh D
print("\nThuật toán Bellman-Ford bắt đầu từ đỉnh D:")
khoangCach = g.bellman_ford('D')
for i, d in enumerate(khoangCach):
    print(f"Khoảng cách từ D đến {g.duLieuDinh[i]}: {d}")
