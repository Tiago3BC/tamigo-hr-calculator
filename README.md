# tamigo-hr-calculator

A Streamlit app to load Excel files, process HR data, and calculate key performance indicators (KPIs) related to employee metrics.

## Project Structure

```
streamlit_kpi_app/
├── .gitattributes              # Git behavior settings for text files, diffing, etc.
├── .gitignore                  # Files and folders Git should ignore
├── app.py                      # Entry point for the Streamlit app
├── requirements.txt            # Project dependencies
├── README.md                   # Project documentation
├── .streamlit/
│   └── config.toml             # Streamlit-specific configuration (e.g., theme)
├── data/                       # Sample or static input files
│   └── sample_input.xlsx       
├── kpi_engine/                 # Python package for data processing & KPI calculation
│   ├── __init__.py
│   └── kpi_calculator.py       # Functions to calculate KPIs
└── utils/
    ├── __init__.py
    └── helpers.py              # Reusable helper functions (e.g., formatting)
````

## Overview

This project provides an interactive web app built with Streamlit that helps HR teams and analysts to:

- Upload Excel data files easily
- Validate and clean data
- Calculate and display important HR KPIs dynamically
- Export results or use them for further analysis

## Getting Started

1. Clone the repo:

```bash
   git clone https://github.com/yourusername/tamigo-hr-calculator.git
   cd tamigo-hr-calculator/streamlit_kpi_app
````

2. Install dependencies:

```bash
   pip install -r requirements.txt
```

3. Run the app:

```bash
   streamlit run app.py
````
