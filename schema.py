import pandas as pd

def extract_schema(df):
    schema = {
        "columns": df.columns.tolist(),
        "dtypes": df.dtypes.astype(str).to_dict(),
        "missing": df.isnull().sum().to_dict(),
        "row_count": len(df),
        "column_count": df.shape[1]
    }
    return schema
