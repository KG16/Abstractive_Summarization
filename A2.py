# import os
# path = "C:\\Users\\kriti\\Documents\\Project\\Abstractive_Summarization\\Dataset"
# files = os.listdir(path)
# for file in files:
#     newf=""
#     with open(path + "\\" + file, 'r') as f:
#         for line in f:
#             if ("." or ","or "but"or "and"or "yet"or "or" or "so" or "!" or "?") not in line[-1]:
#                 newf+=line.strip()+".\n"
#         f.close()
#     with open(path + "\\" + file, 'w') as f:
#         f.write(newf)
#         f.close()
#
#     print(newf)
#     break
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
        # print('=========================================')
        # print(syn1)
        # print('----------------')
        for syn2 in synsets2:
            # print(syn2)
            simi_score = syn1.path_similarity(syn2)
            # print(simi_score)
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


# def symmetric_sentence_similarity(sentence1, sentence2):
#     """ compute the symmetric sentence similarity using Wordnet """
#     return (sentence_similarity(sentence1, sentence2) + sentence_similarity(sentence2, sentence1)) / 2


def symmetric_sentence_similarity(candidates):
    """ compute the symmetric sentence similarity using Wordnet """
    # return (sentence_similarity(sentence1, sentence2) + sentence_similarity(sentence2, sentence1)) / 2
    no_of_candidates = candidates.__len__()
    for i in range(no_of_candidates):
        for j in range(i + 1, no_of_candidates):
            val = (sentence_similarity(candidates[i][0], candidates[j][0] + sentence_similarity(candidates[j][0],
                                                                                                candidates[
                                                                                                    i][0])) / 2)
            if val > 0.5:
                if candidates[i][1] > candidates[j][1]:
                    candidates.remove(candidates[j])
                else:
                    candidates.remove(candidates[i])



def main():
    candidates = [
        # "Dogs are awesome.",
        "Some gorgeous creatures are felines.",
        # "Dolphins are swimming mammals.",
        "Cats are beautiful animals."
    ]
    symmetric_sentence_similarity(candidates)
    # print(symmetric_sentence_similarity("Cats is beautiful.","Cats are beautiful animals."))


#     Some gorgeous creatures are felines.


if __name__ == '__main__':
    main()
