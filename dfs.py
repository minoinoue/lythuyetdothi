# Hàm nhập đồ thị từ người dùng
def create_graph():
    graph = {}
    n = int(input("Nhập số lượng đỉnh trong đồ thị: "))

    for i in range(n):
        node = input(f"Nhập tên đỉnh thứ {i + 1}: ")
        neighbours = input(f"Nhập các đỉnh kề với đỉnh {node}, cách nhau bởi dấu cách: ").split()
        graph[node] = neighbours

    return graph


# Hàm kiểm tra tính liên thông của đồ thị
def check_connected(graph, visited):
    # Nếu số đỉnh đã thăm bằng tổng số đỉnh trong đồ thị thì đồ thị liên thông
    if len(visited) == len(graph):
        print("\nĐồ thị liên thông")
    else:
        print("\nĐồ thị không liên thông")


# Hàm DFS (Tìm kiếm theo chiều sâu)
def dfs(visited, graph, node):  # Hàm DFS
    if node not in visited:
        print(node, end=" ")  # In đỉnh hiện tại trên cùng một dòng
        visited.add(node)  # Đánh dấu đỉnh là đã thăm
        for neighbour in graph[node]:  # Đệ quy thăm các đỉnh kề
            dfs(visited, graph, neighbour)


# Code chính
print("Nhập đồ thị để thực hiện tìm kiếm theo chiều sâu (DFS):")
graph = create_graph()  # Nhập đồ thị từ người dùng
visited = set()  # Tập hợp các đỉnh đã thăm
print("\nĐang thực hiện Tìm kiếm theo chiều sâu (DFS):")
dfs(visited, graph, list(graph.keys())[0])  # Bắt đầu DFS từ đỉnh đầu tiên
check_connected(graph, visited)  # Kiểm tra tính liên thông của đồ thị
