import numpy as np
import pandas as pd
import tkinter as tk
from tkinter import messagebox
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Embedding, Bidirectional
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.preprocessing.text import Tokenizer
from sklearn.preprocessing import LabelEncoder

# Assuming you've already loaded your data and built the model as per your example
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

model = Sequential()
model.add(Embedding(vocab_size, 64))
model.add(Bidirectional(LSTM(128)))
model.add(Dense(64, activation='relu'))
model.add(Dense(len(set(labels)), activation='softmax'))

model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
model.fit(X, y, epochs=10, batch_size=32)  # Training on the whole dataset

def predict_language(text):
    seq = tokenizer.texts_to_sequences([text])
    padded = pad_sequences(seq, maxlen=max_len, padding='post')
    pred = model.predict(padded)
    pred_label = label_encoder.inverse_transform([np.argmax(pred)])
    return pred_label[0]

def get_prediction():
    input_text = text_input.get("1.0", "end-1c")
    if input_text.strip() == "":
        messagebox.showerror("Error", "Please enter some text.")
    else:
        predicted_language = predict_language(input_text)
        result_label.config(text=f"Predicted Language: {predicted_language}")

# Create GUI
root = tk.Tk()
root.title("Language Detection")

label = tk.Label(root, text="Enter Text:")
label.pack()

text_input = tk.Text(root, height=5, width=50)
text_input.pack()

predict_button = tk.Button(root, text="Predict Language", command=get_prediction)
predict_button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()
