from collections import deque
graph = {
    1: [2, 3],
    2: [1, 4, 5],
    3: [1, 6, 7],
    4: [2, 8],
    5: [2, 8],
    6: [3, 9],
    7: [3, 9],
    8: [4, 5, 10],
    9: [6, 7, 10],
    10: [8, 9],
}

def dfs(graph, vertex, visited=None, order=None):
    if visited is None:
        visited, order = set(), []
    visited.add(vertex)
    order.append(vertex)
    for nb in graph[vertex]:
        if nb not in visited:
            dfs(graph, nb, visited, order)
    return order

def bfs(graph, start):
    visited = {start}
    queue = deque([start])
    order = []
    while queue:
        v = queue.popleft()
        order.append(v)
        for nb in graph[v]:
            if nb not in visited:
                visited.add(nb)
                queue.append(nb)
    return order

if __name__ == "__main__":
    dfs_order = dfs(graph, 1)
    bfs_order = bfs(graph, 1)
    print("DFS:", dfs_order, "- вершин:", len(dfs_order))
    print("BFS:", bfs_order, "- вершин:", len(bfs_order))