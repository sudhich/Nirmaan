"""
=========================================================
Customer Segmentation System
Utility Functions
Author : Sudhiram Chauhan
=========================================================
"""

import joblib
import numpy as np
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent


# =========================================================
# Load Saved Model
# =========================================================
def load_model():
    """
    Load the trained K-Means model and StandardScaler.
    """

    model = joblib.load(BASE_DIR / "model.pkl")
    scaler = joblib.load(BASE_DIR / "scaler.pkl")

    return model, scaler


# =========================================================
# Predict Customer Segment
# =========================================================
def predict_customer_segment(model, scaler,
                             age,
                             gender,
                             income,
                             spending_score):
    """
    Predict the customer cluster.
    """

    # Create input array
    customer = np.array([
        [
            age,
            gender,
            income,
            spending_score
        ]
    ])

    # Scale input
    customer_scaled = scaler.transform(customer)

    # Predict cluster
    cluster = model.predict(customer_scaled)[0]

    return int(cluster)


# =========================================================
# Business Recommendation
# =========================================================
def get_business_recommendation(cluster):
    """
    Return customer type and business strategy.
    """

    recommendations = {

        0: (
            "Budget Customer",
            """• Offer Discount Coupons
• Promote Budget Products
• Seasonal Sale Notifications"""
        ),

        1: (
            "Regular Customer",
            """• Loyalty Rewards Program
• Personalized Email Offers
• Cashback Benefits"""
        ),

        2: (
            "Premium Customer",
            """• VIP Membership
• Premium Services
• Exclusive Event Invitations"""
        ),

        3: (
            "High Income, Low Spending",
            """• Personalized Recommendations
• Premium Product Demonstrations
• Limited-Time Exclusive Offers"""
        ),

        4: (
            "High Spending Customer",
            """• Luxury Products
• Early Access to New Collections
• Premium Customer Support"""
        )

    }

    return recommendations.get(
        cluster,
        (
            "Unknown Customer",
            "No recommendation available."
        )
    )


# =========================================================
# Display Cluster Information
# =========================================================
def display_cluster_info(cluster):
    """
    Print customer details in console.
    """

    customer_type, recommendation = get_business_recommendation(cluster)

    print("=" * 50)
    print("Predicted Cluster :", cluster)
    print("Customer Type     :", customer_type)
    print("\nBusiness Recommendation")
    print(recommendation)
    print("=" * 50)


# =========================================================
# Test Module
# =========================================================
if __name__ == "__main__":

    try:
        model, scaler = load_model()

        print("Model loaded successfully.")

        cluster = predict_customer_segment(
            model,
            scaler,
            age=25,
            gender=1,
            income=60,
            spending_score=75
        )

        display_cluster_info(cluster)

    except FileNotFoundError:
        print("Error: model.pkl or scaler.pkl not found.")
        print("Run train_model.py first.")