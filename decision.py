def decide_next_steps(schema):
    actions = []

    if any(v > 0 for v in schema["missing"].values()):
        actions.append("analyze_missing")

    numeric_cols = [
        col for col, dtype in schema["dtypes"].items()
        if "int" in dtype or "float" in dtype
    ]

    if len(numeric_cols) > 0:
        actions.append("analyze_distribution")

    return actions


