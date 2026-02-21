import os

# Project name
PROJECT_NAME = "high-fn-cost-ml"

# Folder structure
folders = [
    f"{PROJECT_NAME}/data",
    f"{PROJECT_NAME}/notebooks",
    f"{PROJECT_NAME}/src",
    f"{PROJECT_NAME}/config",
    f"{PROJECT_NAME}/artifacts",
    f"{PROJECT_NAME}/logs",
]

# Files to create
files = [
    # Data
    f"{PROJECT_NAME}/data/disease_detection_high_FN_cost_dataset.csv",

    # Notebooks
    f"{PROJECT_NAME}/notebooks/eda.ipynb",

    # Source code
    f"{PROJECT_NAME}/src/__init__.py",
    f"{PROJECT_NAME}/src/data_loader.py",
    f"{PROJECT_NAME}/src/preprocessing.py",
    f"{PROJECT_NAME}/src/model.py",
    f"{PROJECT_NAME}/src/evaluation.py",
    f"{PROJECT_NAME}/src/utils.py",

    # Config
    f"{PROJECT_NAME}/config/__init__.py",
    f"{PROJECT_NAME}/config/config.py",

    # Root files
    f"{PROJECT_NAME}/main.py",
    f"{PROJECT_NAME}/requirements.txt",
    f"{PROJECT_NAME}/README.md",
]

def create_structure():
    # Create folders
    for folder in folders:
        os.makedirs(folder, exist_ok=True)
        print(f"Folder created: {folder}")

    # Create files
    for file in files:
        with open(file, "w", encoding="utf-8") as f:
            pass
        print(f"File created: {file}")

    print("\nProject structure created successfully ✅")

if __name__ == "__main__":
    create_structure()