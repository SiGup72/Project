import pandas as pd

from schema import extract_schema
from memory import has_schema, get_from_memory, save_to_memory
from decision import decide_next_steps
from analyzer import basic_analysis, analyze_missing, analyze_distribution, detect_anomalies, get_anomalies
from visualizer import plot_histogram, plot_anomalies,get_preference


def main():
    df = pd.read_csv("titanic.csv")
    schema = extract_schema(df)
    schema_id = hash(str(schema))

    if has_schema(schema_id):
        print("Using cached insights")
        insights = get_from_memory(schema_id)

    else:
        print("New dataset schema detected")
        insights = {}

        print("\nSelect analysis type:")
        print("1. Overall analysis")
        print("2. Missing values only")
        print("3. Distribution only")
        print("4. Anomaly detection only")
        print("5. Run all analyses")
        choice = input("Enter your choice (1-5): ").strip()

        actions = []

        if choice == "1":
            actions = ["basic_analysis"]
        elif choice == "2":
            actions = ["analyze_missing"]
        elif choice == "3":
            actions = ["analyze_distribution"]
        elif choice == "4":
            actions = ["anomaly_detection"]
        elif choice == "5":
            actions = ["basic_analysis", "analyze_missing", "analyze_distribution", "anomaly_detection"]
        else:
            print("Invalid choice. Running all analyses by default.")
            actions = ["basic_analysis", "analyze_missing", "analyze_distribution", "anomaly_detection"]

        #conditional analysis
        if "basic_analysis" in actions:
            insights["basic"] = basic_analysis(df)

        if "analyze_missing" in actions:
            insights["missing"] = analyze_missing(df)

        if "analyze_distribution" in actions:
            insights["distribution"] = analyze_distribution(df)
            numeric_cols = df.select_dtypes(include=["int", "float"]).columns
            plot_choice=get_preference()
            SHOW_PLOTS = plot_choice in ["1", "3"]   #show plots if 1 or 3
            SAVE_PLOTS = plot_choice in ["2", "3"]   #save plots if 2 or 3
            for col in numeric_cols:
                plot_histogram(df, col, show=SHOW_PLOTS, save=SAVE_PLOTS)

        if "anomaly_detection" in actions:
            df = detect_anomalies(df)
            anomalies = get_anomalies(df)
            print(anomalies)
            insights["anomalies"] = df["anomaly"].value_counts().to_dict()
            plot_choice=get_preference()
            SHOW_PLOTS = plot_choice in ["1", "3"]   #show plots if 1 or 3
            SAVE_PLOTS = plot_choice in ["2", "3"]   #save plots if 2 or 3
            plot_anomalies(df, x_col="Age", y_col="Fare", show=SHOW_PLOTS, save=SAVE_PLOTS)

        save_to_memory(schema_id, insights)

    print("\nAgent Insights:")  #summary
    for key, value in insights.items():
        print(f"\n--- {key.upper()} ---")
        print(value)


if __name__ == "__main__":
    main()
