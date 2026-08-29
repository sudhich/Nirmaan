import tkinter as tk
from tkinter import messagebox

import numpy as np
import tensorflow as tf
from PIL import Image, ImageDraw


# Load trained MNIST model
model = tf.keras.models.load_model("mnist_model.keras")


# Create main window
root = tk.Tk()
root.title("MNIST Digit Recognition")
root.geometry("500x650")
root.resizable(False, False)


# Title
title_label = tk.Label(
    root,
    text="MNIST Digit Recognition",
    font=("Arial", 24, "bold")
)
title_label.pack(pady=20)


# Instructions
instruction_label = tk.Label(
    root,
    text="Draw a digit from 0 to 9",
    font=("Arial", 14)
)
instruction_label.pack(pady=5)


# Canvas
canvas = tk.Canvas(
    root,
    width=280,
    height=280,
    bg="black",
    cursor="cross"
)
canvas.pack(pady=20)


# Create PIL image
image = Image.new("L", (280, 280), 0)
draw = ImageDraw.Draw(image)


# Drawing function
def draw_digit(event):
    x = event.x
    y = event.y

    brush_size = 18

    # Draw on Tkinter canvas
    canvas.create_oval(
        x - brush_size,
        y - brush_size,
        x + brush_size,
        y + brush_size,
        fill="white",
        outline="white"
    )

    # Draw on PIL image
    draw.ellipse(
        [
            x - brush_size,
            y - brush_size,
            x + brush_size,
            y + brush_size
        ],
        fill=255
    )


# Connect mouse movement to drawing
canvas.bind("<B1-Motion>", draw_digit)


# Prediction function
def predict_digit():

    # Resize image from 280x280 to 28x28
    img = image.resize((28, 28))

    # Convert image to NumPy array
    img_array = np.array(img)

    # Normalize pixel values
    img_array = img_array / 255.0

    # Add batch dimension
    img_array = img_array.reshape(1, 28, 28)

    # Make prediction
    prediction = model.predict(img_array, verbose=0)

    # Get predicted digit
    predicted_digit = np.argmax(prediction[0])

    # Get confidence
    confidence = prediction[0][predicted_digit] * 100

    # Display result
    result_label.config(
        text=f"Prediction: {predicted_digit}\n"
             f"Confidence: {confidence:.2f}%"
    )


# Clear function
def clear_canvas():

    # Clear Tkinter canvas
    canvas.delete("all")

    # Reset PIL image
    draw.rectangle(
        [0, 0, 280, 280],
        fill=0
    )

    # Reset result
    result_label.config(
        text="Prediction: -\nConfidence: -"
    )


# Buttons frame
button_frame = tk.Frame(root)
button_frame.pack(pady=10)


# Predict button
predict_button = tk.Button(
    button_frame,
    text="Predict",
    font=("Arial", 14, "bold"),
    width=12,
    command=predict_digit
)
predict_button.grid(row=0, column=0, padx=10)


# Clear button
clear_button = tk.Button(
    button_frame,
    text="Clear",
    font=("Arial", 14, "bold"),
    width=12,
    command=clear_canvas
)
clear_button.grid(row=0, column=1, padx=10)


# Result label
result_label = tk.Label(
    root,
    text="Prediction: -\nConfidence: -",
    font=("Arial", 18, "bold")
)
result_label.pack(pady=25)


# Start application
root.mainloop()