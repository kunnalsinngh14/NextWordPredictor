import numpy as np 
import pandas as pd
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.preprocessing.sequence import pad_sequences
import pickle
import streamlit as st

st.set_page_config(page_title="Next Word Predictor", page_icon="🧠", layout="centered")

model = keras.models.load_model('model.keras')

with open('tokenizer.pkl', 'rb') as f:
    tok = pickle.load(f)

st.title("Next Word Predictor 🧠")
st.write("Start typing a sentence, and the AI will guess your next word!")

input_text = st.text_input("Enter your text...")
if(st.button("Predict")):
    if input_text != "":
        seqs = tok.texts_to_sequences([input_text])
        x = pad_sequences(seqs, maxlen=20, padding='pre')
        pred = model.predict(x, verbose=0)
        pred_idx = np.argmax(pred)
        if pred_idx in tok.index_word:
            predicted_word = tok.index_word[pred_idx]
            st.success(f"**Predicted Word:** {predicted_word}")
            st.info(f"**Sentence:** {input_text} {predicted_word}")
        else:
            st.error("I'm not sure what the next word is!")
    else:
        st.header("please enter a valid sentence")