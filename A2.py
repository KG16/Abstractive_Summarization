import A1.py
import A3.py
import globvar.py


def summarization():
    g = A1.Opinosis_Graph()
    node_size = number_of_nodes(g)
    candidate = []
    for j in range(node_size):
        if check_VSN(g[j]) == True:
            '''
            path_len=1
            score=0
            clist=[]
            '''
            clist, score, path_len = A3.traverse(g[j], pri[j], label[j])
            candidate.append(clist)

    unique_candidate = eliminate_duplicate(candidate)
    sorted_candidate = sortby_score_path(unique_candidate)
    output = []
    for i in range(globvar.SUM_SIZE):
        ans = pick_next_best_candidate(i, sorted_candidate)
        output.append(ans)
