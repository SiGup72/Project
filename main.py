from schema import extract_schema
from memory import has_schema, get_from_memory, save_to_memory
from decision import decide_next_steps
from analyzer import (
    basic_analysis,
    analyze_missing,
    analyze_distribution,
    detect_anomalies,
    get_anomalies
)
from visualizer import plot_histogram, plot_anomalies

def run_eda_agent(df):
    results = {}
    schema = extract_schema(df)
    schema_id = hash(str(schema))

    if has_schema(schema_id):
        results["cached"] = True
        return get_from_memory(schema_id)

    results["schema"] = schema
    actions = decide_next_steps(schema)

    if "analyze_missing" in actions:
        results["missing"] = analyze_missing(df)

    if "analyze_distribution" in actions:
        results["distribution"] = analyze_distribution(df)
        figs = []
        for col in df.select_dtypes(include=["int", "float"]).columns:
            fig = plot_histogram(df, col)
            if fig:
                figs.append(fig)
        results["histograms"] = figs

    df = detect_anomalies(df)
    if "anomaly" in df.columns:
        results["anomalies"] = df["anomaly"].value_counts().to_dict()
        fig = plot_anomalies(df, x_col="Age", y_col="Fare")
        results["anomaly_plot"] = fig

    save_to_memory(schema_id, results)
    return results
