
import streamlit as st
import numpy as np
import pandas as pd

from sklearn.linear_model import LinearRegression

# --------------------------------
# 1. Page Configuration
# --------------------------------
st.set_page_config(
    page_title="Student Performance Predictor",
    page_icon="🎓",
    layout="centered"
)

# --------------------------------
# 2. Train ML Model
# --------------------------------
@st.cache_resource
def train_model():

    np.random.seed(42)

    # Generate sample training data
    study_hours = np.random.uniform(0, 10, 500)
    attendance = np.random.uniform(40, 100, 500)
    previous_marks = np.random.uniform(20, 100, 500)

    # Simulated exam marks
    exam_marks = (
        study_hours * 4
        + attendance * 0.2
        + previous_marks * 0.5
        + np.random.normal(0, 5, 500)
    )

    exam_marks = np.clip(exam_marks, 0, 100)

    X = pd.DataFrame({
        "Study Hours": study_hours,
        "Attendance": attendance,
        "Previous Marks": previous_marks
    })

    y = exam_marks

    model = LinearRegression()
    model.fit(X, y)

    return model


model = train_model()

# --------------------------------
# 3. Application UI
# --------------------------------
st.title("🎓 Student Performance Predictor")

st.write(
    "Predict expected exam marks using "
    "Machine Learning."
)

st.divider()

# Student details
student_name = st.text_input(
    "Enter Student Name"
)

study_hours = st.slider(
    "Daily Study Hours",
    min_value=0.0,
    max_value=10.0,
    value=4.0,
    step=0.5
)

attendance = st.slider(
    "Attendance Percentage",
    min_value=0,
    max_value=100,
    value=75
)

previous_marks = st.number_input(
    "Previous Exam Marks",
    min_value=0.0,
    max_value=100.0,
    value=70.0
)

# --------------------------------
# 4. Prediction
# --------------------------------
if st.button("Predict Performance"):

    input_data = pd.DataFrame({
        "Study Hours": [study_hours],
        "Attendance": [attendance],
        "Previous Marks": [previous_marks]
    })

    prediction = model.predict(input_data)[0]

    prediction = np.clip(prediction, 0, 100)

    st.subheader("Prediction Result")

    st.write("Student:", student_name or "Student")

    st.metric(
        "Expected Exam Marks",
        f"{prediction:.2f}/100"
    )

    if prediction >= 75:
        st.success("Excellent Performance")
    elif prediction >= 50:
        st.info("Average Performance")
    else:
        st.warning("Needs Improvement")

    # Display input summary
    st.subheader("Student Details")

    st.dataframe(
        input_data,
        use_container_width=True
    )

    st.progress(int(prediction))

    st.caption(
        "This is a demonstration model trained on "
        "synthetic sample data. Predictions are not "
        "validated for real student outcomes."
    )
