import random
import numpy as np
import matplotlib.pyplot as plt
from sklearn import cluster, datasets


def plot_by_groups(points, labels):
    for i in set(labels):
        cordinate = [point for point, label in zip(points, labels) if label == i]
        group = np.array(cordinate)
        color = 'black' if i == -1 else None
        marker = 'x' if i == -1 else None
        plt.scatter(group[:, 0], group[:, 1], color=color, marker=marker)
    plt.show()


def distance(p, q):
    return np.linalg.norm(p-q)


def find_neighbors(points, eps):
    neighbors = [[] for _ in points]
    for i, p in enumerate(points):
        for j, q in enumerate(points):
            neighbors[i] += [j] if distance(p, q) <= eps else []
    return neighbors

data = np.array([[1, 1], [1, 2], [2, 1], [2, 2], [1.5, 1.5],
                 [6, 1], [6, 2], [7, 1], [7, 2], [6.5, 1.5],
                 [3, 1], [4, 1], [5, 1], [1, 5], [1.5, 4.5]])

N = data.shape[0]
M = 4
EPS = 1.0
print("==========Show Data Point==========")
plot_by_groups(data, np.zeros(N))

guess = -np.ones(N, dtype=np.int64)
neighbors = find_neighbors(data, eps=EPS)
cores = {i for i in range(N) if len(neighbors[i]) >= M}

phase_2 = set(cores)
phase_3 = {i for i in range(N) if i not in cores}
queue = set()
print("==========Show DBSCAN Algorithm Step by Step==========")
for _ in range(12):
    print(f"==========Show DBSCAN on step {_}==========")
    if not phase_2 and not queue:
        print('WARNING: Core clustering process is already stabled!')
        i = None
    else:
        if not queue:
            i = phase_2.pop()
            cluster_number = i
        else:
            i = queue.pop()
            phase_2 -= {i}
        if guess[i] == -1 and len(neighbors[i]) >= M:
            guess[i] = cluster_number
            queue |= {n for n in neighbors[i] if n in cores and guess[n] == -1}
            queue -= {i}
    if i is not None:
        plt.gcf().gca().add_artist(plt.Circle(data[i], EPS, alpha=0.5))
    plot_by_groups(data, guess)
