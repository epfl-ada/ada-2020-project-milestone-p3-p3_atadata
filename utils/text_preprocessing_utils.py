from nltk.corpus import stopwords
import numpy as np


def clean_words(X):
    new_words = []
    for word in X:
        # We consider contractions not very valuable, as well as very short words/individual letters
        if len(word) <= 3 or '\'' in word:
            continue

        # Removing stop words
        if word in stopwords.words('english'):
            continue

        new_words.append(word)
    return new_words


def read_glove_embeddings(filename):
    embeddings = {}

    f = open(filename)
    for line in f:
        values = line.split()
        word = values[0]
        embeddings[word] = np.asarray(values[1:], dtype='float32')
    f.close()

    print('Embeddings containing %s word vectors.' % len(embeddings))
    return embeddings


def compute_relevant_embedding_matrix(embeddings, all_words, max_words, embedding_dim):
    """Computes the embeddings matrix and the mapping of words to indexes"""
    # Also compute the mapping from words to indexes in matrix
    word_to_idx = {}
    embedding_matrix = np.zeros((max_words, embedding_dim))

    idx = 0
    # Only go through unique words
    for word in list(set(all_words)):
        embedding_vector = embeddings.get(word)
        if embedding_vector is not None:
            embedding_matrix[idx] = embedding_vector
            word_to_idx[word] = idx
        idx = idx + 1

    return embedding_matrix, word_to_idx
