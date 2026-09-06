# Real-Time Face Detection using OpenCV

## 📌 Project Overview

This project detects human faces in real time using a webcam.

It uses:

* Python
* OpenCV
* Haar Cascade Classifier
* Webcam

When a face is detected, a rectangle is drawn around the face.

---

## 📂 Project Structure

```text
Real_Time_Face_Detection/
│
├── venv/
│
├── main.py
│
├── haarcascade_frontalface_default.xml
│
└── requirements.txt
```

---

## 🛠️ Technologies Used

| Technology   | Purpose              |
| ------------ | -------------------- |
| Python       | Programming language |
| OpenCV       | Computer Vision      |
| Haar Cascade | Face detection       |
| Webcam       | Input video          |

---

## ⚙️ Setup
# Install
https://github.com/opencv/opencv/blob/4.x/data/haarcascades/haarcascade_frontalface_default.xml?utm_source=chatgpt.com
### Step 1: Create virtual environment

Open the VS Code terminal:

```bash
python -m venv venv
```

### Step 2: Activate virtual environment

#### Windows PowerShell

```powershell
.\venv\Scripts\Activate.ps1
```

#### Windows Command Prompt

```cmd
venv\Scripts\activate
```

After activation, you should see:

```text
(venv)
```

---

## 📦 Install Dependencies

Run:

```bash
pip install -r requirements.txt
```

Or:

```bash
pip install opencv-python
```

---

## ▶️ Run the Project

Make sure the virtual environment is activated.

Run:

```bash
python main.py
```
# If error
python -c "import cv2; print(cv2.__version__); print(hasattr(cv2, 'CascadeClassifier'))"
## output:
4.10.0
True
# Unstall
python -m pip uninstall opencv-python -y
# Install
python -m pip install opencv-python==4.10.0.84
The webcam window will open.



The program will detect faces and draw rectangles around them.

---

## 🛑 Stop the Program

Press:

```text
q
```

on the keyboard.

---

## 🧠 How It Works

```text
Webcam
   ↓
Capture Frame
   ↓
Convert BGR → Grayscale
   ↓
Haar Cascade Classifier
   ↓
Detect Faces
   ↓
Draw Rectangle
   ↓
Display Frame
```

---

## 🔍 Important OpenCV Functions

### `cv2.VideoCapture(0)`

Opens the default webcam.

```python
cap = cv2.VideoCapture(0)
```

---

### `cap.read()`

Reads a frame from the webcam.

```python
ret, frame = cap.read()
```

* `ret` → whether the frame was successfully captured
* `frame` → captured image

---

### `cv2.cvtColor()`

Converts the image from BGR to grayscale.

```python
gray = cv2.cvtColor(
    frame,
    cv2.COLOR_BGR2GRAY
)
```

---

### `detectMultiScale()`

Detects faces in the image.

```python
faces = face_cascade.detectMultiScale(
    gray,
    scaleFactor=1.1,
    minNeighbors=5
)
```

---

### `cv2.rectangle()`

Draws a rectangle around each detected face.

```python
cv2.rectangle(
    frame,
    (x, y),
    (x + w, y + h),
    (255, 0, 0),
    2
)
```

---

### `cv2.imshow()`

Displays the webcam frame.

```python
cv2.imshow(
    "Real-Time Face Detection",
    frame
)
```

---

### `cv2.waitKey()`

Waits for keyboard input.

```python
cv2.waitKey(1)
```

We use it to detect the `q` key.

---

## 📄 Haar Cascade File

The project uses:

```text
haarcascade_frontalface_default.xml
```

This is a pretrained Haar Cascade model for detecting frontal human faces.

Keep the XML file in the same directory as `main.py`.

---

## ⚠️ Troubleshooting

### Camera not opening

If you see:

```text
ERROR: Cannot access webcam!
```

Check:

1. Your webcam is connected.
2. No other application is using the webcam.
3. Windows camera permissions allow Python/VS Code to access the camera.

You can also try:

```python
cap = cv2.VideoCapture(1)
```

instead of:

```python
cap = cv2.VideoCapture(0)
```

---

### Haar Cascade not found

If you see:

```text
ERROR: Haar Cascade file not found!
```

make sure this file exists:

```text
haarcascade_frontalface_default.xml
```

and is located beside:

```text
main.py
```

---

### OpenCV not installed

Activate `venv` first:

```powershell
.\venv\Scripts\Activate.ps1
```

Then:

```bash
pip install opencv-python
```

---

## 🎯 Learning Outcomes

After completing this project, you will understand:

* What Computer Vision is
* How OpenCV works
* How to access a webcam
* Image-to-grayscale conversion
* Haar Cascade face detection
* Bounding boxes
* Real-time video processing
* Python virtual environments
* OpenCV basic functions

---

## 🚀 Future Improvements

This project can be extended with:

* Eye detection
* Smile detection
* Face recognition
* Multiple face tracking
* Attendance system
* Age and gender detection
* Deep-learning-based face detection

---

## 👨‍💻 Author

**Sudhiram Chauhan**

Project: **Real-Time Face Detection using OpenCV**
