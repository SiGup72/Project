import streamlit as st
import pandas as pd
from main import run_eda_agent

st.set_page_config(page_title="EDA Agent", layout="wide")

st.title("📊 EDA Agent")
st.write("Upload a CSV file to perform automated exploratory data analysis.")

uploaded_file = st.file_uploader("Upload CSV", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)

    st.subheader("Dataset Preview")
    st.dataframe(df.head())

    if st.button("Run EDA"):
        with st.spinner("Analyzing dataset..."):
            results = run_eda_agent(df)

        st.success("Analysis complete!")

        # ---------------- Schema ----------------
        if "schema" in results:
            st.subheader("Schema")
            st.json(results["schema"])

        # ---------------- Missing ----------------
        if "missing" in results:
            st.subheader("Missing Values")
            st.write(results["missing"])

        # ---------------- Statistics ----------------
        if "distribution" in results:
            st.subheader("Statistical Summary")
            st.write(results["distribution"])

        # ---------------- Histograms ----------------
        if "histograms" in results:
            st.subheader("Distributions")

            for fig in results["histograms"]:
                left, center, right = st.columns([1, 2, 1])
                with center:
                    st.pyplot(fig, use_container_width=False)

        # ---------------- Anomalies ----------------
        if "anomalies" in results:
            st.subheader("Anomaly Summary")
            st.write(results["anomalies"])

        if results.get("anomaly_plot"):
            st.subheader("Anomaly Visualization")
            left, center, right = st.columns([1, 2, 1])
            with center:
                st.pyplot(results["anomaly_plot"], use_container_width=False)
