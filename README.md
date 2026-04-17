# fraud-detection-app

# 💳 Credit Card Fraud Detection App

## 🚀 Live Demo

🔗 [https://your-link.streamlit.app](https://fraud-detection-app-mifvbksouxdxed2xbk7hme.streamlit.app/)

---

## 📌 Problem Statement

Credit card fraud is a critical issue in the financial industry. The goal of this project is to build a machine learning model that can accurately identify fraudulent transactions from a highly imbalanced dataset.

---

## 📊 Dataset

* Total Records: **284,807 transactions**
* Features: **30 (Time, Amount, V1–V28)**
* Target Variable:

  * `0` → Non-Fraud
  * `1` → Fraud

---

## ⚙️ Approach

### 🔹 Data Preprocessing

* Handled missing values (if any)
* Feature scaling using **StandardScaler**
* Addressed class imbalance using **SMOTE**

### 🔹 Model Building

Implemented multiple classification models:

* Logistic Regression
* Decision Tree
* Random Forest (Best Performing)
* Gradient Boosting
* XGBoost

---

## 📈 Model Evaluation

Due to class imbalance, accuracy alone is not reliable. So we used:

* Precision
* Recall
* F1-score
* ROC-AUC Score

### ✅ Final Model Performance (Random Forest)

* Recall: **0.84** (High fraud detection ability)
* Precision: **0.21**
* ROC-AUC Score: **0.97**

---

## 🌐 Deployment

The model is deployed using **Streamlit Cloud**, allowing users to input transaction details and get real-time predictions.

---

## 🖥️ Features

* Simple user interface
* Real-time fraud prediction
* Lightweight and fast
* Cloud deployed

---

## ⚠️ Note

The original dataset contains anonymized features (V1–V28) generated using PCA.
For demonstration purposes, the app uses simplified inputs (Time and Amount), while the actual model relies on all features for accurate predictions.

---

## 🛠️ Tech Stack

* Python
* Scikit-learn
* Pandas & NumPy
* Streamlit
* GitHub

---

## 📂 Project Structure

```
fraud-detection-app/
│
├── app.py
├── fraud_model.pkl
├── requirements.txt
└── README.md
```

---

## 🎯 Key Learnings

* Handling imbalanced datasets
* Model evaluation beyond accuracy
* End-to-end ML project development
* Deploying ML models using Streamlit

---

## 👨‍💻 Author

**Swagath Reddy**

---

## ⭐ If you like this project

Give it a ⭐ on GitHub!
