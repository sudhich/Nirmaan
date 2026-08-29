# 🧠 MNIST Handwritten Digit Recognition

A beginner-friendly **Deep Learning + GUI project** that recognizes handwritten digits from **0 to 9** using TensorFlow/Keras and a Tkinter graphical interface.

The user can draw a digit with the mouse, click **Predict**, and the trained model will identify the digit and display its confidence.

---

## 🎯 Project Objective

The objective of this project is to build an end-to-end **Handwritten Digit Recognition System** using the MNIST dataset.

```text
MNIST Dataset
      ↓
Data Preprocessing
      ↓
Build Neural Network
      ↓
Train Model
      ↓
Evaluate Model
      ↓
Save Model
      ↓
Tkinter GUI
      ↓
User Draws Digit
      ↓
TensorFlow Model
      ↓
Prediction
```

---

## 🛠️ Technologies Used

* **Python**
* **TensorFlow / Keras**
* **NumPy**
* **Pillow**
* **Tkinter**
* **MNIST Dataset**

---

# 📂 Project Structure

```text
MNIST_Digit_Recognition/
│
├── venv/                  # Virtual environment
│
├── train_model.py         # Train and save the model
│
├── main.py                # Tkinter GUI application
│
├── mnist_model.keras      # Trained TensorFlow model
│
├── requirements.txt       # Required Python libraries
│
└── README.md              # Project documentation
```

### File Description

| File                | Purpose                                   |
| ------------------- | ----------------------------------------- |
| `venv/`             | Isolated Python environment               |
| `train_model.py`    | Loads MNIST and trains the model          |
| `main.py`           | Provides the GUI and performs predictions |
| `mnist_model.keras` | Saved trained model                       |
| `requirements.txt`  | Contains required libraries               |
| `README.md`         | Project documentation                     |

---

# ⚙️ Setup Instructions

## Step 1: Create the Project Folder

Open Command Prompt or Terminal:

```bash
mkdir MNIST_Digit_Recognition
cd MNIST_Digit_Recognition
```

---

## Step 2: Create a Virtual Environment

Create a virtual environment named `venv`:

```bash
python -m venv venv
```

This creates an isolated Python environment for the project.

---

## Step 3: Activate the Virtual Environment

### Windows

```bash
venv\Scripts\activate
```

After activation, you should see:

```text
(venv)
```

at the beginning of your terminal prompt.


---

# 📦 Step 4: Install Required Libraries

Make sure the virtual environment is activated.

Then install the libraries from `requirements.txt`:

```bash
pip install -r requirements.txt
```

The `requirements.txt` file contains:

```text
tensorflow
numpy
pillow
```

You can also install them directly:

```bash
pip install tensorflow numpy pillow
```

---

# 🧠 Step 5: Train the Model

Run:

```bash
python train_model.py
```

The script will:

1. Load the MNIST dataset.
2. Display the dataset information.
3. Normalize pixel values.
4. Build the neural network.
5. Compile the model.
6. Train the model.
7. Evaluate the model.
8. Save the trained model.

After successful training, this file will be created:

```text
mnist_model.keras
```

---

# 💾 About `mnist_model.keras`

`mnist_model.keras` is the **trained TensorFlow/Keras model**.

It contains the learned model information needed to make predictions.

It is created automatically by:

```python
model.save("mnist_model.keras")
```

You do **not** need to create this file manually.

---

# 🖥️ Step 6: Run the GUI

After training is completed, run:

```bash
python main.py
```

The MNIST Digit Recognition GUI will open.

---

# ✏️ How to Use the Application

### Step 1 — Draw

Use your mouse to draw a digit from:

```text
0 1 2 3 4 5 6 7 8 9
```

### Step 2 — Predict

Click:

```text
Predict
```

The model will process your drawing and display the prediction.

Example:

```text
Prediction: 7
Confidence: 98.42%
```

### Step 3 — Clear

Click:

```text
Clear
```

to remove the current drawing and draw another digit.

---

# 🔄 How Prediction Works

The GUI drawing goes through several preprocessing steps:

```text
User Drawing
     ↓
280 × 280 Image
     ↓
Grayscale Image
     ↓
Resize to 28 × 28
     ↓
Convert to NumPy Array
     ↓
Normalize 0–255 → 0–1
     ↓
TensorFlow Model
     ↓
Prediction Probabilities
     ↓
Highest Probability
     ↓
Predicted Digit
```

---

# 🧠 Model Architecture

The project uses a simple neural network.

```text
Input Image
    ↓
28 × 28
    ↓
Flatten
    ↓
784 Values
    ↓
Dense Layer
128 Neurons
    ↓
ReLU
    ↓
Dense Layer
10 Neurons
    ↓
Softmax
    ↓
Digit 0–9
```

### Why 10 output neurons?

MNIST contains 10 possible classes:

```text
0, 1, 2, 3, 4, 5, 6, 7, 8, 9
```

Therefore, the output layer contains **10 neurons**.

---

# 📊 About the MNIST Dataset

MNIST is a famous handwritten digit dataset.

It contains:

* **60,000 training images**
* **10,000 testing images**
* **10 classes**
* Image size: **28 × 28 pixels**
* Grayscale images
* Pixel values: **0–255**

---

# 🔢 Image Normalization

Original MNIST pixel values are:

```text
0 to 255
```

We normalize them to:

```text
0 to 1
```

using:

```python
X_train = X_train / 255.0
X_test = X_test / 255.0
```

This helps the neural network train more effectively.

---

# 🧪 Model Training

The model is compiled using:

```python
model.compile(
    optimizer="adam",
    loss="sparse_categorical_crossentropy",
    metrics=["accuracy"]
)
```

The model is trained using:

```python
model.fit(
    X_train,
    y_train,
    epochs=10,
    batch_size=32,
    validation_split=0.2
)
```

### Important Parameters

| Parameter              | Meaning                                  |
| ---------------------- | ---------------------------------------- |
| `optimizer="adam"`     | Updates model weights during training    |
| `loss`                 | Measures prediction error                |
| `accuracy`             | Measures correct predictions             |
| `epochs=10`            | Number of complete training passes       |
| `batch_size=32`        | Images processed in each batch           |
| `validation_split=0.2` | Uses 20% of training data for validation |

---

# 🔮 Making Predictions

The GUI loads the saved model:

```python
model = tf.keras.models.load_model("mnist_model.keras")
```

Then it makes a prediction:

```python
prediction = model.predict(img_array)
```

The predicted digit is obtained using:

```python
predicted_digit = np.argmax(prediction[0])
```

---

# ▶️ Complete Run Sequence

Every time you set up the project for the first time:

```text
1. Create Project Folder
          ↓
2. Create Virtual Environment
          ↓
3. Activate Virtual Environment
          ↓
4. Install Requirements
          ↓
5. Run train_model.py
          ↓
6. mnist_model.keras is created
          ↓
7. Run main.py
          ↓
8. Draw Digit
          ↓
9. Click Predict
```

Commands:

```bash
python -m venv venv
```

```bash
venv\Scripts\activate
```

```bash
pip install -r requirements.txt
```

```bash
python train_model.py
```

```bash
python main.py
```

---

# 🎓 Learning Outcomes

After completing this project, students will understand:

* What image classification is
* What MNIST is
* How to load datasets using TensorFlow
* Image preprocessing
* Image normalization
* Neural network architecture
* Flatten layer
* Dense layer
* ReLU activation
* Softmax activation
* Model compilation
* Model training
* Model evaluation
* Model prediction
* Saving a trained model
* Loading a trained model
* Creating a Tkinter GUI
* Connecting a Deep Learning model to a GUI
* Using a virtual environment

---

# 🚀 Future Improvements

The project can be improved by:

* Replacing the Dense network with a **CNN**
* Improving the drawing canvas
* Adding prediction probabilities for all digits
* Adding an image upload option
* Adding prediction history
* Improving the GUI design
* Adding a **Save Drawing** feature
* Creating a Windows `.exe` application

---

# 🔑 Key Takeaway

This project demonstrates how a Deep Learning model can be converted into a practical application:

```text
          Deep Learning
                +
             TensorFlow
                +
              Tkinter
                ↓
     Handwritten Digit Recognition
```

The project follows a complete **AI application development workflow**:

```text
Data
 ↓
Preprocessing
 ↓
Model
 ↓
Training
 ↓
Evaluation
 ↓
Saving
 ↓
GUI
 ↓
Prediction
```

---

## 👨‍💻 Project Information

**Project Name:** MNIST Handwritten Digit Recognition

**Domain:** Deep Learning / Image Classification

**Framework:** TensorFlow / Keras

**GUI:** Tkinter

**Dataset:** MNIST

**Language:** Python
