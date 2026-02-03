# DATA ANALYSIS AGENT
## 🔍Overview
This project implements a Python-based Data Analysis Agent that automates Exploratory Data Analysis (EDA) for tabular datasets. At its core, the agent analyzes a given dataset by compressing the dataset schema and storing analysis insights, instead of repeatedly working on raw data or full analysis history.
The agent autonomously:
- Understands the structure of the dataset
- Decides which EDA steps to perform
- Stores insights in memory
- Avoids redundant analysis
The entire system is built using pure Python and lightweight data analysis libraries.
## 🎯Motivation
I am a 2nd-year Data Science student looking to strengthen my fundamentals by building practical, real-world projects instead of relying only on notebooks or tutorials. While learning data analysis, I noticed that exploratory analysis is often:
- Repetitive
- Manual
- Inefficient when reused across datasets

This project was chosen to:
- Practice clean Python project structure
- Understand how autonomous systems work
- Build a reusable and extensible data analysis pipeline
- Explore how intelligent agents can assist in data analysis without heavy AI/ML models
## ⚙️Features
- Automatically summarizes the structure of a dataset (columns, data types, missing values)
- Stores analysis results so the same checks are not repeated
- Uses simple rule-based logic to decide which EDA step to run next
- Identifies missing values in the dataset
- Analyzes data distributions and detects outliers
- Generates visualizations using matplotlib and seaborn
- Built with a clean, modular, and easy-to-extend Python code structure
## 🧠How the Agent works
The data analysis agent follows a structured workflow:
Dataset (CSV)
     ↓
Schema Compression
     ↓
Check Agent Memory
     ↓
Decision Engine
     ↓
EDA Analysis
     ↓
Store Insights
     ↓
Plots & Summary
   
This approach makes the agent efficient, stateful, and reusable.

## Project Structure
## Libraries and Tools used
## Dataset
## How to run
## Extensibility
## License 
