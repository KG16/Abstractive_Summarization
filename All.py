import networkx as nx

import GlobVars

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


def VSN(j):
    return 0


def PRI_calc(LABEL):
    return 0


def VEN(LABEL):
    return 0


def ValidSentence(sentence):
    return 0


def Neighbours(LABEL):
    return G.neighbors


def traverse(cList, node_v, score, PRI_overlap, sentence, pathLen):
    redundancy = PRI_calc(LABEL)
    if redundancy >= GlobVars.REDUNDANCY_PARA:
        if (VEN(node_v)):
            if ValidSentence(sentence):
                final_score = score / pathLen
                cList.append((sentence, final_score))  # check appending tupple in list
    for vn in Neighbours(LABEL):
        PRI_new = PRI_overlap + PRI_calc(vn)


def OpinosisSummarization():
    # node_size=G.number_of_nodes()
    node_size = len(graph_helper)

    for j in range(node_size):
        if (VSN(j) == 1):
            pathLen = 1
            score = 0
            cList = []
            traverse(cList, LABEL, score, PRI_overlap, LABEL, pathLen)


def main():
    lines_list = read_input_datafiles()
    opinosis_graph(lines_list)
    print(G.nodes.data())
    print(list(G.nodes))
