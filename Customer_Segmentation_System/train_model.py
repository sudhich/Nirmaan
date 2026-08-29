"""
=========================================================
Customer Segmentation System
Train K-Means Model
Author : Sudhiram Chauhan
=========================================================
"""

import pandas as pd
import matplotlib.pyplot as plt
import joblib
from pathlib import Path

from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score


BASE_DIR = Path(__file__).resolve().parent
DATASET_PATH = BASE_DIR / "Mall_Customers.csv"


# =========================================================
# 1. Load Dataset
# =========================================================
print("=" * 60)
print("Loading Dataset...")
print("=" * 60)

df = pd.read_csv(DATASET_PATH)

print("\nFirst 5 Rows:\n")
print(df.head())

print("\nDataset Shape :", df.shape)

print("\nDataset Information:\n")
print(df.info())

print("\nMissing Values:\n")
print(df.isnull().sum())


# =========================================================
# 2. Data Preprocessing
# =========================================================

# Encode Gender. The original dataset names this column "Genre".
gender_column = "Gender" if "Gender" in df.columns else "Genre"
df["Gender"] = df[gender_column].map({
    "Male": 1,
    "Female": 0
})

# Features
features = [
    "Age",
    "Gender",
    "Annual Income (k$)",
    "Spending Score (1-100)"
]

X = df[features]


# =========================================================
# 3. Feature Scaling
# =========================================================
print("\nScaling Features...")

scaler = StandardScaler()

X_scaled = scaler.fit_transform(X)


# =========================================================
# 4. Elbow Method
# =========================================================
print("\nFinding Optimal Number of Clusters...")

wcss = []

for k in range(1, 11):

    model = KMeans(
        n_clusters=k,
        random_state=42,
        n_init=10
    )

    model.fit(X_scaled)

    wcss.append(model.inertia_)


plt.figure(figsize=(8,5))
plt.plot(range(1,11), wcss, marker="o")
plt.title("Elbow Method")
plt.xlabel("Number of Clusters")
plt.ylabel("WCSS")
plt.grid(True)
plt.savefig(BASE_DIR / "elbow_method.png", bbox_inches="tight")
plt.close()


# =========================================================
# 5. Train Final Model
# =========================================================
print("\nTraining K-Means Model...")

kmeans = KMeans(
    n_clusters=5,
    random_state=42,
    n_init=10
)

kmeans.fit(X_scaled)


# =========================================================
# 6. Assign Cluster Labels
# =========================================================
df["Cluster"] = kmeans.labels_


# =========================================================
# 7. Model Evaluation
# =========================================================
score = silhouette_score(
    X_scaled,
    kmeans.labels_
)

print("\nSilhouette Score :", round(score,3))


# =========================================================
# 8. Cluster Summary
# =========================================================
print("\nCluster Counts\n")

print(df["Cluster"].value_counts().sort_index())


print("\nCluster Centers (Scaled Data)\n")

print(kmeans.cluster_centers_)


# =========================================================
# 9. Save Model
# =========================================================
joblib.dump(kmeans, BASE_DIR / "model.pkl")
joblib.dump(scaler, BASE_DIR / "scaler.pkl")
joblib.dump(features, BASE_DIR / "features.pkl")

print("\nModel Saved Successfully.")

print("model.pkl")
print("scaler.pkl")
print("features.pkl")


# =========================================================
# 10. Visualize Clusters
# =========================================================

plt.figure(figsize=(8,6))

plt.scatter(
    df["Annual Income (k$)"],
    df["Spending Score (1-100)"],
    c=df["Cluster"],
    cmap="rainbow",
    s=70
)

plt.xlabel("Annual Income (k$)")
plt.ylabel("Spending Score")
plt.title("Customer Segments")

plt.grid(True)
plt.savefig(BASE_DIR / "customer_segments.png", bbox_inches="tight")
plt.close()


# =========================================================
# Training Completed
# =========================================================
print("\n" + "=" * 60)
print("K-Means Training Completed Successfully")
print("=" * 60)