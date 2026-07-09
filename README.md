# 📝 Next Word Predictor

A Deep Learning streamlit application that predicts the **next word** in a sentence using an **LSTM (Long Short-Term Memory) Neural Network**, **TensorFlow/Keras**, and **Streamlit**.

---

## 🚀 Features

* Predicts the most likely next word based on user input.
* Uses Keras Tokenizer for text preprocessing.
* Converts text into integer sequences and applies sequence padding.
* Built using an Embedding layer and LSTM neural network.
* Interactive Streamlit web application.
* Trained on a custom text corpus.

---

## 🛠️ Tech Stack

* Python
* NumPy
* TensorFlow
* Keras
* Streamlit
* Pickle

---

## 📂 Project Structure

```text
Next-Word-Predictor/
│
├── app.py                     # Streamlit web application
├── src.ipynb                  # Model training notebook
├── next_word_predictor.txt    # Training dataset
├── model.keras                # Trained LSTM model
├── tokenizer.pickle           # Saved tokenizer
├── requirements.txt           # Project dependencies
└── README.md
```

---

## 📊 Model Training Pipeline

1. Load the text dataset.
2. Convert all text to lowercase.
3. Tokenize the text using Keras Tokenizer.
4. Convert text into integer sequences.
5. Generate input-output sequence pairs.
6. Pad all input sequences to the same length.
7. One-hot encode the target words.
8. Build an LSTM-based neural network.
9. Train the model using categorical cross-entropy loss.
10. Save the trained model and tokenizer.

---

## 🧠 Model Architecture

```text
Input Layer
      │
Embedding Layer
      │
LSTM Layer (32 Units)
      │
Dense Layer (Softmax - Vocabulary Size Outputs)
```

---

## ⚙️ Training Configuration

```python
Vocabulary Size : 10000
Embedding Size  : 32
LSTM Units      : 32
Optimizer       : Adam
Loss Function   : Categorical Crossentropy
Padding         : Pre
```

---



## ⚙️ Installation

### Clone the Repository

```bash
git clone https://github.com/your-username/Next-Word-Predictor.git
cd Next-Word-Predictor
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run the Application

```bash
streamlit run app.py
```

---

## 💻 Usage

1. Launch the Streamlit application.
2. Enter the beginning of a sentence.
3. Click the **Predict** button.
4. The model predicts the most probable next word.

---

## 📷 Example

### Input

```text
the sun was
```

### Output

```text
shining
```

---

### Input

```text
people were
```

### Output

```text
playing
```



---

© 2026 Kunal Singh
