# ============================================================
# Customer Churn Prediction System
# utils.py
# ============================================================

import joblib
import pandas as pd

# ============================================================
# Load Model
# ============================================================
"""
joblib note:
Every day:

Study for 10 hours
↓
Take exam
↓
Forget everything
↓
Study again tomorrow

With joblib
Study for 10 hours
↓
Save your notes 📒
↓
Tomorrow
↓
Open the notes
↓
Continue immediately

joblib is like saving your notes.
"""
def load_model(model_path="model.pkl"):
    """
    Load trained machine learning model.
    """

    try:

        model = joblib.load(model_path)

        return model

    except FileNotFoundError:

        return None


# ============================================================
# Load Accuracy
# ============================================================

def load_accuracy(file_path="accuracy.pkl"):
    """
    Load saved model accuracy.
    """

    try:

        accuracy = joblib.load(file_path)

        return accuracy

    except:

        return None


# ============================================================
# Predict Churn
# ============================================================

def predict_customer(
        model,
        age,
        total_purchase,
        account_manager,
        years,
        num_sites,
        location,
        company):

    """
    Predict customer churn.
    """

    data = pd.DataFrame({

        "Age": [age],

        "Total_Purchase": [total_purchase],

        "Account_Manager": [account_manager],

        "Years": [years],

        "Num_Sites": [num_sites],

        "Location": [location],

        "Company": [company]

    })

    prediction = model.predict(data)[0]

    probability = model.predict_proba(data)[0]

    confidence = max(probability) * 100

    return prediction, confidence


# ============================================================
# Convert Prediction to Text
# ============================================================

def prediction_text(prediction):

    if prediction == 1:

        return "Customer Will Churn"

    else:

        return "Customer Will Stay"


# ============================================================
# Validate Numeric Inputs
# ============================================================

def validate_inputs(age,
                    purchase,
                    years,
                    sites):

    try:

        age = float(age)

        purchase = float(purchase)

        years = float(years)

        sites = float(sites)

        return True

    except:

        return False


# ============================================================
# Clear Dictionary
# ============================================================

def clear_variables(dictionary):

    for key in dictionary:

        dictionary[key].set("")