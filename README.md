# tamigo-hr-calculator

streamlit_kpi_app/
├── .gitattributes                # Git behavior settings for text files, diffing, etc.
├── .gitignore                    # Files and folders Git should ignore
├── app.py                        # Entry point for the Streamlit app
├── requirements.txt              # Dependencies for the project
├── README.md                     # Project documentation
├── .streamlit/
│   └── config.toml               # Streamlit-specific configuration (e.g., theme)
├── data/                         # (Optional) For sample or static input files
│   └── sample_input.xlsx         
├── kpi_engine/                   # Python package for data processing & KPI calculation
│   ├── __init__.py
│   ├── file_loader.py            # Logic to load and validate Excel files
│   └── kpi_calculator.py         # Contains functions to calculate KPIs
└── utils/
    ├── __init__.py
    └── helpers.py                # Reusable helper functions (e.g., formatting)
