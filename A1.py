import glob

import networkx as nx

graph_helper = dict()
G = nx.DiGraph()

def read_input_datafiles():
    path = "C:\\Users\\kriti\\OneDrive\\Documents\\3-2\\Project\\Dataset"
    files = glob.glob(path)
    for file in files:
        f = open(file, 'r')
        lines_list = f.readlines()
        f.close()
    return lines_list


def opinosis_graph(lines_list):
    lines_list = read_input_datafiles()
    no_sentences = lines_list.__len__()
    for i in range(no_sentences):
        word_list = lines_list[i].split()  # for  the current sentence only
        for i in range(word_list.__len__()):
            print(word_list[i])
        sentence_size = word_list.__len__()
        for j in range(sentence_size):
            LABEL = word_list[j]
            PID = j
            SID = i
            if LABEL in graph_helper.keys():
                graph_helper[LABEL].append((SID, PID))
            else:
                graph_helper[LABEL] = [(SID, PID)]
                G.add_node(LABEL)
                if j > 0:  # not first word of sentence  i.e. PID>0
                    G.add_edge(LABEL, word_list[j - 1])

def main():
    lines_list = read_input_datafiles()
    opinosis_graph(lines_list)
    print(G.nodes.data())
    print(list(G.nodes))
