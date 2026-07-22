"""
OptiCrop: Model Building
- K-Means Clustering (pattern discovery)
- Logistic Regression (crop classification)
- Model evaluation and saving the best model
"""

import pandas as pd
import numpy as np
import pickle
import matplotlib.pyplot as plt

from sklearn.cluster import KMeans
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix

# -----------------------------
# Load pre-processed data
# -----------------------------
x_train = pd.read_csv('x_train.csv')
x_test = pd.read_csv('x_test.csv')
y_train = pd.read_csv('y_train.csv').squeeze()
y_test = pd.read_csv('y_test.csv').squeeze()

x = pd.concat([x_train, x_test])
df = pd.concat([x, pd.concat([y_train, y_test])], axis=1)
df = df.rename(columns={0: 'label'})

# -----------------------------
# 1. K-Means Clustering (Elbow Method)
# -----------------------------
wcss = []
for i in range(1, 11):
    km = KMeans(n_clusters=i, init="k-means++", max_iter=300, n_init=10, random_state=0)
    km.fit(x)
    wcss.append(km.inertia_)

plt.plot(range(1, 11), wcss)
plt.title("The Elbow method", fontsize=20)
plt.xlabel("No of clusters")
plt.ylabel("wcss")
plt.savefig("elbow_method.png")
plt.close()

# Train K-Means with chosen k (based on elbow graph)
km = KMeans(n_clusters=4, init="k-means++", max_iter=300, n_init=10, random_state=0)
y_means = km.fit_predict(x)

z = pd.concat([pd.DataFrame(y_means), df['label'].reset_index(drop=True)], axis=1)
z = z.rename(columns={0: 'cluster'})

print("Crops in First cluster:", z[z['cluster'] == 0]['label'].unique())
print("Crops in Second cluster:", z[z['cluster'] == 1]['label'].unique())
print("Crops in Third cluster:", z[z['cluster'] == 2]['label'].unique())
print("Crops in Fourth cluster:", z[z['cluster'] == 3]['label'].unique())

# -----------------------------
# 2. Logistic Regression
# -----------------------------
model = LogisticRegression(max_iter=1000)
model.fit(x_train, y_train)
y_pred = model.predict(x_test)

# -----------------------------
# 3. Evaluate Model Performance
# -----------------------------
cr = classification_report(y_test, y_pred)
print(cr)

cm = confusion_matrix(y_test, y_pred)
print("Confusion Matrix:\n", cm)

accuracy = model.score(x_test, y_test)
print(f"Model Accuracy: {accuracy:.4f}")

# -----------------------------
# 4. Save the Best Model
# -----------------------------
with open("model.pkl", "wb") as f:
    pickle.dump(model, f)

print("Model saved as model.pkl")

# -----------------------------
# 5. Predict Best Crop for Given Parameters
# -----------------------------
sample = np.array([[105, 35, 40, 25, 64, 7, 100]])
prediction = model.predict(sample)
print("The suggested crop for given climatic condition is:", prediction)
