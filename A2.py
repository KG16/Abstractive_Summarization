import A1.py

graph_helper = A1.graph_helper
G = A1.G


def VSN(j):
    return 0


# node_size=G.number_of_nodes()
node_size = len(graph_helper)

for j in range(node_size):
    if (VSN(j) == 1):
