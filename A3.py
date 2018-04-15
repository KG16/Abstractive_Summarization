import os
import re
from operator import itemgetter

import networkx as nx
import pylab as plt

graph_helper = dict()
G = nx.DiGraph()

# text = nltk.word_tokenize("hi, I'm a person called Kriti.")
# print(nltk.pos_tag(text))

def main():
    # print("hi")
    path = "C:\\Users\\kriti\\Documents\\Project\\Abstractive_Summarization\\Dataset"
    files = os.listdir(path)
    lines_list = []
    for file in files:
        f = open(path + "\\" + file, 'r')
        lines_list = f.readlines()
        f.close()
        break
    # print(lines_list)
    no_sentences = lines_list.__len__()
    for i in range(no_sentences):
        word_list = re.findall(r"[\w']+|[.,!?;]", lines_list[i])
        sentence_size = word_list.__len__()
        for j in range(sentence_size):
            LABEL = word_list[j].lower()
            PID = j  # zero based indexing
            SID = i
            # print(LABEL, SID, PID)
            if LABEL in graph_helper.keys():
                graph_helper[LABEL].append((SID, PID))
            else:
                graph_helper[LABEL] = [(SID, PID)]
                G.add_node(LABEL)
            if j > 0:  # not first word of sentence  i.e. PID>0
                G.add_edge(word_list[j - 1], LABEL)  # directed edge
    nx.draw(G, with_labels=True)
    plt.savefig('labels1.png')  # tested
    all_keys = graph_helper.keys()
    # print("Stmt")
    for node_v in all_keys:
        avg = 0
        list_of_vals = graph_helper[node_v]
        list_of_vals = sorted(list_of_vals, key=itemgetter(1))
        for i in range(len(list_of_vals)):
            avg += list_of_vals[i][1]
        avg /= len(list_of_vals)
        print("avg vsn= " + str(avg) + "  len(list_of_values)= " + str(len(list_of_vals)) + "  " + node_v)
        print(nx.number_of_selfloops(G))


if __name__ == "__main__":
    main()
