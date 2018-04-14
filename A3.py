import glob

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

path = "C:\\Users\\kriti\\OneDrive\\Documents\\3-2\\Project\\Dataset"
files = glob.glob(path)
lines_list = []  # do I need list of list?
for file in files:
    f = open(file, 'r')
    lines_list = f.readlines()
    f.close()
    break
print(lines_list.lower())
