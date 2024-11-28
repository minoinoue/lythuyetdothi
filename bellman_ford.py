import sys

INF = 10**18
MaxN = 102

def Bellman_Ford(n, s, edges):
    dist = [INF] * (n + 1)
    mark = [0] * (n + 1)
    dist[s] = 0
    
    for i in range(1, n + 1):
        for u, v, weight in edges:
            if dist[u] + weight < dist[v]:
                if i == n:  # Tại lần cập nhật thứ n, nếu đỉnh vẫn được cập nhật, đánh dấu chu trình âm
                    mark[v] = 1
                dist[v] = dist[u] + weight

    print(f"\nKhoảng cách từ đỉnh {s} đến tất cả các đỉnh còn lại:")
    for i in range(1, n + 1):
        if mark[i] == 0:
            if dist[i] == INF:
                print(f"Đỉnh {i}:-1 (không thể đến được)")  # Không thể tiếp cận được đỉnh này
            else:
                print(f"Đỉnh {i}: {dist[i]}")  # In khoảng cách ngắn nhất
        else:
            print(f"Đỉnh {i}:-1 (thuộc chu trình âm)")  # Đỉnh thuộc chu trình âm

n, m, s = map(int, input("Nhập vào số đỉnh (n), số cạnh (m) và đỉnh bắt đầu (s): ").split())

edges = []
    
for i in range(m):
    u, v, weight = map(int, input(f"Nhập cạnh thứ {i+1} với (u, v, trọng số): ").split())
    edges.append((u, v, weight))
    
Bellman_Ford(n, s, edges)
