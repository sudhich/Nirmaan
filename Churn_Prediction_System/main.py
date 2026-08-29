# ============================================================
# Customer Churn Prediction System
# GUI Application
# ============================================================

import subprocess
import sys
from pathlib import Path
import pandas as pd
import tkinter as tk
from tkinter import messagebox, ttk

from utils import (
    load_model as load_saved_model,
    load_accuracy as load_saved_accuracy,
    predict_customer,
    prediction_text,
    validate_inputs,
)

# ============================================================
# Global Variables
# ============================================================

model = None

BASE_DIR = Path(__file__).resolve().parent
#print(f"BASE_DIR: {BASE_DIR}")
CSV_FILE = BASE_DIR / "customer_churn.csv"
#print(f"CSV_FILE: {CSV_FILE}")
MODEL_FILE = BASE_DIR / "model.pkl"
ACCURACY_FILE = BASE_DIR / "accuracy.pkl"

# ============================================================
# Create Main Window
# ============================================================

root = tk.Tk()
root.title("Customer Churn Prediction System")
root.geometry("700x650")
root.configure(bg="#F1EDEC")
root.resizable(True, True)

# ============================================================
# Title
# ============================================================

title = tk.Label(
    root,
    text="Customer Churn Prediction System",
    font=("Arial", 22, "bold"),
    bg="#ECF0F1",
    fg="#2C3E50",
)
title.pack(pady=20)

# ============================================================
# Main Frame
# ============================================================

frame = tk.Frame(root, bg="white", relief="groove", bd=2)
frame.pack(padx=20, pady=10, fill="both", expand=True)

# ============================================================
# Variables
# ============================================================

age_var = tk.StringVar()
purchase_var = tk.StringVar()
manager_var = tk.StringVar()
years_var = tk.StringVar()
sites_var = tk.StringVar()
location_var = tk.StringVar()
company_var = tk.StringVar()

# ============================================================
# Input Fields
# ============================================================

tk.Label(frame, text="Age", font=("Arial", 12), bg="white").grid(
    row=0, column=0, padx=20, pady=10, sticky="w"
)
age_entry = tk.Entry(frame, textvariable=age_var, width=35, font=("Arial", 11))
age_entry.grid(row=0, column=1, pady=10)

# ------------------------------------------------------------

tk.Label(frame, text="Total Purchase", font=("Arial", 12), bg="white").grid(
    row=1, column=0, padx=20, pady=10, sticky="w"
)
purchase_entry = tk.Entry(frame, textvariable=purchase_var, width=35, font=("Arial", 11))
purchase_entry.grid(row=1, column=1)

# ------------------------------------------------------------

tk.Label(frame, text="Account Manager", font=("Arial", 12), bg="white").grid(
    row=2, column=0, padx=20, pady=10, sticky="w"
)
manager_combo = ttk.Combobox(
    frame,
    textvariable=manager_var,
    values=["0", "1"],
    width=32,
    state="readonly",
)
manager_combo.grid(row=2, column=1)

# ------------------------------------------------------------

tk.Label(frame, text="Years", font=("Arial", 12), bg="white").grid(
    row=3, column=0, padx=20, pady=10, sticky="w"
)
years_entry = tk.Entry(frame, textvariable=years_var, width=35, font=("Arial", 11))
years_entry.grid(row=3, column=1)

# ------------------------------------------------------------

tk.Label(frame, text="Number of Sites", font=("Arial", 12), bg="white").grid(
    row=4, column=0, padx=20, pady=10, sticky="w"
)
sites_entry = tk.Entry(frame, textvariable=sites_var, width=35, font=("Arial", 11))
sites_entry.grid(row=4, column=1)

# ------------------------------------------------------------

tk.Label(frame, text="Location", font=("Arial", 12), bg="white").grid(
    row=5, column=0, padx=20, pady=10, sticky="w"
)
location_combo = ttk.Combobox(frame, textvariable=location_var, width=32)
location_combo.grid(row=5, column=1)

# ------------------------------------------------------------

tk.Label(frame, text="Company", font=("Arial", 12), bg="white").grid(
    row=6, column=0, padx=20, pady=10, sticky="w"
)
company_combo = ttk.Combobox(frame, textvariable=company_var, width=32)
company_combo.grid(row=6, column=1)

# ============================================================
# Buttons
# ============================================================

button_frame = tk.Frame(frame, bg="white")
button_frame.grid(row=7, column=0, columnspan=2, pady=30)

train_btn = tk.Button(
    button_frame,
    text="Train Model",
    width=15,
    bg="orange",
    fg="white",
    font=("Arial", 11, "bold"),
)
train_btn.grid(row=0, column=0, padx=10)

predict_btn = tk.Button(
    button_frame,
    text="Predict Churn",
    width=15,
    bg="green",
    fg="white",
    font=("Arial", 11, "bold"),
)
predict_btn.grid(row=0, column=1, padx=10)

clear_btn = tk.Button(button_frame, text="Clear", width=12)
clear_btn.grid(row=0, column=2, padx=10)

exit_btn = tk.Button(button_frame, text="Exit", width=12)
exit_btn.grid(row=0, column=3, padx=10)

# ============================================================
# Status Labels
# ============================================================

status_label = tk.Label(
    root,
    text="Status : Model Not Trained",
    font=("Arial", 12, "bold"),
    fg="red",
    bg="#ECF0F1",
)
status_label.pack()

accuracy_label = tk.Label(root, text="Accuracy : --", font=("Arial", 12), bg="#ECF0F1")
accuracy_label.pack(pady=5)

prediction_label = tk.Label(
    root,
    text="Prediction : --",
    font=("Arial", 15, "bold"),
    fg="blue",
    bg="#ECF0F1",
)
prediction_label.pack(pady=20)

# ============================================================
# Helper Functions
# ============================================================

def update_status(message, color="red"):
    status_label.config(text=message, fg=color)


def load_model_from_file():
    global model

    try:
        model = load_saved_model(str(MODEL_FILE))
    except Exception as exc:
        update_status("Status : Error Loading Model", "red")
        messagebox.showerror("Error", str(exc))
        return False

    if model is not None:
        update_status("Status : Model Loaded Successfully", "green")
        try:
            accuracy = load_saved_accuracy(str(ACCURACY_FILE))
            if accuracy is not None:
                accuracy_label.config(text=f"Accuracy : {accuracy:.4f}")
            else:
                accuracy_label.config(text="Accuracy : --")
        except Exception:
            accuracy_label.config(text="Accuracy : --")
        return True

    update_status("Status : Model Not Found", "red")
    accuracy_label.config(text="Accuracy : --")
    return False


def train_model():
    global model

    try:
        result = subprocess.run(
            [sys.executable, str(BASE_DIR / "train_model.py")],
            cwd=str(BASE_DIR),
            capture_output=True,
            text=True,
            check=False,
        )

        if result.returncode == 0:
            if load_model_from_file():
                messagebox.showinfo("Training Complete", "Model trained successfully.")
            else:
                messagebox.showerror("Training Error", "The model file could not be loaded.")
        else:
            error_text = result.stderr.strip() or result.stdout.strip() or "Unknown training error."
            update_status("Status : Training Failed", "red")
            messagebox.showerror("Training Error", error_text)

    except Exception as exc:
        update_status("Status : Training Failed", "red")
        messagebox.showerror("Error", str(exc))


def predict_churn():
    global model

    if model is None:
        if not load_model_from_file():
            messagebox.showwarning("Model", "Please train/load the model first.")
            return

    try:
        age = float(age_var.get())
        purchase = float(purchase_var.get())
        account_manager = int(manager_var.get())
        years = float(years_var.get())
        sites = float(sites_var.get())
        location = location_var.get()
        company = company_var.get()
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numeric values.")
        return

    if not validate_inputs(age_var.get(), purchase_var.get(), years_var.get(), sites_var.get()):
        messagebox.showerror("Input Error", "Please enter valid numeric values.")
        return

    if not location or not company:
        messagebox.showerror("Input Error", "Please select a location and company.")
        return

    prediction, confidence = predict_customer(
        model,
        age,
        purchase,
        account_manager,
        years,
        sites,
        location,
        company,
    )

    label_text = f"Prediction : {prediction_text(prediction)}\nConfidence : {confidence:.2f}%"
    if prediction == 1:
        prediction_label.config(text=label_text, fg="red")
    else:
        prediction_label.config(text=label_text, fg="green")


def clear_fields():
    age_var.set("")
    purchase_var.set("")
    years_var.set("")
    sites_var.set("")

    manager_combo.current(0)

    if len(location_combo["values"]) > 0:
        location_combo.current(0)

    if len(company_combo["values"]) > 0:
        company_combo.current(0)

    prediction_label.config(text="Prediction : --", fg="blue")
    accuracy_label.config(text="Accuracy : --")


def exit_program():
    answer = messagebox.askyesno("Exit", "Are you sure you want to exit?")
    if answer:
        root.destroy()


# ============================================================
# Load Dataset & Populate Controls
# ============================================================

try:
    df = pd.read_csv(CSV_FILE)
    df = df.dropna()

    location_list = sorted(df["Location"].astype(str).unique().tolist())
    location_combo["values"] = location_list
    if len(location_list) > 0:
        location_combo.current(0)

    company_list = sorted(df["Company"].astype(str).unique().tolist())
    company_combo["values"] = company_list
    if len(company_list) > 0:
        company_combo.current(0)

    manager_combo["values"] = ["0", "1"]
    manager_combo.current(0)

except FileNotFoundError:
    messagebox.showerror("File Error", f"Dataset '{CSV_FILE.name}' not found.")
except Exception as exc:
    messagebox.showerror("Error", str(exc))

# ============================================================
# Bind Buttons
# ============================================================

train_btn.config(command=train_model)
predict_btn.config(command=predict_churn)
clear_btn.config(command=clear_fields)
exit_btn.config(command=exit_program)

# ============================================================
# Load Model at Startup
# ============================================================

load_model_from_file()

# ============================================================
# Run Application
# ============================================================

root.mainloop()
