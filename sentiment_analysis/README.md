````markdown
# 😊 Sentiment Analysis Application

A Machine Learning and NLP project that predicts the sentiment of a text comment using **TF-IDF** and **Logistic Regression**.

The application provides a simple web interface built with **Streamlit**, where users can enter a comment and receive a sentiment prediction.

---

## 📌 Project Overview

Sentiment Analysis is an NLP task used to determine the emotional tone of a piece of text.

For example:

> "I really love this product!"

Prediction:

```text
😊 Positive
````

Another example:

> "This product is terrible."

Prediction:

```text
😞 Negative
```

This project uses a Machine Learning approach to classify comments into sentiment categories.

---

## 🎯 Project Objectives

* Understand Natural Language Processing (NLP)
* Work with a real-world text dataset
* Perform basic text preprocessing
* Convert text into numerical features using TF-IDF
* Train a Logistic Regression classifier
* Evaluate the trained model
* Save the trained model
* Build a web application using Streamlit
* Perform real-time sentiment prediction

---

## 🏗️ Project Architecture

                  Dataset
                     │
                     ▼
              Data Preprocessing
                     │
                     ▼
              Train/Test Split
                     │
                     ▼
                TF-IDF
              Vectorization
                     │
                     ▼
            Logistic Regression
                     │
                     ▼
              Trained Model
                     │
              ┌──────┴──────┐
              │             │
              ▼             ▼
        model.pkl      vectorizer.pkl
              │             │
              └──────┬──────┘
                     ▼
             Streamlit App
                     │
                     ▼
              User enters text
                     │
                     ▼
              Sentiment Result


---

## 📂 Project Structure


sentiment_analysis/
│
├── sentiment_data.csv
│
├── train_model.py
│
├── app.py
│
├── model.pkl
│
├── vectorizer.pkl
│
├── requirements.txt
│
└── README.md


---

## 📊 Dataset

The project uses a CSV dataset containing comments and their corresponding sentiment labels.

### Dataset columns

| Column       | Description                               |
| ------------ | ----------------------------------------- |
| `Comment`    | Text/comment written by the user          |
| `Sentiment`  | Sentiment class/label                     |
| `Unnamed: 0` | Index column removed during preprocessing |

The dataset contains approximately **241,000 comments**.

> **Note:** The exact meaning of sentiment labels `0`, `1`, and `2` should be verified from the dataset/source before presenting them as Negative, Neutral, and Positive in the final application.

---

## 🛠️ Technologies Used

* Python
* Pandas
* Scikit-learn
* Joblib
* Streamlit
* TF-IDF
* Logistic Regression

---

## 📦 Installation

### Step 1: Create a virtual environment

```bash
python -m venv sentiment
```

### Windows

```bash
sentiment\Scripts\activate
```

If PowerShell blocks activation, you can also run the project using the Python executable inside the virtual environment.

---

### Step 3: Install dependencies

```bash
pip install -r requirements.txt
```

---

# 🧠 Model Training

Run:

```bash
python train_model.py
```

The training script performs the following steps:

```text
Load Dataset
     ↓
Remove Unnecessary Column
     ↓
Handle Missing Values
     ↓
Separate Features and Target
     ↓
Train/Test Split
     ↓
TF-IDF Vectorization
     ↓
Logistic Regression
     ↓
Model Evaluation
     ↓
Save Model
```

After training, two files are created:

```text
model.pkl
vectorizer.pkl
```

### `model.pkl`

Contains the trained Logistic Regression model.

### `vectorizer.pkl`

Contains the trained TF-IDF vectorizer.

Both files are required by the Streamlit application.

---

# 🌐 Running the Web Application

After training the model, run:

```bash
streamlit run app.py
```

Streamlit will start a local web server and open the application in your browser.

---

# 💻 Using the Application

Enter a comment into the text box.

Example:

```text
I really enjoyed this product. It is excellent!
```

Click:

```text
Predict Sentiment
```

The application will display the predicted sentiment and model confidence.

---

## 🔄 Prediction Workflow

When a user enters:

```text
"I love this product!"
```

the application performs:

```text
User Input
    ↓
Text
    ↓
TF-IDF Vectorization
    ↓
Numerical Features
    ↓
Logistic Regression
    ↓
Prediction
    ↓
Sentiment
```

---

# 📈 Machine Learning Model

## TF-IDF

TF-IDF stands for:

**Term Frequency – Inverse Document Frequency**

It converts text into numerical values that a Machine Learning model can understand.

For example:

```text
"I love this product"
```

is converted into a numerical vector.

---

## Logistic Regression

Logistic Regression is used as the classification algorithm.

The model learns patterns from the training comments and their sentiment labels.

During prediction:

```text
New Comment
     ↓
TF-IDF
     ↓
Logistic Regression
     ↓
Sentiment Class
```

---

# 📊 Model Evaluation

The training script evaluates the model using:

* Accuracy
* Precision
* Recall
* F1-score
* Classification Report

The actual performance values are generated when:

```bash
python train_model.py
```

is executed.

---

# 🎯 Example Predictions

### Example 1

Input:

```text
I really love this product!
```

Output:

```text
😊 Positive
```

### Example 2

Input:

```text
This product is terrible.
```

Output:

```text
😞 Negative
```

### Example 3

Input:

```text
The product is okay.
```

Output:

```text
😐 Neutral
```

> These examples assume the dataset labels are mapped as `0 = Negative`, `1 = Neutral`, and `2 = Positive`. Verify the dataset's actual label mapping before final deployment.

---

# 🚀 Future Improvements

This project can be improved by adding:

* Better text preprocessing
* Lemmatization
* Stemming
* Word embeddings
* Word2Vec
* Transformer models
* BERT
* Hugging Face Transformers
* Sentiment probability charts
* Batch CSV prediction
* Prediction history
* REST API using FastAPI
* Cloud deployment

---

# 📚 Concepts Learned

Through this project, we learn:

```text
NLP
│
├── Text Data
├── Text Preprocessing
├── TF-IDF
├── Feature Extraction
├── Train/Test Split
├── Classification
├── Logistic Regression
├── Model Evaluation
├── Model Serialization
└── Streamlit Deployment
```

---

# 👨‍💻 Author

**Sudhiram Chauhan**

AI Trainer | Data Science | Machine Learning | NLP

---

# ⭐ Project Summary

This project demonstrates an end-to-end NLP Machine Learning workflow:

```text
Real-World Dataset
       ↓
Data Cleaning
       ↓
TF-IDF
       ↓
Machine Learning
       ↓
Model Evaluation
       ↓
Model Saving
       ↓
Streamlit Application
       ↓
Real-Time Sentiment Prediction
```

This project is designed as **Day 45 — NLP Project: Sentiment Analysis Application**.

```

You now have the three main project files: **`train_model.py`**, **`app.py`**, and **`README.md`**. The next useful file is `requirements.txt`, and then we can run the project end-to-end and fix any errors that appear.
```
