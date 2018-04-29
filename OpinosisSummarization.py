import os
import re
from operator import itemgetter

import networkx as nx
import pylab as plt
from numpy import random

import GlobVars
import PruneSimilarSentences

graph_helper = dict()
G = nx.DiGraph()
flag = 0


def create_graph(lines_list, file):
    global G
    global graph_helper
    no_sentences = lines_list.__len__()
    for i in range(no_sentences):
        # text = nltk.word_tokenize("Wow, what a beautiful day.")
        # print(nltk.pos_tag(text))
        # word_list = lines_list[i].split()  # for  the current sentence only
        word_list = re.findall(r"[\w']+|[.,!?;]", lines_list[i])  # Separates punctuations from words
        sentence_size = word_list.__len__()
        for j in range(sentence_size):
            label = word_list[j].lower()
            pid = j  # zero based indexing
            sid = i  # Positional Reference Information(PRI) is (SID, PID)
            # print(label, sid, pid)
            if label in graph_helper.keys():  # if node exits in dictionary, just append
                graph_helper[label].append((sid, pid))
            else:  # create node in graph and key in dictionary
                graph_helper[label] = [(sid, pid)]
                G.add_node(label)
            if j > 0:  # not first word of sentence  i.e. pid>0
                if word_list[j - 1] != label:  # Removes self loops
                    G.add_edge(word_list[j - 1], label)  # directed edge from previous to current word
    nx.draw(G, with_labels=True)
    # print("no of selfloops  " + str(nx.number_of_selfloops(G))) # Output=0
    plt.savefig('opinosis_graph_' + str(file) + '.png')


def vsn(node_v):
    avg = 0  # Average value of pid in all sentences the word occurred in
    list_of_values = graph_helper[node_v]
    # list_of_values = sorted(list_of_values, key=itemgetter(1))  # needed? Sorting on PID?
    for i in range(len(list_of_values)):
        avg += list_of_values[i][1]
    avg /= len(list_of_values)
    # print("avg vsn= " + str(avg) + "  len(list_of_values)= " + str(len(list_of_values)) + "  " + node_v)
    if avg <= 5:  # Suggested=2.
        return 1
    return 0


def pri_calc(curr_word, prev_word):
    count = 0
    for i in range(len(graph_helper[curr_word])):
        for j in range(len(graph_helper[prev_word])):
            if graph_helper[curr_word][i][0] != graph_helper[prev_word][j][0]:  # check
                if abs(graph_helper[curr_word][i][1] - graph_helper[prev_word][j][1]) <= GlobVars.REDUNDANCY_PARA:
                    count += 1
    return count


def ven(label):
    if label in [".", "!", "?"]:  # [".", ",", "but", "and", "yet", "or", "so", "!", "?"]:
        return 1
    return 0


def check_valid_sentence(sentence):
    return 1


def path_score(redundancy, path_len):
    # improve
    return redundancy / path_len


def traverse(c_list, node_v, score, pri_overlap, sentence, path_len, path):
    global flag
    global G
    global graph_helper
    if flag != 0:  # Don't have to traverse that nodes children, return
        return

    redundancy = len(graph_helper[node_v])  # wrong. only for first
    if redundancy >= GlobVars.REDUNDANCY_PARA:
        if ven(node_v):
            # print(sentence + "  " + str(score))
            if check_valid_sentence(sentence) == 1:
                if path_len == 0:
                    flag = 2
                    return
                final_score = score / path_len
                c_list.append((sentence, final_score))
                flag = 1
                return

    for vn in G.neighbors(node_v):  # check if directed children only
        if vn not in path:
            new_path_len = path_len + 1
            if new_path_len > 10:
                flag = 2
                return
            pri_new = pri_overlap + graph_helper[vn]  # should append this nodes PRI to sentence PRI
            if vn not in path:
                path.append(vn)
            new_sentence = sentence + " " + vn
            new_score = score + path_score(redundancy, new_path_len)
            traverse(c_list, vn, new_score, pri_new, new_sentence, new_path_len, path)


def sort_by_path_score(candidates):
    return sorted(candidates, key=itemgetter(1), reverse=True)


def create_summary():
    global flag
    global G
    global graph_helper
    all_keys = graph_helper.keys()
    candidates = []
    final_summary_sentences = ''
    ind = 0
    for node_v in all_keys:
        if vsn(node_v) == 1:
            path_len = 1
            score = 0
            c_list = []
            path = []
            traverse(c_list, node_v, score, graph_helper[node_v], node_v, path_len, path)
            # if flag == 0:
            candidates.extend(c_list)  # not append
            # print(node_v, ind)
            ind += 1
            flag = 0
    # print("candidates len=" + str(candidates.__len__()))
    # for i in range(candidates.__len__()):
    #     print(candidates[i])
    candidates1 = PruneSimilarSentences.symmetric_sentence_similarity(candidates)
    # print("candidates post pruning len=" + str(candidates1.__len__()))
    # for i in range(candidates1.__len__()):
    #     print(candidates1[i])
    candidates2 = sort_by_path_score(candidates1)
    candidates4 = []
    candidates3 = []
    for i in range(candidates2.__len__()):
        candidates3.append(candidates2[i][0])

    if len(candidates2) >= 12:
        for i in range(12):
            candidates4.append(candidates2[i][0])
        candidates2 = random.choice(candidates4, 4)
    else:
        for i in range(candidates2.__len__()):
            candidates3[i] = candidates2[i][0]
        candidates2 = candidates3

    for i in range(min(GlobVars.SUMMARY_SIZE_PARA, candidates2.__len__())):
        final_summary_sentences += candidates2[i]
    return final_summary_sentences


def main():
    path = "C:\\Users\\kriti\\Documents\\Project\\Abstractive_Summarization\\Dataset"
    path2 = "C:\\Users\\kriti\\Documents\\Project\\Abstractive_Summarization\\Output"
    files = os.listdir(path)
    global G
    global graph_helper
    for file in files:
        f = open(path + "\\" + file, 'r')
        lines_list = f.readlines()
        f.close()
        create_graph(lines_list, file)
        final_summary = create_summary()  # print on file save it
        f = open(path2 + "\\" + file + ".txt", 'w')
        f.write(final_summary)
        f.close()
        print("Finished summarizing file " + file)
        graph_helper.clear()
        G.clear()


if __name__ == "__main__":
    main()
