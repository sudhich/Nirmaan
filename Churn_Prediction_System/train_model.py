# ============================================================
# Customer Churn Prediction
# train_model.py
# ============================================================

import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix
)

# ============================================================
# Dataset Path
# ============================================================

CSV_FILE = "customer_churn.csv"

# ============================================================
# Load Dataset
# ============================================================

print("=" * 60)
print("Loading Dataset...")
print("=" * 60)

df = pd.read_csv(CSV_FILE)

print("Dataset Loaded Successfully!")
print("Dataset Shape :", df.shape)

# ============================================================
# Check Missing Values
# ============================================================

print("\nMissing Values")
print(df.isnull().sum())

# Remove Missing Values

df.dropna(inplace=True)

# ============================================================
# Drop Unnecessary Columns
# ============================================================

drop_columns = [
    "Names",
    "Onboard_date"
]

df.drop(columns=drop_columns, inplace=True)

# ============================================================
# Features & Target
# ============================================================

X = df.drop("Churn", axis=1)

y = df["Churn"]

# ============================================================
# Identify Columns
# ============================================================

categorical_columns = X.select_dtypes(include=["object"]).columns.tolist()

numeric_columns = X.select_dtypes(exclude=["object"]).columns.tolist()

print("\nCategorical Columns")
print(categorical_columns)

print("\nNumeric Columns")
print(numeric_columns)

# ============================================================
# Preprocessing
# ============================================================

categorical_transformer = Pipeline(

    steps=[

        ("imputer", SimpleImputer(strategy="most_frequent")),

        ("encoder", OneHotEncoder(handle_unknown="ignore"))

    ]

)

numeric_transformer = Pipeline(

    steps=[

        ("imputer", SimpleImputer(strategy="mean"))

    ]

)

preprocessor = ColumnTransformer(

    transformers=[

        ("cat", categorical_transformer, categorical_columns),

        ("num", numeric_transformer, numeric_columns)

    ]

)

# ============================================================
# Machine Learning Pipeline
# ============================================================

model = Pipeline(

    steps=[

        ("preprocessor", preprocessor),

        ("classifier", LogisticRegression(max_iter=1000))

    ]

)

# ============================================================
# Train Test Split
# ============================================================

X_train, X_test, y_train, y_test = train_test_split(

    X,
    y,

    test_size=0.20,

    random_state=42,

    stratify=y

)

# ============================================================
# Train Model
# ============================================================

print("\nTraining Model...")

model.fit(X_train, y_train)

print("Training Completed Successfully!")

# ============================================================
# Prediction
# ============================================================

y_pred = model.predict(X_test)

# ============================================================
# Evaluation
# ============================================================

accuracy = accuracy_score(y_test, y_pred)

precision = precision_score(y_test, y_pred)

recall = recall_score(y_test, y_pred)

f1 = f1_score(y_test, y_pred)

cm = confusion_matrix(y_test, y_pred)

# ============================================================
# Display Performance
# ============================================================

print("\n")
print("=" * 60)
print("MODEL PERFORMANCE")
print("=" * 60)

print(f"Accuracy  : {accuracy:.4f}")

print(f"Precision : {precision:.4f}")

print(f"Recall    : {recall:.4f}")

print(f"F1 Score  : {f1:.4f}")

print("\nConfusion Matrix")

print(cm)

print("=" * 60)

# ============================================================
# Save Model
# ============================================================

joblib.dump(model, "model.pkl")

print("\nModel saved as model.pkl")

# ============================================================
# Save Feature Names
# ============================================================

joblib.dump(list(X.columns), "features.pkl")

print("Feature list saved as features.pkl")

# ============================================================
# Save Accuracy
# ============================================================

joblib.dump(accuracy, "accuracy.pkl")

print("Accuracy saved as accuracy.pkl")

# ============================================================
# Finish
# ============================================================

print("\nProject Training Completed Successfully!")

print("=" * 60)