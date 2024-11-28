import sys
import heapq

# Đặt giá trị vô cùng lớn cho khoảng cách
INF = 10**18
MaxN = 101

# Nhập số lượng đỉnh, cạnh và điểm xuất phát
n, m, s = map(int, input("Nhập số đỉnh, số cạnh, điểm xuất phát: ").split())

# Khởi tạo danh sách kề và mảng khoảng cách
dsc = [[] for _ in range(MaxN)]  # Danh sách kề
khoang_cach = [INF] * MaxN      # Mảng khoảng cách
danh_dau = [False] * MaxN       # Mảng đánh dấu

# Đọc các cạnh
for i in range(m):
    u, v, w = map(int, input(f"Nhập cạnh thứ {i+1} theo dạng u v w (với u và v là đỉnh, w là trọng số): ").split())
    dsc[u].append((v, w))

# Hàm Dijkstra để tìm khoảng cách từ điểm xuất phát
def Dijkstra(s):
    khoang_cach[s] = 0
    pq = []
    heapq.heappush(pq, (0, s))

    while pq:
        d, v = heapq.heappop(pq)
        
        if danh_dau[v]:
            continue
        danh_dau[v] = True
        
        for u, w in dsc[v]:
            if not danh_dau[u] and khoang_cach[u] > khoang_cach[v] + w:
                khoang_cach[u] = khoang_cach[v] + w
                heapq.heappush(pq, (khoang_cach[u], u))

# Chạy thuật toán Dijkstra từ nút s
Dijkstra(s)

# Xuất kết quả
print("\nKhoảng cách từ đỉnh", s, "đến tất cả các đỉnh còn lại:")
for i in range(1, n + 1):
    if khoang_cach[i] == INF:
        print(f"Đỉnh {i}: -1 (không thể đến được)")
    else:
        print(f"Đỉnh {i}: {khoang_cach[i]}")

