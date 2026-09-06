import cv2


# ==========================================
# 1. Load Haar Cascade
# ==========================================

face_cascade = cv2.CascadeClassifier(
    "haarcascade_frontalface_default.xml"
)


# Check Haar Cascade
if face_cascade.empty():
    print("ERROR: Haar Cascade file not found!")
    exit()


# ==========================================
# 2. Open Webcam
# ==========================================

cap = cv2.VideoCapture(0)


# Check Webcam
if not cap.isOpened():
    print("ERROR: Cannot access webcam!")
    exit()


print("================================")
print(" Real-Time Face Detection")
print("================================")
print("Webcam started...")
print("Press 'q' to quit.")


# ==========================================
# 3. Real-Time Detection
# ==========================================

while True:

    # Read webcam frame
    ret, frame = cap.read()

    if not ret:
        print("ERROR: Cannot read webcam.")
        break


    # ======================================
    # 4. Convert BGR → Grayscale
    # ======================================

    gray = cv2.cvtColor(
        frame,
        cv2.COLOR_BGR2GRAY
    )


    # ======================================
    # 5. Detect Faces
    # ======================================

    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30)
    )


    # ======================================
    # 6. Draw Rectangle
    # ======================================

    for (x, y, w, h) in faces:

        cv2.rectangle(
            frame,
            (x, y),
            (x + w, y + h),
            (255, 0, 0),
            2
        )


    # ======================================
    # 7. Display Face Count
    # ======================================

    cv2.putText(
        frame,
        f"Faces: {len(faces)}",
        (20, 40),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0, 255, 0),
        2
    )


    # ======================================
    # 8. Display Webcam
    # ======================================

    cv2.imshow(
        "Real-Time Face Detection",
        frame
    )


    # ======================================
    # 9. Press Q to Exit
    # ======================================

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break


# ==========================================
# 10. Release Resources
# ==========================================

cap.release()

cv2.destroyAllWindows()

print("Webcam stopped.")