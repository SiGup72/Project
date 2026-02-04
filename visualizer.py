import os
import matplotlib.pyplot as plt
import pandas as pd

def get_preference():
    print("\nDo you want to view or save plots?")
    print("1. View only")
    print("2. Save only")
    print("3. Both view and save")
    plot_choice = input("Enter your choice (1-3, default 3): ").strip() or "3"
    return plot_choice

def plot_anomalies(df, x_col, y_col, save_dir="output/anomaly", show=False, save=True):
        for col in [x_col, y_col, "anomaly"]:
            if col not in df.columns:
                raise ValueError(f"Column '{col}' not found in DataFrame")
        
        os.makedirs(save_dir, exist_ok=True)

        plt.figure()
        plt.scatter(df[x_col], df[y_col], c=df["anomaly"], cmap="coolwarm", edgecolor='k')
        plt.xlabel(x_col)
        plt.ylabel(y_col)
        plt.title(f"Anomaly Detection: {y_col} vs {x_col}")
        plt.colorbar(label="Anomaly (-1=Outlier, 1=Normal)")

        if save:
            file_path = os.path.join(save_dir, f"anomaly_{x_col}_{y_col}.png")
            plt.savefig(file_path)
            print(f"Anomaly plot saved to {file_path}")

        if show:
            plt.show()

        plt.close()
        

def plot_histogram(df, column, save_dir="output/plots", show=False, save=True):
    if column not in df.columns:   #check if column exists
        raise ValueError(f"Column '{column}' not found in DataFrame")

    if not pd.api.types.is_numeric_dtype(df[column]):  #check if column is numeric 
        print(f"Skipping histogram: '{column}' is not numeric")
        return
    
    data = df[column].dropna()

    os.makedirs(save_dir, exist_ok=True) #creates folder if it doesn't exist 

    plt.figure()
    plt.hist(data, bins=20)
    plt.title(f"Distribution of {column}")
    plt.xlabel(column)
    plt.ylabel("Frequency")

    if save:
        file_path = os.path.join(save_dir, f"{column}_histogram.png")
        plt.savefig(file_path)
        print(f"Histogram saved to {file_path}")

    if show:
        plt.show()

    plt.close()

    print(f"Histogram saved to {file_path}")

    
