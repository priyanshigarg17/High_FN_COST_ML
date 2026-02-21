# src/evaluation.py

import numpy as np
from sklearn.metrics import classification_report, confusion_matrix, recall_score
from config.config import THRESHOLD

def evaluate_model(model, X_test, y_test):
    y_prob = model.predict_proba(X_test)[:, 1]

    # Custom threshold
    y_pred = np.where(y_prob >= THRESHOLD, 1, 0)

    print("\nConfusion Matrix:")
    print(confusion_matrix(y_test, y_pred))

    print("\nClassification Report:")
    print(classification_report(y_test, y_pred))

    recall = recall_score(y_test, y_pred)
    print(f"\nRecall (Focus Metric): {recall:.4f}")