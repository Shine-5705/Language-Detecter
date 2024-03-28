import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Embedding, Bidirectional
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.preprocessing.text import Tokenizer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
data = pd.read_csv("Language Detection.csv")
texts = data['Text']

labels = data['Language']

tokenizer = Tokenizer()
tokenizer.fit_on_texts(texts)
sequences = tokenizer.texts_to_sequences(texts)
max_len = max([len(seq) for seq in sequences])
vocab_size = len(tokenizer.word_index) + 1

X = pad_sequences(sequences, maxlen=max_len, padding='post')
label_encoder = LabelEncoder()
y = label_encoder.fit_transform(labels)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = Sequential()
model.add(Embedding(vocab_size, 64))
model.add(Bidirectional(LSTM(128)))
model.add(Dense(64, activation='relu'))
model.add(Dense(len(set(labels)), activation='softmax'))

model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

model.summary()
history = model.fit(X_train, y_train, epochs=10, batch_size=32, validation_split=0.1)
loss, accuracy = model.evaluate(X_test, y_test)
print("Test Accuracy:", accuracy)
def predict_language(text):
    seq = tokenizer.texts_to_sequences([text])
    padded = pad_sequences(seq, maxlen=max_len, padding='post')
    pred = model.predict(padded)
    pred_label = label_encoder.inverse_transform([np.argmax(pred)])
    return pred_label[0]

# Test the function
text_to_predict = "असाइनमेंट को पाठ्यक्रम में मौजूद पूरी वेबसाइट पर लागू किया जाना चाहिए।"
predicted_language = predict_language(text_to_predict)
print("Predicted Language:", predicted_language)
