# Danh sách các đỉnh đã thăm
visited = []
# Khởi tạo hàng đợi
queue = []


# Hàm BFS (Tìm kiếm theo chiều rộng)
def bfs(visited, graph, node):
    visited.append(node)
    queue.append(node)

    while queue:  # Lặp qua từng đỉnh trong hàng đợi
        m = queue.pop(0)
        print(m, end=" ")

        for neighbour in graph[m]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)

    if len(visited) == len(graph):
        print("\nĐồ thị liên thông")
    else:
        print("\nĐồ thị không liên thông")


# Hàm nhập liệu từ người dùng để tạo đồ thị
def create_graph():
    graph = {}
    n = int(input("Nhập số lượng đỉnh trong đồ thị: "))

    for i in range(n):
        node = input(f"Nhập tên đỉnh thứ {i + 1}: ")
        neighbours = input(f"Nhập các đỉnh kề với đỉnh {node}, cách nhau bởi dấu cách: ").split()
        graph[node] = neighbours

    return graph


# Nhập đồ thị từ người dùng
graph = create_graph()
visited = []  # Reset lại danh sách đã thăm
bfs(visited, graph, list(graph.keys())[0])  # Gọi hàm BFS từ đỉnh đầu tiên

print("\n-------------------------")

