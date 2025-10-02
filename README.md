# tamigo-hr-calculator

A Streamlit app to load Excel files, process HR data, and calculate key performance indicators (KPIs) related to employee metrics.

## Project Structure

```
streamlit_kpi_app/
├── .gitattributes
├── .gitignore
├── app.py                      # Entry point for the Streamlit app
├── requirements.txt
├── README.md
├── .streamlit/
│   └── config.toml             # Streamlit-specific configuration
├── data/
│   └── sample_input.xlsx
├── calculator_engine/          # Python package for data processing & calculation
│   ├── __init__.py
│   └── calculator.py           # Functions to calc HR metrics
└── utils/
    ├── __init__.py
    └── helpers.py              # Reusable helper functions
```

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
```

2. Install dependencies:

```bash
   pip install -r requirements.txt
```

3. Run the app:

```bash
   streamlit run app.py
```
