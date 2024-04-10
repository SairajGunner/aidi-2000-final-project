import numpy as np
from create_corpus import sent2seq
import nltk
import pickle
from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin

sentencer_model_tokenizer = pickle.load(open("./nlp-ai/sentence_model_tokenizer.pkl", "rb"))
sentencer_model = pickle.load(open("./nlp-ai/sentence_model.pkl", "rb"))

sentence_length = 80

def transform(sentences, model, tokenizer):
    if len(sentences) == 0:
        return []
    splitted_sentences = [sentences[0]]
    for sentence in sentences[1:]:
        previous_sentence = splitted_sentences.pop()
        pair_sentences = np.array([sent2seq(tokenizer, nltk.tokenize.word_tokenize(previous_sentence), padding_location="pre"),
                                    sent2seq(tokenizer, nltk.tokenize.word_tokenize(sentence), padding_location="post")])

        prob_split = model.predict([pair_sentences[0, :].reshape(1, sentence_length),
                                              pair_sentences[1, :].reshape(1, sentence_length)])[:, 0][0]
        if prob_split > 0.5:
            splitted_sentences += [previous_sentence, sentence]
        else:
            splitted_sentences += [(previous_sentence + ' ' + sentence)]

    return splitted_sentences

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/process', methods=["POST"])
@cross_origin()
def predict():
    sentences = request.json['sentences']
    response = {"prediction": transform(sentences, sentencer_model, sentencer_model_tokenizer)}
    return jsonify(response)

app.run()