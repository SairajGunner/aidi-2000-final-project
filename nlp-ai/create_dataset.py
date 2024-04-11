from typing import List
import numpy as np
import nltk
from itertools import chain
nltk.download('punkt')

def create_dataset(texts: List[str], min_sentence_length_for_splitting=10):
    positive_pairs = []
    negative_pairs = []
    for text in texts:
        sentences = nltk.sent_tokenize(text)
        if len(sentences)>1:
          sentences = [nltk.tokenize.word_tokenize(sentence.replace('.', '')) for sentence in sentences]
          sentences_pairs = list(zip(sentences[:-1], sentences[1:]))
          positive_pairs.append(sentences_pairs)

          for negative_sample in sentences:
              if len(negative_sample) > min_sentence_length_for_splitting:
                  first_sent, second_sent = negative_sample[:len(negative_sample) // 2], negative_sample[len(negative_sample) // 2:]
                  negative_pairs.append([(first_sent, second_sent)])
    
    positive_pairs = list(chain.from_iterable(positive_pairs))
    negative_pairs = list(chain.from_iterable(negative_pairs))
    
    return positive_pairs, negative_pairs