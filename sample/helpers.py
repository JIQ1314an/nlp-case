from collections import Counter
from . import core

import pandas as pd


def read(path):
    corpus = []
    with open(path) as f:
        for line in f.readlines():
            corpus.append(line.rstrip('\n'))
    # print(corpus)
    return corpus


def split_sentence(corpus: list):
    """split corpus

    :param corpus: list type sentence
    :return: word_list: two-dimensional list

    """
    word_list = list()
    for i in range(len(corpus)):
        word_list.append(corpus[i].split(' '))
    return word_list


def count_word_num(corpus: list):
    """Count words
    :param corpus: two-dimensional list
    :return: list, the element is Count type
    """
    word_list = split_sentence(corpus)
    count_list = []
    unrepeated_word_list = []
    for i in range(len(word_list)):
        # The Counter type is similar to a dict, returns 0 for nonexistent keys
        count_list.append(Counter(word_list[i]))
        unrepeated_word_list.extend(word_list[i])

    return pd.Series(unrepeated_word_list).unique(), count_list


def get_text_vector(corpus: list):
    text_vector = {}
    # Get words and statistics for all articles
    unrepeated_word_list, count_list = count_word_num(corpus)
    # print(unrepeated_word_list)

    for i, count in enumerate(count_list):  # Get words and statistics for the current article
        print("TF-IDF statistics for Document {}".format(i + 1))
        scores = {word: core.tf_idf(word, count, count_list) for word in count}
        # print(scores.keys())
        # Sort in descending order by value
        sorted_words = sorted(scores.items(), key=lambda x: x[1], reverse=True)

        for word, score in sorted_words:
            print("word: {}, TF-IDF: {}\t".format(word, round(score, 5)))

        # get text vector
        for w in unrepeated_word_list:
            if w in scores.keys():
                fill_text_vector(text_vector, w, round(scores[w], 5))
            else:
                fill_text_vector(text_vector, w, 0)

        # print(text_vector)
        print()

    return pd.DataFrame(text_vector).values


def fill_text_vector(text_vector, w, score):
    temp_list = text_vector.get(w)  # Key=w If not exists, then return None
    if temp_list:
        temp_list.append(score)
        text_vector[w] = temp_list
    else:
        text_vector[w] = [score]
