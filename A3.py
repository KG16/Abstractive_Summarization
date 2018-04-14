import os
import re

import networkx as nx
import pylab as plt

graph_helper = dict()
G = nx.DiGraph()
# graph_helper = dict()
# from operator import itemgetter
#
# G = nx.DiGraph()
#
# graph_helper["the"] = [(4, 1)]
# graph_helper["the"].append((2, 7))
# graph_helper["the"].append((3, 5))
# graph_helper["the"].append((1, 2))
# graph_helper["the"].append((4, 5))
# print(graph_helper)
#
# avg = 0
# print(len(graph_helper["the"]))
# # sor=sorted(graph_helper.items(), key=lambda graph_helper: graph_helper[1])
# sor = graph_helper["the"]
# print(sor)
# sor = sorted(sor, key=itemgetter(1))
# for i in range(len(sor)):
#     avg += sor[i][1]
# avg /= len(sor)
# print(avg)
#
#
# text = nltk.word_tokenize("hi, I'm a person called Kriti.")
# # word_tokenize("And now for something completely different")
#
# print(nltk.pos_tag(text))
# # [('And', 'CC'), ('now', 'RB'), ('for', 'IN'), ('something', 'NN'),
# # ('completely', 'RB'), ('different', 'JJ')]

path = "C:\\Users\\kriti\\Documents\\Project\\Abstractive_Summarization\\Dataset"
files = os.listdir(path)
for file in files:
    f = open(path + "\\" + file, 'r')
    lines_list = f.readlines()
    f.close()
    break
print(lines_list)
no_sentences = lines_list.__len__()
for i in range(no_sentences):
    # text = nltk.word_tokenize("hi, I'm a person called Kriti.")
    # # word_tokenize("And now for something completely different")
    #
    # print(nltk.pos_tag(text))
    # word_list = lines_list[i].split()  # for  the current sentence only
    word_list = re.findall(r"[\w']+|[.,!?;]", lines_list[i])
    sentence_size = word_list.__len__()
    for j in range(sentence_size):
        LABEL = word_list[j]
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
plt.savefig('labels.png')
