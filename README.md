# 🌱 Smart Crop Recommendation System

An end-to-end Machine Learning project that recommends the best crop to grow based on soil nutrients and environmental conditions. This project includes data preprocessing, visualization, model training, evaluation, and deployment using Flask.

---

## 🚀 Features

- Data cleaning & preprocessing
- Outlier detection and removal (IQR method)
- Exploratory Data Analysis (EDA)
- Multiple ML models:
  - Decision Tree
  - Random Forest
  - Support Vector Machine (SVM)
  - Logistic Regression
  - K-Nearest Neighbors (KNN)
- Model evaluation using:
  - Classification Report
  - Confusion Matrix
- Model & scaler saving using `joblib`
- Web-based UI using Flask
- Real-time prediction from user input

---

## 📊 Dataset Information

- **File:** `Crop_Recommendation.csv`
- **Total Records:** 2200
- **Features:**
  - Nitrogen (N)
  - Phosphorus (P)
  - Potassium (K)
  - Temperature (°C)
  - Humidity (%)
  - pH Value
  - Rainfall (mm)
- **Target Variable:**
  - Crop Type

---

## 🔍 Exploratory Data Analysis

The project includes:

- Correlation Heatmap
- Crop Distribution Count Plot
- Histograms with KDE
- Boxplots for outlier detection

---

## 🧹 Data Cleaning

- Checked for null values
- Applied **IQR-based outlier removal**
- Recursive cleaning until no outliers remain

---

## ⚙️ Machine Learning Pipeline

1. Label Encoding of target variable
2. Train-Test Split (80/20)
3. Feature Scaling using `StandardScaler`
4. Model Training using 5 classifiers
5. Evaluation using:
   - Accuracy
   - Classification Report
   - Confusion Matrix

---

## 🤖 Models Used

| Model | Description |
|------|------------|
| Decision Tree | Simple tree-based classifier |
| Random Forest | Ensemble learning method |
| SVM | Effective for high-dimensional spaces |
| Logistic Regression | Linear classification |
| KNN | Distance-based classifier |

---

## 💾 Model Saving

- Models saved as `.pkl` files
- Scaler saved for consistent preprocessing

---

## 🌐 Flask Web Application

The project includes a Flask-based UI where users can input:

- Nitrogen
- Phosphorus
- Potassium
- Temperature
- Humidity
- pH
- Rainfall

📌 The app returns predictions from all trained models.

---

---

## 🧠 Prediction Workflow

1. User inputs values
2. Data is scaled using saved scaler
3. Each model predicts crop
4. Results are decoded using LabelEncoder
5. Predictions displayed on UI

---
