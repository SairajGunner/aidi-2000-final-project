import numpy as np
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.preprocessing.text import Tokenizer
import nltk
from itertools import chain

sentence_length = 80

def fit_tokenizer(texts, tokenizer):
    corpus = [[nltk.tokenize.word_tokenize(sentence) for sentence in nltk.sent_tokenize(text)] for text in texts]
    corpus = list(chain.from_iterable(corpus))
    tokenizer.fit_on_texts(corpus)

def sent2seq(tokenizer, sentence, padding_location="pre"):
    sequences = tokenizer.texts_to_sequences([sentence])
    return pad_sequences(sequences, maxlen=sentence_length, dtype='int32', padding=padding_location,
        truncating=padding_location, value=0.0).squeeze()

def create_corpuses(texts, positive_pairs, negative_pairs):
    tokenizer = Tokenizer()
    fit_tokenizer(texts, tokenizer)

    positive_pairs = np.array([[sent2seq(tokenizer, sent1, padding_location="pre"),
                              sent2seq(tokenizer, sent2, padding_location="post")] for sent1, sent2 in
                            positive_pairs])
    negative_pairs = np.array([[sent2seq(tokenizer, sent1, padding_location="pre"),
                            sent2seq(tokenizer, sent2, padding_location="post")] for sent1, sent2 in negative_pairs])

    # X contains all the text
    X = np.concatenate((positive_pairs, negative_pairs))

    # 1 = split sentences (positive pairs) and 0 = merged sentences (negative pairs)
    y = np.array([1] * len(positive_pairs) + [0] * len(negative_pairs))

    return X, y, tokenizer