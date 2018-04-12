import A3


def VSN(j):
    return 0


def OpinosisSummarization():
    # node_size=G.number_of_nodes()
    node_size = len(graph_helper)

    for j in range(node_size):
        if (VSN(j) == 1):
            pathLen = 1
            score = 0
            cList = []
            A3.Traverse(cList, LABEL, score, PRI_overlap, LABEL, pathLen)
