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
```
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
```
This approach makes the agent efficient, stateful, and reusable.

## 📂Project Structure
```
eda-agent/
│
├── titanic.csv      # Example dataset used for demonstration
│
├── main.py          # Entry point – runs the agent and handles user menu 
├── schema.py        # Extracts dataset schema: column names, types, missing values
├── memory.py        # Stores insights in memory to avoid redundant analysis
├── decision.py      # Rule-based logic to decide which analysis to run
├── analyzer.py      # Analysis functions: overall stats, missing values, distributions, anomalies
├── visualizer.py    # Plotting and visualization
│
├── output/
│   └── plots/       # Histograms of numeric columns
|   └── anomaly/     # Scatter plots highlighting anomalies
│
├── requirements.txt
└── README.md
```

## 📦Libraries and Tools used
- **pandas** (schema.py, analyzer.py)
  - Used for loading datasets, column-wise analysis, missing value detection, and statistics.
- **numpy**  (schema.py)
  - Used for numerical computations such as skewness and range calculations.
- **matplotlib/seaborn** (visualizer.py)
  - Used for generating and saving EDA visualizations.
- **Python (3.12.10)**
  - Core language used to build the agent logic and workflow.

## 📊Dataset
- **Dataset Name:** Titanic – Machine Learning from Disaster
- **Source:** Kaggle
- **Type:** Tabular data (CSV)
- **Target Variable:** Survived
### The dataset contains a mix of:
- Numerical features (Age, Fare, etc.)
- Categorical features (Sex, Embarked, etc.)
- Missing values
  
## 🚀How to run
1. Install dependencies
   ```bash
   pip install -r requirements.txt
   ```
2. Run the agent 
   ```bash
   py main.py
   ```

## 📈 Example Output
- Identification of missing values in columns like Age and Cabin
- Detection of skewed distributions (e.g., Fare)
- Outlier identification in numerical features
- Automatically generated plots saved in the outputs/plots/ directory
- Stored insights to avoid re-running the same analysis
  
## 🧪Extensibility
This project can be extended by:
- Adding correlation analysis
- Supporting multiple datasets dynamically
- Connecting to LLM-based systems for natural language insight generation
- Adding anomaly detection or lightweight ML models

## 📜License 
MIT License

