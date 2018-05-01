import difflib

fn1 = 'speech as secretary of state via .'
fn2 = 'will be secretary of state via'
score = difflib.SequenceMatcher(None, fn1.lower(), fn2.lower()).ratio()
print(score)


def eliminate_duplicate(candidates):
    """ compute the symmetric sentence similarity using Wordnet """
    no_of_candidates = candidates.__len__()
    remove_sen = []
    for i in range(no_of_candidates):
        for j in range(i + 1, no_of_candidates):
            if i in remove_sen or j in remove_sen:
                continue
            val = difflib.SequenceMatcher(None, candidates[i], candidates[j]).ratio()
            # print(sentence_similarity(candidates[i][0], candidates[j][0]))
            # print(sentence_similarity(candidates[j][0], candidates[i][0]))
            # print(candidates[i][0], candidates[j][0])
            # print('-----------------------------')
            if val > 0.6:
                if candidates[i][1] > candidates[j][1]:
                    if j not in remove_sen:
                        remove_sen.append(j)
                else:
                    if i not in remove_sen:
                        remove_sen.append(i)
    remove_sen.sort(reverse=True)
    for k in remove_sen:
        del candidates[k]
    # print(candidates)
    return candidates
