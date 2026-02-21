# src/preprocessing.py

from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler

from config.config import TARGET_COLUMN, TEST_SIZE, RANDOM_STATE


def split_data(df):
    X = df.drop(columns=[TARGET_COLUMN])
    y = df[TARGET_COLUMN]

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=TEST_SIZE,
        stratify=y,
        random_state=RANDOM_STATE
    )

    return X_train, X_test, y_train, y_test


def preprocess_data(X_train, X_test):
    # Numerical pipeline
    num_pipeline = Pipeline(
        steps=[
            ("imputer", SimpleImputer(strategy="median")),
            ("scaler", StandardScaler())
        ]
    )

    # Fit only on training data
    X_train_processed = num_pipeline.fit_transform(X_train)

    # Transform test data
    X_test_processed = num_pipeline.transform(X_test)

    return X_train_processed, X_test_processed