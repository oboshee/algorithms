import random
from collections import Counter

random.seed(42)          # для воспроизводимости результата

M0 = 3                   # стартовая полная сеть
N = 1000                 # сколько узлов добавляем
M = 2                    # связей у каждого нового узла

edges = []
for i in range(M0):
    for j in range(i + 1, M0):
        edges.append((i, j))

repeated = []
for u, v in edges:
    repeated += [u, v]

for new in range(M0, M0 + N):
    targets = set()
    while len(targets) < M:
        targets.add(random.choice(repeated))
    for t in targets:
        edges.append((new, t))
        repeated += [new, t]

degree = Counter()
for u, v in edges:
    degree[u] += 1
    degree[v] += 1

if __name__ == "__main__":
    print("Узлов:", len(degree), "| рёбер:", len(edges))
    print("Топ-5 хабов (узел: степень):")
    for node, d in degree.most_common(5):
        print(f"  узел {node}: {d}")

    print("Средняя степень:", round(2 * len(edges) / len(degree), 2))
    print("Минимальная степень:", min(degree.values()))