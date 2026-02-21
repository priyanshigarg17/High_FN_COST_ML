
# 🏥 High FN Cost Disease Detection Model

## 📌 Problem Statement

In many real-world classification problems such as **medical diagnosis**, missing a positive case can be significantly more costly than incorrectly flagging a negative one.

In this project:

* False Negative (FN) cost is assumed to be **10x higher** than False Positive (FP).
* The objective is to design a model that prioritizes **Recall for the positive class** (disease cases).
* The focus is to reduce missed disease cases while maintaining a reasonable balance in predictions.

---

## 📊 Dataset Overview

The dataset represents a simulated medical screening scenario.

**Target Variable:**
`disease_present`

* `1` → Disease
* `0` → No Disease

**Features include:**

* Age
* Blood Pressure
* Cholesterol
* BMI
* Smoking History
* Family History

The dataset is **imbalanced**, with fewer positive cases (~15%).

---

## 🎯 Objective

Since False Negatives are 10x more costly:

* The model should aggressively minimize FN.
* Recall for the positive class becomes the primary metric.
* Accuracy is not considered a reliable evaluation metric in this case.

---

## 🧠 Approach

### 1️⃣ Cost-Sensitive Learning

Higher class weight assigned to the positive class to penalize FN heavily.

### 2️⃣ Custom Decision Threshold

Instead of the default 0.5 threshold, a custom threshold was used to increase sensitivity and reduce missed disease cases.

### 3️⃣ Focused Evaluation Strategy

Model evaluation emphasizes:

* Confusion Matrix
* Recall (Positive Class)
* Precision-Recall trade-off

Accuracy is not used as the primary metric due to class imbalance and asymmetric cost.

---

## 📈 Results Summary

The final model achieved:

* High Recall (~93%) for disease cases
* Very low False Negatives
* Increased False Positives (expected trade-off)

This behavior aligns with the business objective of minimizing missed diagnoses.

---

## ⚖️ Trade-off Discussion

Improving recall comes at the cost of increased false positives.

In medical systems:

* Missing a disease case can be life-threatening.
* Additional screening for healthy patients is often acceptable.

Thus, the model intentionally prioritizes safety over strict precision.

---

## 🏗 Project Structure

```
high-fn-cost-ml/
│
├── data/
├── notebooks/
├── src/
├── config/
├── artifacts/
├── logs/
│
├── main.py
├── requirements.txt
└── README.md
```

---

## 💡 Key Learnings

* Accuracy can be misleading in imbalanced datasets.
* Cost-sensitive learning is crucial in high-risk domains.
* Decision threshold tuning significantly impacts FN/FP trade-off.
* Business context must guide model evaluation.

---

## 🚀 Future Improvements

* Automated threshold optimization
* Precision-Recall curve visualization
* Cross-validation with cost-based scoring
* Model comparison (Logistic Regression vs XGBoost)
* Deployment-ready API


