from tensorflow.keras import Input, Model
from tensorflow.keras.layers import Embedding, LSTM, Concatenate, Dense
from create_corpus import create_corpuses
from create_dataset import create_dataset
import pickle

lstm_layer_size= 64
embedding_layer_size = 100
dropout_rate= 0.3
activation= 'softmax'
epochs=10

all_text = ''

with open('./nlp-ai/wikipedia_articles.txt', encoding="utf8") as f:
    for line in f:
        all_text += line

texts = all_text.split("___NEXT___")

print('texts - ', texts[0])

positive_pairs, negative_pairs = create_dataset(texts)

X, y, tokenizer = create_corpuses(texts, positive_pairs, negative_pairs)

print('X - ', X[0])

weights = y * (len(y) - sum(y)) / sum(y)  # positive weight
weights[weights == 0] = 1  # negative weight
vocab_size = len(tokenizer.word_index) + 1

forward_model_input = Input(shape=(X.shape[-1],))
forward_model = Embedding(vocab_size, embedding_layer_size)(forward_model_input)
forward_model = LSTM(lstm_layer_size, return_sequences=False, dropout=dropout_rate,
            go_backwards=False)(forward_model)

print('Done with forward pass')

backward_model_input = Input(shape=(X.shape[-1],))
backward_model = Embedding(vocab_size, embedding_layer_size)(backward_model_input)
backward_model = LSTM(lstm_layer_size, return_sequences=False, dropout=dropout_rate,
            go_backwards=True)(backward_model)

print('Done with backward pass')

model_concatenated = Concatenate()([forward_model, backward_model])
model_concatenated = Dense(lstm_layer_size * 2, activation=activation)(model_concatenated)

model_concatenated = Dense(1, activation='sigmoid')(model_concatenated)
model = Model(inputs=[forward_model_input, backward_model_input], outputs=model_concatenated)

print('Compiling the model')
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

print('Fitting the model')
model.fit([X[:, 0, :], X[:, 1, :]], y, batch_size=256, epochs=epochs, shuffle=True,
    sample_weight=weights)

print('Model fit. Now pickling.')
pickle.dump(model, open('sentence_model.pkl','wb'))
print('Pickled the model. Now pickling the tokenizer.')
pickle.dump(tokenizer, open('sentence_model_tokenizer.pkl','wb'))