# config/config.py

DATA_PATH = "data/disease_detection_high_FN_cost_dataset.csv"
TARGET_COLUMN = "disease_present"

TEST_SIZE = 0.2
RANDOM_STATE = 42

# Cost-sensitive learning
CLASS_WEIGHTS = {0: 1, 1: 7}

# Custom threshold (to reduce FN)
THRESHOLD = 0.5