import streamlit as st
import pandas as pd
import numpy as np
import pickle
import re
from keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import load_model

# Load label encoder
with open("Model/label_encoder.pkl", "rb") as f:
    label_encoder = pickle.load(f)

# Load tokenizer
with open("Model/tokenizer.pkl", "rb") as f:
    tokenizer = pickle.load(f)

# Load model
model = load_model("Model/emotion_det.h5")

# Preprocessing functions
def preprocess_text(text):
    text = text.lower()
    text = re.sub(r'\W', ' ', text)
    text = re.sub(r'\s+', ' ', text)
    return text

def predict_emotion(test_sentence):
    test_sentence = preprocess_text(test_sentence)
    test_sequence = tokenizer.texts_to_sequences([test_sentence])
    test_sequence_pad = pad_sequences(test_sequence, maxlen=80)  # Menggunakan panjang maksimum yang diharapkan oleh model
    predicted_class = np.argmax(model.predict(test_sequence_pad), axis=-1)
    predicted_emotion = label_encoder.inverse_transform(predicted_class)[0]
    return predicted_emotion

# Streamlit app
st.title("Emotion Detection App")

sentence = st.text_input("Enter a sentence:")

if st.button("Predict"):
    if sentence:
        emotion = predict_emotion(sentence)
        st.write(f"The predicted emotion is: {emotion}")
    else:
        st.write("Please enter a sentence.")
