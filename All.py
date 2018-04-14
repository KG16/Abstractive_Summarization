import os
from operator import itemgetter

import networkx as nx

import GlobVars

# import pylab as plt
# import nltk
graph_helper = dict()
G = nx.DiGraph()
candidates = []
final_summary_sentences = []


def opinosis_graph(lines_list):
    no_sentences = lines_list.__len__()
    for i in range(no_sentences):
        # text = nltk.word_tokenize("hi, I'm a person called Kriti.")
        # # word_tokenize("And now for something completely different")
        #
        # print(nltk.pos_tag(text))
        word_list = lines_list[i].split()  # for  the current sentence only
        sentence_size = word_list.__len__()
        for j in range(sentence_size):
            label = word_list[j]
            pid = j  # zero based indexing
            sid = i
            print(label, sid, pid)
            if label in graph_helper.keys():
                graph_helper[label].append((sid, pid))
            else:
                graph_helper[label] = [(sid, pid)]
                G.add_node(label)
            if j > 0:  # not first word of sentence  i.e. pid>0
                G.add_edge(word_list[j - 1], label)  # directed edge
    # nx.draw(G, with_labels=True)
    # plt.savefig('labels.png')


def vsn(node_v):
    avg = 0
    list_of_vals = graph_helper[node_v]
    list_of_vals = sorted(list_of_vals, key=itemgetter(1))
    for i in range(len(list_of_vals)):
        avg += list_of_vals[i][1]
    avg /= len(list_of_vals)
    print("avg vsn= " + avg + " " + node_v)
    if avg <= 2:
        return 1
    return 0


def pri_calc(curr_word, prev_word):
    return 0


def ven(label):
    if label in [".", ",", "but", "and", "yet", "or", "so"]:
        return 1
    return 0


def validSentence(sentence):
    return 0


def pathScore(redundancy, path_len):
    return 0


def traverse(c_list, node_v, score, pri_overlap, sentence, path_len):
    redundancy = len(graph_helper[node_v])
    if redundancy >= GlobVars.REDUNDANCY_PARA:
        if (ven(node_v)):
            if validSentence(sentence):
                final_score = score / path_len
                c_list.append((sentence, final_score))  # check appending tupple in list
    for vn in G.neighbors(node_v):  # check if directed children only
        PRI_new = pri_overlap + pri_calc(vn)
        # figure out PRI
        newSent = sentence + " " + vn
        new_path_len = path_len + 1
        newScore = score + pathScore(redundancy, new_path_len)
        # add if collapsible
        traverse(c_list, vn, newScore, PRI_new, newSent, new_path_len)


def eliminate_duplicates(candidates):
    return candidates


def sort_by_path_score(candidates):
    return sorted(candidates, key=itemgetter(1))


def next_best_sentence(candidates):
    # delete that sentence from pool
    return candidates


def opinosis_summarization():
    # node_size=G.number_of_nodes()
    node_size = len(graph_helper)
    all_keys = graph_helper.keys()
    for node_v in all_keys:
        if vsn(node_v) == 1:
            path_len = 1
            score = 0
            c_list = []
            traverse(c_list, node_v, score, graph_helper[node_v], node_v, path_len)
            candidates.extend(c_list)  # not append
    candidates1 = eliminate_duplicates(candidates)
    candidates2 = sort_by_path_score(candidates1)
    for i in range(GlobVars.SUMMARY_SIZE_PARA):
        final_summary_sentences.extend(next_best_sentence(candidates2))


def main():
    path = "C:\\Users\\kriti\\Documents\\Project\\Abstractive_Summarization\\Dataset"
    files = os.listdir(path)
    for file in files:
        f = open(path + "\\" + file, 'r')
        lines_list = f.readlines()
        f.close()
        opinosis_graph(lines_list)
        opinosis_summarization()
