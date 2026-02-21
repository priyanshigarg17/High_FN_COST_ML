# src/model.py

from sklearn.linear_model import LogisticRegression
from config.config import CLASS_WEIGHTS, RANDOM_STATE

def build_model():
    model = LogisticRegression(
        class_weight=CLASS_WEIGHTS,
        max_iter=1000,
        random_state=RANDOM_STATE
    )
    return model