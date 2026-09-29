
# ============================================================
# Sentiment Analysis Web Application
# ============================================================

import os
import joblib
import streamlit as st


# ============================================================
# 1. PATHS
# ============================================================

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

MODEL_PATH = os.path.join(BASE_DIR, "model.pkl")
VECTORIZER_PATH = os.path.join(BASE_DIR, "vectorizer.pkl")


# ============================================================
# 2. LOAD MODEL AND VECTORIZER
# ============================================================

model = joblib.load(MODEL_PATH)
vectorizer = joblib.load(VECTORIZER_PATH)


# ============================================================
# 3. PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="Sentiment Analysis",
    page_icon="😊",
    layout="centered"
)


# ============================================================
# 4. TITLE
# ============================================================

st.title("😊 Sentiment Analysis Application")

st.write(
    "Enter a sentence or comment below and the model will "
    "predict its sentiment."
)


# ============================================================
# 5. USER INPUT
# ============================================================

comment = st.text_area(
    "Enter your comment:",
    placeholder="Example: I really enjoyed this product!",
    height=150
)


# ============================================================
# 6. PREDICTION BUTTON
# ============================================================

if st.button("Predict Sentiment"):

    if comment.strip() == "":
        st.warning("Please enter a comment.")

    else:

        # Convert text into TF-IDF features
        comment_tfidf = vectorizer.transform([comment])

        # Make prediction
        prediction = model.predict(comment_tfidf)[0]

        # Get prediction probability
        probabilities = model.predict_proba(comment_tfidf)[0]

        confidence = max(probabilities) * 100


        # ====================================================
        # SENTIMENT LABEL
        # ====================================================

        # IMPORTANT:
        # Verify the actual meaning of 0, 1 and 2
        # from your dataset before final deployment.

        sentiment_labels = {
            0: "Negative",
            1: "Neutral",
            2: "Positive"
        }

        sentiment = sentiment_labels.get(
            prediction,
            str(prediction)
        )


        # ====================================================
        # DISPLAY RESULT
        # ====================================================

        st.subheader("Prediction")

        if sentiment == "Positive":

            st.success(f"😊 Positive")

        elif sentiment == "Negative":

            st.error(f"😞 Negative")

        elif sentiment == "Neutral":

            st.info(f"😐 Neutral")

        else:

            st.write(f"Sentiment: {sentiment}")


        # ====================================================
        # CONFIDENCE
        # ====================================================

        st.write(f"**Confidence:** {confidence:.2f}%")

        st.progress(int(confidence))
