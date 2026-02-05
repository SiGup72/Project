import matplotlib.pyplot as plt
import pandas as pd

def plot_histogram(df, column):
    if column not in df.columns:
        return None

    if not pd.api.types.is_numeric_dtype(df[column]):
        return None

    data = df[column].dropna()

    fig, ax = plt.subplots(figsize=(3, 2))
    ax.hist(data, bins=20)
    ax.set_title(f"{column}", fontsize=9)
    ax.set_xlabel(column, fontsize=8)
    ax.set_ylabel("Freq", fontsize=8)
    ax.tick_params(axis="both", labelsize=7)
    fig.tight_layout()

    return fig




def plot_anomalies(df, x_col, y_col):
    if any(col not in df.columns for col in [x_col, y_col, "anomaly"]):
        return None

    fig, ax = plt.subplots(figsize=(4, 3))
    scatter = ax.scatter(
        df[x_col],
        df[y_col],
        c=df["anomaly"],
        cmap="coolwarm",
        s=18,              # smaller points
        edgecolor="k"
    )

    ax.set_xlabel(x_col, fontsize=8)
    ax.set_ylabel(y_col, fontsize=8)
    ax.set_title("Anomaly Detection", fontsize=9)
    ax.tick_params(axis="both", labelsize=7)
    fig.colorbar(scatter, ax=ax, shrink=0.8)
    fig.tight_layout()

    return fig
