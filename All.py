import glob
from operator import itemgetter

import networkx as nx

import GlobVars

graph_helper = dict()
G = nx.DiGraph()
candidates = []
final_summary_sentences = []

def read_input_datafiles():
    path = "C:\\Users\\kriti\\OneDrive\\Documents\\3-2\\Project\\Dataset"
    files = glob.glob(path)
    lines_list = []  # do I need list of list?
    for file in files:
        f = open(file, 'r')
        lines_list += f.readlines()
        f.close()
    return lines_list


def opinosis_graph(lines_list):
    no_sentences = lines_list.__len__()
    for i in range(no_sentences):
        word_list = lines_list[i].split()  # for  the current sentence only
        for i in range(word_list.__len__()):
            print(word_list[i])
        sentence_size = word_list.__len__()
        for j in range(sentence_size):
            LABEL = word_list[j]
            PID = j  #zero based indexing
            SID = i
            print(LABEL, SID, PID)
            if LABEL in graph_helper.keys():
                graph_helper[LABEL].append((SID, PID))
            else:
                graph_helper[LABEL] = [(SID, PID)]
                G.add_node(LABEL)
                if j > 0:  # not first word of sentence  i.e. PID>0
                    G.add_edge(word_list[j - 1], LABEL)  # directed edge


def VSN(node_v):
    avg = 0
    list_of_vals = graph_helper[node_v]
    list_of_vals = sorted(list_of_vals, key=itemgetter(1))
    for i in range(len(list_of_vals)):
        avg += list_of_vals[i][1]
    avg /= len(list_of_vals)
    if avg <= GlobVars.VSN_PARA:  # why underlined?
        return 1
    return 0


def PRI_calc(LABEL):
    return 0


def VEN(LABEL):
    if LABEL in [".", ",", "but", "and", "yet"]:
        return 1
    return 0


def ValidSentence(sentence):
    return 0


def pathScore(redundancy, pathLen):
    return 0

def traverse(cList, node_v, score, PRI_overlap, sentence, pathLen):
    redundancy = len(graph_helper[node_v])
    if redundancy >= GlobVars.REDUNDANCY_PARA:
        if (VEN(node_v)):
            if ValidSentence(sentence):
                final_score = score / pathLen
                cList.append((sentence, final_score))  # check appending tupple in list
    for vn in G.neighbors(node_v):  #check if directed children only
        PRI_new = PRI_overlap + PRI_calc(vn)
        # figure out PRI
        newSent = sentence + " " + node_v
        newPathLen = pathLen + 1
        newScore = score + pathScore(redundancy, newPathLen)




def eliminate_duplicates(candidates):
    return candidates


def Sort_by_path_score(candidates):
    return sorted(candidates, key=itemgetter(1))


def next_best_sentence(candidates):
    # delete that sencence from pool
    return candidates


def opinosisSummarization():
    # node_size=G.number_of_nodes()
    node_size = len(graph_helper)
    all_keys = graph_helper.keys()
    for node_v in all_keys:
        if (VSN(node_v) == 1):
            pathLen = 1
            score = 0
            cList = []
            traverse(cList, node_v, score, graph_helper[node_v], node_v, pathLen)
            candidates.extend(cList)  # not append
    candidates1 = eliminate_duplicates(candidates)
    candidates2 = Sort_by_path_score(candidates1)
    for i in range(GlobVars.SUMMARY_SIZE_PARA):
        final_summary_sentences.extend(next_best_sentence(candidates2))


def main():
    lines_list = read_input_datafiles()
    opinosis_graph(lines_list)
    opinosisSummarization()
    # print(G.nodes.data())
    # print(list(G.nodes))
