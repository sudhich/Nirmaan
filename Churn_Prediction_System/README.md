# Customer Churn Prediction System

A Machine Learning desktop application developed using **Python**, **Scikit-learn**, and **Tkinter** to predict whether a customer is likely to leave (churn) or stay with a company.

---

## Project Overview

Customer churn prediction helps businesses identify customers who are likely to stop using their services. By predicting churn in advance, companies can take preventive actions to improve customer retention.

This project demonstrates a complete End-to-End Machine Learning workflow including:

- Data Loading
- Data Preprocessing
- Feature Engineering
- Model Training
- Model Evaluation
- Model Saving
- Desktop GUI using Tkinter
- Customer Churn Prediction

---

## Machine Learning Workflow

```
Customer_Churn.csv
        │
        ▼
Load Dataset
        │
        ▼
Data Cleaning
        │
        ▼
Feature Selection
        │
        ▼
Encoding
        │
        ▼
Train/Test Split
        │
        ▼
Logistic Regression
        │
        ▼
Model Evaluation
        │
        ▼
Save Model
        │
        ▼
GUI Prediction
```

---

## Dataset

**Dataset Name**

Customer_Churn.csv

### Features

| Feature | Description |
|----------|-------------|
| Names | Customer Name |
| Age | Customer Age |
| Total_Purchase | Total Purchase Amount |
| Account_Manager | Whether an Account Manager is Assigned |
| Years | Number of Years as Customer |
| Num_Sites | Number of Sites Used |
| Onboard_date | Customer Onboarding Date |
| Location | Customer Location |
| Company | Company Name |
| Churn | Target Variable |

---

## Machine Learning Algorithm

- Logistic Regression
                
---

## Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Joblib
- Tkinter
- Matplotlib

---

## Project Structure

```
Customer_Churn_Prediction/
│
├── Customer_Churn.csv
├── main.py
├── train_model.py
├── utils.py
├── model.pkl
├── features.pkl
├── accuracy.pkl
├── requirements.txt
└── README.md
```

---


### Install Required Libraries

Step:1
pip install -r requirements.txt
Step:2
python main.py


---

## GUI Features

- Train Model
- Predict Customer Churn
- Load Saved Model
- Input Validation
- Prediction Confidence
- Clear Inputs
- Exit Application

---

## Evaluation Metrics

The model is evaluated using:

- Accuracy
- Precision
- Recall
- F1 Score
- Confusion Matrix

---

## Sample Prediction

Input:

```
Age = 45
Total Purchase = 12000
Account Manager = 1
Years = 6
Number of Sites = 8
```

Output:

```
Prediction:
Customer Will Churn

Confidence:
91.45%
```

---

## Learning Outcomes

After completing this project, students will be able to:

- Understand Customer Churn Prediction
- Perform Data Preprocessing
- Handle Categorical Variables
- Build a Classification Model
- Evaluate Machine Learning Models
- Save and Load Trained Models
- Develop a Desktop GUI using Tkinter

---

## Future Improvements

- Random Forest Classifier
- XGBoost Classifier
- Feature Importance Visualization
- ROC Curve
- Dashboard with Charts
- Prediction History
- Export Prediction Report
- Dark Mode GUI

---

## Author

**Sudhiram Chauhan**

AI Trainer | Machine Learning Engineer | Data Scientist

---

## License

This project is developed for educational purposes.