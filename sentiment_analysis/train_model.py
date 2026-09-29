
# ============================================================
# Sentiment Analysis - Model Training
# ============================================================

import os
import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report


# ============================================================
# 1. PATHS
# ============================================================

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

DATA_PATH = os.path.join(BASE_DIR, "sentiment_data.csv")

MODEL_PATH = os.path.join(BASE_DIR, "model.pkl")
VECTORIZER_PATH = os.path.join(BASE_DIR, "vectorizer.pkl")


# ============================================================
# 2. LOAD DATASET
# ============================================================

print("Loading dataset...")

df = pd.read_csv(DATA_PATH)

print("\nDataset Shape:", df.shape)
print("\nColumns:")
print(df.columns.tolist())


# ============================================================
# 3. REMOVE UNNECESSARY COLUMN
# ============================================================

if "Unnamed: 0" in df.columns:
    df.drop("Unnamed: 0", axis=1, inplace=True)


# ============================================================
# 4. SELECT REQUIRED COLUMNS
# ============================================================

df = df[["Comment", "Sentiment"]]


# ============================================================
# 5. HANDLE MISSING VALUES
# ============================================================

df.dropna(subset=["Comment", "Sentiment"], inplace=True)


# Convert comments to string
df["Comment"] = df["Comment"].astype(str)


# ============================================================
# 6. DISPLAY SENTIMENT DISTRIBUTION
# ============================================================

print("\nSentiment Distribution:")
print(df["Sentiment"].value_counts())


# ============================================================
# 7. INPUT AND TARGET
# ============================================================

X = df["Comment"]
y = df["Sentiment"]


# ============================================================
# 8. TRAIN-TEST SPLIT
# ============================================================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)

print("\nTraining samples:", len(X_train))
print("Testing samples :", len(X_test))


# ============================================================
# 9. TF-IDF VECTORIZATION
# ============================================================

print("\nCreating TF-IDF features...")

vectorizer = TfidfVectorizer(
    max_features=20000,
    ngram_range=(1, 2),
    stop_words="english"
)

X_train_tfidf = vectorizer.fit_transform(X_train)
X_test_tfidf = vectorizer.transform(X_test)

print("TF-IDF Training Shape:", X_train_tfidf.shape)
print("TF-IDF Testing Shape :", X_test_tfidf.shape)


# ============================================================
# 10. TRAIN LOGISTIC REGRESSION
# ============================================================

print("\nTraining Logistic Regression model...")

model = LogisticRegression(
    max_iter=1000
)

model.fit(X_train_tfidf, y_train)

print("Training completed!")


# ============================================================
# 11. PREDICTION
# ============================================================

y_pred = model.predict(X_test_tfidf)


# ============================================================
# 12. MODEL EVALUATION
# ============================================================

accuracy = accuracy_score(y_test, y_pred)

print("\n==============================")
print("MODEL PERFORMANCE")
print("==============================")

print(f"Accuracy: {accuracy:.4f}")

print("\nClassification Report:")
print(classification_report(y_test, y_pred))


# ============================================================
# 13. SAVE MODEL
# ============================================================

joblib.dump(model, MODEL_PATH)

print("\nModel saved to:")
print(MODEL_PATH)


# ============================================================
# 14. SAVE TF-IDF VECTORIZER
# ============================================================

joblib.dump(vectorizer, VECTORIZER_PATH)

print("\nVectorizer saved to:")
print(VECTORIZER_PATH)


# ============================================================
# 15. TEST WITH SAMPLE COMMENTS
# ============================================================

sample_comments = [
    "I really love this product!",
    "This is terrible and I hate it.",
    "The product is okay."
]

sample_tfidf = vectorizer.transform(sample_comments)

predictions = model.predict(sample_tfidf)

print("\n==============================")
print("SAMPLE PREDICTIONS")
print("==============================")

for comment, prediction in zip(sample_comments, predictions):
    print(f"\nComment   : {comment}")
    print(f"Sentiment : {prediction}")


print("\nTraining process completed successfully!")
