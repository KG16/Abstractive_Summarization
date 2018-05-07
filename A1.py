import re

import networkx as nx


def create_graph(lines_list, file):
    global G
    global graph_helper
    no_sentences = lines_list.__len__()
    for i in range(no_sentences):
        word_list = re.findall(r"[\w']+|[.,!?;]", lines_list[i])
        sentence_size = word_list.__len__()
        for j in range(sentence_size):
            label = word_list[j].lower()
            pid = j
            sid = i
            if label in graph_helper.keys():
                graph_helper[label].append((sid, pid))
            else:
                graph_helper[label] = [(sid, pid)]
                G.add_node(label)
            if j > 0:
                if word_list[j - 1] != label:
                    G.add_edge(word_list[j - 1], label)
    nx.draw(G, with_labels=True)
