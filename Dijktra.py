class DoThi:
    def __init__(self, kich_thuoc):
        # Khởi tạo ma trận kề với kích thước cho trước
        self.ma_tran_ke = [[0] * kich_thuoc for _ in range(kich_thuoc)]
        self.kich_thuoc = kich_thuoc
        self.du_lieu_dinh = [''] * kich_thuoc

    def them_canh(self, u, v, trong_so):
        if 0 <= u < self.kich_thuoc and 0 <= v < self.kich_thuoc:
            self.ma_tran_ke[u][v] = trong_so
            self.ma_tran_ke[v][u] = trong_so  # Đồ thị vô hướng

    def them_du_lieu_dinh(self, dinh, du_lieu):
        if 0 <= dinh < self.kich_thuoc:
            self.du_lieu_dinh[dinh] = du_lieu

    def dijkstra(self, du_lieu_dinh_bat_dau):
        dinh_bat_dau = self.du_lieu_dinh.index(du_lieu_dinh_bat_dau)
        khoang_cach = [float('inf')] * self.kich_thuoc
        khoang_cach[dinh_bat_dau] = 0
        da_duyet = [False] * self.kich_thuoc

        for _ in range(self.kich_thuoc):
            khoang_cach_min = float('inf')
            u = None
            for i in range(self.kich_thuoc):
                if not da_duyet[i] and khoang_cach[i] < khoang_cach_min:
                    khoang_cach_min = khoang_cach[i]
                    u = i

            if u is None:
                break

            da_duyet[u] = True

            for v in range(self.kich_thuoc):
                if self.ma_tran_ke[u][v] != 0 and not da_duyet[v]:
                    alt = khoang_cach[u] + self.ma_tran_ke[u][v]
                    if alt < khoang_cach[v]:
                        khoang_cach[v] = alt

        return khoang_cach

# Tạo đồ thị với 7 đỉnh
do_thi = DoThi(7)

# Thêm dữ liệu cho các đỉnh
do_thi.them_du_lieu_dinh(0, 'A')
do_thi.them_du_lieu_dinh(1, 'B')
do_thi.them_du_lieu_dinh(2, 'C')
do_thi.them_du_lieu_dinh(3, 'D')
do_thi.them_du_lieu_dinh(4, 'E')
do_thi.them_du_lieu_dinh(5, 'F')
do_thi.them_du_lieu_dinh(6, 'G')

# Thêm các cạnh và trọng số
do_thi.them_canh(3, 0, 4)  # D - A, trọng số 4
do_thi.them_canh(3, 4, 2)  # D - E, trọng số 2
do_thi.them_canh(0, 2, 3)  # A - C, trọng số 3
do_thi.them_canh(0, 4, 4)  # A - E, trọng số 4
do_thi.them_canh(4, 2, 4)  # E - C, trọng số 4
do_thi.them_canh(4, 6, 5)  # E - G, trọng số 5
do_thi.them_canh(2, 5, 5)  # C - F, trọng số 5
do_thi.them_canh(2, 1, 2)  # C - B, trọng số 2
do_thi.them_canh(1, 5, 2)  # B - F, trọng số 2
do_thi.them_canh(6, 5, 5)  # G - F, trọng số 5

# Chạy thuật toán Dijkstra từ đỉnh D đến tất cả các đỉnh
print("\nThuật toán Dijkstra bắt đầu từ đỉnh D:")
khoang_cach = do_thi.dijkstra('D')
for i, d in enumerate(khoang_cach):
    print(f"Khoảng cách từ D đến {do_thi.du_lieu_dinh[i]}: {d}")
