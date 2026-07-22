"""
OptiCrop: Smart Agricultural Production Optimization Engine
Data Collection, EDA, and Pre-processing
"""

import pandas as pd
import numpy as np

pd.set_option('max_colwidth', 20)
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', 50)

import matplotlib.pyplot as plt
import seaborn as sns
plt.style.use('fivethirtyeight')
plt.rcParams['figure.figsize'] = (12, 8)

from sklearn.cluster import KMeans
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, classification_report

# -----------------------------
# 1. Read the Dataset
# -----------------------------
# Dataset source: https://www.kaggle.com/datasets/chitrakumari25/smart-agricultural-production-optimizing-engine
data = pd.read_csv('Crop_recommendation.csv')
print(data.head())
print(data.info())
print(data.describe())

df = data.rename(columns={
    'N': 'nitrogen',
    'P': 'phosphorous',
    'K': 'potassium'
})

# -----------------------------
# 2. Univariate Analysis
# -----------------------------
fig, axes = plt.subplots(2, 4, figsize=(16, 8))
cols = ['nitrogen', 'phosphorous', 'potassium', 'temperature', 'humidity', 'ph', 'rainfall']
for i, col in enumerate(cols):
    ax = axes[i // 4][i % 4]
    sns.histplot(df[col], kde=True, ax=ax)
    ax.set_title(f'Ratio of {col.capitalize()}')
plt.suptitle('Distribution of agricultural conditions')
plt.tight_layout()
plt.savefig('univariate_analysis.png')
plt.close()

# -----------------------------
# 3. Bivariate Analysis
# -----------------------------
plt.figure(figsize=(10, 8))
sns.scatterplot(x=df['humidity'], y=df['label'])
plt.title('Humidity vs Crop Label')
plt.savefig('bivariate_analysis.png')
plt.close()

# -----------------------------
# 4. Multivariate Analysis
# -----------------------------
plt.figure(figsize=(10, 6))
sns.countplot(data=df[['nitrogen', 'phosphorous', 'potassium', 'temperature', 'humidity', 'ph', 'rainfall']])
plt.savefig('multivariate_analysis.png')
plt.close()

print(df.describe())

# -----------------------------
# 5. Checking for Null Values
# -----------------------------
print("Null values per column:\n", df.isnull().sum())

# -----------------------------
# 6. Handling Outliers (IQR method, example)
# -----------------------------
def remove_outliers_iqr(dataframe, column):
    Q1 = dataframe[column].quantile(0.25)
    Q3 = dataframe[column].quantile(0.75)
    IQR = Q3 - Q1
    lower = Q1 - 1.5 * IQR
    upper = Q3 + 1.5 * IQR
    return dataframe[(dataframe[column] >= lower) & (dataframe[column] <= upper)]

# Example (not applied destructively to preserve crop diversity):
# df = remove_outliers_iqr(df, 'rainfall')

# -----------------------------
# 7. Splitting Data into Train/Test Sets
# -----------------------------
x = df[['nitrogen', 'phosphorous', 'potassium', 'temperature', 'humidity', 'ph', 'rainfall']]
y = df['label']

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=0)

print("Train/Test split complete:", x_train.shape, x_test.shape)

# Save processed splits for the model-building stage
x_train.to_csv('x_train.csv', index=False)
x_test.to_csv('x_test.csv', index=False)
y_train.to_csv('y_train.csv', index=False)
y_test.to_csv('y_test.csv', index=False)
