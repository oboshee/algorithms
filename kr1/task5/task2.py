from collections import deque

graph = {
    'A': ['B', 'C'], 'B': ['A', 'C'], 'C': ['A', 'B', 'D'], 'D': ['C'],
    'E': ['F'], 'F': ['E', 'G'], 'G': ['F'],
    'H': [],
    'I': ['J', 'L'], 'J': ['I', 'K'], 'K': ['J', 'L'], 'L': ['I', 'K'],
}

def find_components(graph):
    visited, components = set(), []
    for vertex in graph:
        if vertex not in visited:
            comp, stack = set(), [vertex]
            while stack:
                v = stack.pop()
                if v not in visited:
                    visited.add(v)
                    comp.add(v)
                    for nb in graph[v]:
                        if nb not in visited:
                            stack.append(nb)
            components.append(comp)
    return components

def is_bipartite(graph, start):
    color = {start: 0}
    queue = deque([start])
    while queue:
        v = queue.popleft()
        for nb in graph[v]:
            if nb not in color:
                color[nb] = 1 - color[v]
                queue.append(nb)
            elif color[nb] == color[v]:
                return False, (v, nb)
    return True, color

if __name__ == "__main__":
    components = find_components(graph)
    print("Компоненты связности:")
    for c in components:
        print("  ", sorted(c))

    print("\nПроверка двудольности:")
    for c in components:
        start = sorted(c)[0]
        sub = {v: [u for u in graph[v] if u in c] for v in c}
        ok, res = is_bipartite(sub, start)
        if ok:
            print(f"  {sorted(c)}: двудольная, раскраска {dict(sorted(res.items()))}")
        else:
            print(f"  {sorted(c)}: НЕ двудольная, смежные {res[0]} и {res[1]} получили один цвет (нечётный цикл)")