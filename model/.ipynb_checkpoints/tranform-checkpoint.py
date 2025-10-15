# preprocessing.py

def encode_columns(X):
    X = X.copy()
    X['Gender'] = X['Gender'].map({'Male': 1, 'Female': 0})
    X['AutoimmuneMarker'] = X['AutoimmuneMarker'].map({'Yes': 1, 'No': 0})
    return X
