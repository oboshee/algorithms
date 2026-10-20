from collections import deque

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['E', 'F'],
    'D': ['G'],
    'E': ['G', 'H'],
    'F': ['G'],
    'G': ['H'],
    'H': [],
}

def topological_sort(graph):
    visited, result = set(), []
    def dfs(v):
        visited.add(v)
        for nb in graph.get(v, []):
            if nb not in visited:
                dfs(nb)
        result.append(v)
    for v in graph:
        if v not in visited:
            dfs(v)
    return result[::-1]

def shortest_path(graph, start, goal):
    prev = {start: None}
    queue = deque([start])
    while queue:
        v = queue.popleft()
        if v == goal:
            break
        for nb in graph[v]:
            if nb not in prev:
                prev[nb] = v
                queue.append(nb)
    if goal not in prev:
        return None
    path, cur = [], goal
    while cur is not None:
        path.append(cur)
        cur = prev[cur]
    return path[::-1]

if __name__ == "__main__":
    order = topological_sort(graph)
    print("Топологический порядок:", order)

    pos = {v: i for i, v in enumerate(order)}
    assert all(pos[u] < pos[v] for u in graph for v in graph[u])
    print("Проверка: для всех рёбер u->v позиция u меньше позиции v - OK")

    path = shortest_path(graph, 'A', 'H')
    print("Кратчайший путь A->H:", ' -> '.join(path), "| длина:", len(path) - 1)