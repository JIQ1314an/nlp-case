import numpy as np
import pandas as pd

from . import helpers
import math


def run(corpus: list):
    text_vector = helpers.get_text_vector(corpus)
    print(text_vector)
    get_text_similarity(text_vector)


def get_text_similarity(text_vector: list):
    # n! cases
    length = len(text_vector) - 1
    for i in range(length):
        print("Similarity between Document {} and the rest of the documents".format(i + 1))
        for j in range(i + 1, length + 1):
            text_sim = cal_cos(text_vector[i], text_vector[j])
            print(" Doc{}: {}".format(j + 1, round(text_sim, 5)))
        print()


def cal_cos(doc, other_doc):
    """The similarity between two texts is calculated based on the cosine formula
    :param doc: One-dimensional array or list type
    :param other_doc: Same as above
    :return:
    """
    doc = np.asarray(doc)
    other_doc = np.asarray(other_doc)

    molecular = sum(doc * other_doc)
    denominator = np.sqrt(sum(doc ** 2)) * np.sqrt(sum(other_doc ** 2))
    return molecular / denominator


def tf(word, count):
    term_occurrences_in_doc = count[word]
    num_terms_in_doc = sum(count.values())
    return term_occurrences_in_doc / num_terms_in_doc


def idf(word, count_list):
    total_num_docs = len(count_list)
    num_docs_containing_term = sum([1 for count in count_list if word in count])
    return math.log(total_num_docs / (1 + num_docs_containing_term))


def tf_idf(word, count, count_list):
    """
    :param word: Solve for tf-idf word
    :param count: Words and statistics for the current article
    :param count_list: Words and statistics for all articles
    :return:
    """
    return tf(word, count) * idf(word, count_list)
