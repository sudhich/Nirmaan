"""
=========================================================
Customer Segmentation System
Author : Sudhiram Chauhan
GUI     : Tkinter
Model   : K-Means Clustering
=========================================================
"""

import tkinter as tk
import subprocess
import sys
from pathlib import Path
from tkinter import ttk, messagebox

from utils import (
    load_model,
    predict_customer_segment,
    get_business_recommendation
)


BASE_DIR = Path(__file__).resolve().parent


# -------------------------------
# Load Saved Model
# -------------------------------
try:
    model, scaler = load_model()
    MODEL_LOADED = True
except (FileNotFoundError, OSError):
    MODEL_LOADED = False


# -------------------------------
# Main Window
# -------------------------------
root = tk.Tk()
root.title("Customer Segmentation System")
root.geometry("650x620")
root.configure(bg="#F4F6F9")
root.resizable(True, True)


# -------------------------------
# Heading
# -------------------------------
title = tk.Label(
    root,
    text="CUSTOMER SEGMENTATION SYSTEM",
    font=("Arial", 18, "bold"),
    bg="#2E86C1",
    fg="white",
    pady=12
)

title.pack(fill="x")


# -------------------------------
# Input Frame
# -------------------------------
frame = tk.Frame(root, bg="white", bd=2, relief="groove")
frame.pack(pady=20, padx=20, fill="x")


# Age
tk.Label(
    frame,
    text="Age",
    bg="white",
    font=("Arial", 12)
).grid(row=0, column=0, padx=10, pady=10, sticky="w")

age_entry = tk.Entry(frame, font=("Arial", 12), width=20)
age_entry.grid(row=0, column=1)


# Gender
tk.Label(
    frame,
    text="Gender",
    bg="white",
    font=("Arial", 12)
).grid(row=1, column=0, padx=10, pady=10, sticky="w")

gender_combo = ttk.Combobox(
    frame,
    values=["Male", "Female"],
    state="readonly",
    width=18,
    font=("Arial", 11)
)
gender_combo.current(0)
gender_combo.grid(row=1, column=1)


# Income
tk.Label(
    frame,
    text="Annual Income (k$)",
    bg="white",
    font=("Arial", 12)
).grid(row=2, column=0, padx=10, pady=10, sticky="w")

income_entry = tk.Entry(frame, font=("Arial", 12), width=20)
income_entry.grid(row=2, column=1)


# Spending Score
tk.Label(
    frame,
    text="Spending Score (1-100)",
    bg="white",
    font=("Arial", 12)
).grid(row=3, column=0, padx=10, pady=10, sticky="w")

score_entry = tk.Entry(frame, font=("Arial", 12), width=20)
score_entry.grid(row=3, column=1)


# -------------------------------
# Result Frame
# -------------------------------
result_frame = tk.LabelFrame(
    root,
    text="Prediction",
    font=("Arial", 12, "bold"),
    padx=15,
    pady=15
)

result_frame.pack(fill="x", padx=20, pady=10)

cluster_label = tk.Label(
    result_frame,
    text="Cluster : ",
    font=("Arial", 12)
)
cluster_label.pack(anchor="w")

segment_label = tk.Label(
    result_frame,
    text="Customer Type : ",
    font=("Arial", 12)
)
segment_label.pack(anchor="w")

recommendation_label = tk.Label(
    result_frame,
    text="Recommendation : ",
    font=("Arial", 12),
    justify="left",
    wraplength=500
)
recommendation_label.pack(anchor="w", pady=10)

status_label = tk.Label(
    result_frame,
    text="Status : Model Loaded" if MODEL_LOADED else "Status : Model Not Found",
    fg="green" if MODEL_LOADED else "red",
    font=("Arial", 11, "bold")
)

status_label.pack(anchor="w")


# -------------------------------
# Prediction Function
# -------------------------------
def predict():

    if not MODEL_LOADED:
        messagebox.showerror(
            "Error",
            "Model not found.\nTrain the model first."
        )
        return

    try:
        age = float(age_entry.get())
        income = float(income_entry.get())
        score = float(score_entry.get())

        if not 1 <= age <= 120:
            raise ValueError("Age must be between 1 and 120.")
        if income < 0:
            raise ValueError("Annual income cannot be negative.")
        if not 1 <= score <= 100:
            raise ValueError("Spending score must be between 1 and 100.")

        gender = gender_combo.get()

        gender = 1 if gender == "Male" else 0

        cluster = predict_customer_segment(
            model,
            scaler,
            age,
            gender,
            income,
            score
        )

        customer_type, recommendation = \
            get_business_recommendation(cluster)

        cluster_label.config(
            text=f"Cluster : {cluster}"
        )

        segment_label.config(
            text=f"Customer Type : {customer_type}"
        )

        recommendation_label.config(
            text=f"Recommendation :\n{recommendation}"
        )

    except ValueError as error:
        messagebox.showerror(
            "Invalid Input",
            str(error) or "Please enter valid numeric values."
        )


# -------------------------------
# Clear
# -------------------------------
def clear():

    age_entry.delete(0, tk.END)
    income_entry.delete(0, tk.END)
    score_entry.delete(0, tk.END)

    gender_combo.current(0)

    cluster_label.config(text="Cluster :")
    segment_label.config(text="Customer Type :")
    recommendation_label.config(text="Recommendation :")


# -------------------------------
# Train Model
# -------------------------------
def train_model():
    global model, scaler, MODEL_LOADED

    try:
        subprocess.run(
            [sys.executable, "train_model.py"],
            cwd=BASE_DIR,
            check=True
        )
        model, scaler = load_model()
        MODEL_LOADED = True
        status_label.config(text="Status : Model Loaded", fg="green")
        messagebox.showinfo("Training", "Model training completed.")
    except (OSError, subprocess.CalledProcessError) as error:
        MODEL_LOADED = False
        status_label.config(text="Status : Model Not Found", fg="red")
        messagebox.showerror("Training Error", f"Model training failed:\n{error}")


# -------------------------------
# Buttons
# -------------------------------
button_frame = tk.Frame(root, bg="#F4F6F9")
button_frame.pack(pady=20)


train_btn = tk.Button(
    button_frame,
    text="Train Model",
    width=18,
    bg="#3498DB",
    fg="white",
    font=("Arial", 11, "bold"),
    command=train_model
)

train_btn.grid(row=0, column=0, padx=8)


predict_btn = tk.Button(
    button_frame,
    text="Predict Segment",
    width=18,
    bg="#27AE60",
    fg="white",
    font=("Arial", 11, "bold"),
    command=predict
)

predict_btn.grid(row=0, column=1, padx=8)


clear_btn = tk.Button(
    button_frame,
    text="Clear",
    width=12,
    bg="#F39C12",
    fg="white",
    font=("Arial", 11, "bold"),
    command=clear
)

clear_btn.grid(row=1, column=0, pady=15)


exit_btn = tk.Button(
    button_frame,
    text="Exit",
    width=12,
    bg="#E74C3C",
    fg="white",
    font=("Arial", 11, "bold"),
    command=root.destroy
)

exit_btn.grid(row=1, column=1)


# -------------------------------
# Footer
# -------------------------------
footer = tk.Label(
    root,
    text="Machine Learning Project using K-Means Clustering",
    bg="#F4F6F9",
    fg="gray",
    font=("Arial", 10)
)

footer.pack(side="bottom", pady=10)


root.mainloop()