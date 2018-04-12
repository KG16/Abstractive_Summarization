import A1
import GlobVars

graph_helper = A1.graph_helper
G = A1.G
cList = []


def PRI_calc(LABEL):
    return 0


def VEN(LABEL):
    return 0


def ValidSentence(sentence):
    return 0


def Neighbours(LABEL):
    return 0


def Traverse(LABEL, score, sentence, pathLen):
    redundancy = PRI_calc(LABEL)
    if redundancy >= GlobVars.REDUNDANCY_PARA:
        if (VEN(LABEL)):
            if ValidSentence(sentence):
                final_score = score / pathLen
                cList.append(sentence, final_score)  # check appending tupple in list
    for vn in Neighbours(LABEL):


def main():
    return 0
