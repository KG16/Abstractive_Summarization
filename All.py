import os
import re
from operator import itemgetter

import networkx as nx
# import fuzzywuzzy as fuzz
import pylab as plt

import GlobVars

# import nltk
graph_helper = dict()
G = nx.DiGraph()
candidates = []  # check if needed
final_summary_sentences = []


def opinosis_graph(lines_list):
    no_sentences = lines_list.__len__()
    for i in range(no_sentences):
        # text = nltk.word_tokenize("hi, I'm a person called Kriti.")
        # print(nltk.pos_tag(text))
        # word_list = lines_list[i].split()  # for  the current sentence only
        word_list = re.findall(r"[\w']+|[.,!?;]", lines_list[i])
        sentence_size = word_list.__len__()
        for j in range(sentence_size):
            label = word_list[j].lower()
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
    nx.draw(G, with_labels=True)
    print("no of selfloops  " + str(nx.number_of_selfloops(G)))
    plt.savefig('labels.png')


def vsn(node_v):
    avg = 0
    list_of_values = graph_helper[node_v]
    list_of_values = sorted(list_of_values, key=itemgetter(1))
    for i in range(len(list_of_values)):
        avg += list_of_values[i][1]
    avg /= len(list_of_values)
    print("avg vsn= " + str(avg) + "  len(list_of_values)= " + str(len(list_of_values)) + "  " + node_v)
    if avg <= 2:
        return 1
    return 0


def pri_calc(curr_word, prev_word):
    return 0


def ven(label):
    if label in [".", ",", "but", "and", "yet", "or", "so"]:
        return 1
    return 0


def check_valid_sentence(sentence):

    return 0


def path_score(redundancy, path_len):
    # improve
    return redundancy / path_len


def traverse(c_list, node_v, score, pri_overlap, sentence, path_len):
    redundancy = len(graph_helper[node_v])  #wrong. only for first
    if redundancy >= GlobVars.REDUNDANCY_PARA:
        if ven(node_v):
            if check_valid_sentence(sentence) ==1:
                final_score = score / path_len
                c_list.append((sentence, final_score))  # check appending tuple in list
    for vn in G.neighbors(node_v):  # check if directed children only
        pri_new = pri_overlap + pri_calc(vn, node_v)
        # figure out PRI
        new_sentence = sentence + " " + vn
        new_path_len = path_len + 1
        new_score = score + path_score(redundancy, new_path_len)
        # add if collapsible
        traverse(c_list, vn, new_score, pri_new, new_sentence, new_path_len)


#
def eliminate_duplicates(candidates):
    # for i in range(candidates.__len__()):
    #     for j in (i+1, candidates.__len__()):
    #         if fuzz.ratio>0.5: #(candidates[i],candidates[j])
    #             #calc lower score sent. and remove
    #             candidates.remove(candidates[i])
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
        final_summary_sentences.extend(next_best_sentence(candidates2))  # shorted this part


def main():
    path = "C:\\Users\\kriti\\Documents\\Project\\Abstractive_Summarization\\Dataset"
    files = os.listdir(path)
    for file in files:
        f = open(path + "\\" + file, 'r')
        lines_list = f.readlines()
        f.close()
        opinosis_graph(lines_list)
        opinosis_summarization()
        break


if __name__ == "__main__":
    main()
