from src.data_loader import load_data
from src.preprocessing import split_data, preprocess_data
from src.model import build_model
from src.evaluation import evaluate_model
from src.utils import setup_logger


def main():
    setup_logger()

    print("Loading data...")
    df = load_data()

    print("Splitting data...")
    X_train, X_test, y_train, y_test = split_data(df)

    print("Preprocessing data...")
    X_train, X_test = preprocess_data(X_train, X_test)

    print("Building model...")
    model = build_model()

    print("Training model...")
    model.fit(X_train, y_train)

    print("Evaluating model...")
    evaluate_model(model, X_test, y_test)

    print("\nPipeline completed successfully ✅")


if __name__ == "__main__":
    main()