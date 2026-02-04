import pandas as pd 
from sklearn.ensemble import IsolationForest
def analyze_missing(df):   #detailed missing values analysis
    return df.isnull().sum()

def analyze_distribution(df):  #statistical distribution analysis
    return df.describe()

def basic_analysis(df):   #overall analysis
    analysis = {
        "rows": df.shape[0],
        "columns": df.shape[1],
        "missing_values": df.isnull().sum(),
        "description": df.describe()
    }
    return analysis


def detect_anomalies(df):
    # Only numeric columns
    numeric_cols = df.select_dtypes(include=["int", "float"])
    
    if numeric_cols.empty:
        print("No numeric columns for anomaly detection.")
        df["anomaly"] = 0
        return df

    model = IsolationForest(contamination=0.05, random_state=42)
    df["anomaly"] = model.fit_predict(numeric_cols)
    return df

def get_anomalies(df):
    if "anomaly" not in df.columns:
        raise ValueError("Anomaly column not found. Run detect_anomalies first.")
    return df[df["anomaly"] == -1]

