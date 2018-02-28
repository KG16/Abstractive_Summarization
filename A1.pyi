import nltk

class Opinosis_Graph():
    def __init__(self, label, pos, SID, PID):
        label = label
        pos = pos
        sid = []
        sid.append(SID)
        pid = []  #  .append(PID)
        pid.append(PID)

    '''
    def create_graph:
        opinosisG = nx.Graph()

    def insert_node(self):

    def update_node(self):
    '''


def read_input_datafiles():
    import glob
    path = "C:\Users\kriti\OneDrive\Documents\3-2\Project\Dataset"
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
        #word_list = lines_list[i].split()  # for  the current sentence only
        text = nltk.word_tokenize(lines_list[i])
        text_pos_tagged = nltk.pos_tag(text)
        sentence_size = text_pos_tagged.__len__()
        print(text_pos_tagged)
        '''
        for j in range(sentence_size):
            LABEL = word_list[j]
            PID = j
            SID = i
            new_node = Opinosis_Graph(LABEL, SID, PID)
            if new_node.LABEL not in G:  #checking with just label not complete node

                new_node.insert_node()  # do I need to pass parameters
            else:
                new_node.update_node()
                
                """
                G=nx.Graph()
                # Add nodes and edges
                G.add_edge("Node1", "Node2")
                nx.draw(G, with_labels = True)
                plt.savefig('labels.png')
                """
        '''
