from nltk import word_tokenize, pos_tag
from nltk.corpus import wordnet as wn


def penn_to_wn(tag):
    """ Convert between a Penn Treebank tag to a simplified Wordnet tag """
    if tag.startswith('N'):
        return 'n'
    if tag.startswith('V'):
        return 'v'
    if tag.startswith('J'):
        return 'a'
    if tag.startswith('R'):
        return 'r'
    return None


def tagged_to_synset(word, tag):
    wn_tag = penn_to_wn(tag)
    if wn_tag is None:
        return None
    try:
        return wn.synsets(word, wn_tag)[0]
    except:
        return None


def sentence_similarity(sentence1, sentence2):
    """ compute the sentence similarity using Wordnet """
    # Tokenize and tag
    sentence1 = pos_tag(word_tokenize(sentence1))
    sentence2 = pos_tag(word_tokenize(sentence2))

    # Get the synsets for the tagged words
    synsets1 = [tagged_to_synset(*tagged_word) for tagged_word in sentence1]
    synsets2 = [tagged_to_synset(*tagged_word) for tagged_word in sentence2]

    # Filter out the Nones
    synsets1 = [ss for ss in synsets1 if ss]
    synsets2 = [ss for ss in synsets2 if ss]

    score, count = 0.0, 1

    # For each word in the first sentence
    for syn1 in synsets1:
        arr_simi_score = []
        for syn2 in synsets2:
            simi_score = syn1.path_similarity(syn2)
            if simi_score is not None:
                arr_simi_score.append(simi_score)
                # print('----------------')
                # print(arr_simi_score)
                if (len(arr_simi_score) > 0):
                    best = max(arr_simi_score)
                    score += best
                    count += 1

            # Average the values
    score /= count
    return score


def symmetric_sentence_similarity(candidates):
    """ compute the symmetric sentence similarity using Wordnet """
    no_of_candidates = candidates.__len__()
    remove_sen = []
    for i in range(no_of_candidates):
        for j in range(i + 1, no_of_candidates):
            if i in remove_sen or j in remove_sen:
                continue
            val = (sentence_similarity(candidates[i][0], candidates[j][0]) + sentence_similarity(candidates[j][0],
                                                                                                 candidates[i][0])) / 2
            # print(sentence_similarity(candidates[i][0], candidates[j][0]))
            # print(sentence_similarity(candidates[j][0], candidates[i][0]))
            # print(candidates[i][0], candidates[j][0])
            # print('-----------------------------')
            if val > 0.5:
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


def main():
    candidates = [
        ("Dogs are awesome.", 5),
        ("Some gorgeous creatures are felines.", 10),
        ("Dolphins are swimming mammals.", 15),
        ("Cats are beautiful animals.", 20)
    ]
    symmetric_sentence_similarity(candidates)


if __name__ == '__main__':
    main()
