import numpy as np
import networkx as nx
import matplotlib
import matplotlib.pyplot as plt

def graph1_adjacency_matrix():
    return np.array([
        [0, 1, 1, 0, 0, 0, 1, 0, ],
        [1, 0, 0, 1, 0, 0, 0, 1, ],
        [1, 0, 0, 1, 1, 0, 0, 0, ],
        [0, 1, 1, 0, 0, 1, 0, 0, ],
        [0, 0, 1, 0, 0, 1, 1, 0, ],
        [0, 0, 0, 1, 1, 0, 0, 1, ],
        [1, 0, 0, 0, 1, 0, 0, 1, ],
        [0, 1, 0, 0, 0, 1, 1, 0, ],
    ])


def build_test_graph1():
    adj_mat = graph1_adjacency_matrix()
    N = len(adj_mat)

    G = nx.Graph()
    for i in range(N):
        G.add_node(str(i))

    for i in range(N):
        for j in range(N):
            if adj_mat[i][j] == 1:
                G.add_edge(str(i), str(j))
    return G


G = build_test_graph1()
print("\n".join(nx.generate_gml(G)))

nx.draw(G)
plt.show()
