# Solar Data Discovery Challenge (B5W0)

This repository contains the code and documentation for the 10 Academy Solar Data Discovery Challenge (Batch 5, Week 0). The project analyzes solar farm data from Benin, Sierra Leone, and Togo to assess solar potential through exploratory data analysis (EDA), data cleaning, cross-country comparisons, and an interactive Streamlit dashboard.

## Project Overview

The challenge consists of three main tasks and an optional bonus task:

-   **Task 1: Data Profiling** - Perform exploratory data analysis on individual country datasets to understand distributions, missing values, and patterns in solar metrics (GHI, DNI, DHI, etc.).
-   **Task 2: Data Cleaning** - Clean the datasets by handling missing values, outliers, and inconsistencies to prepare them for analysis.
-   **Task 3: Cross-Country Comparison** - Compare solar potential metrics (GHI, DNI, DHI) across Benin, Sierra Leone, and Togo using visualizations, statistical tests, and summary statistics.
-   **Bonus: Interactive Dashboard** - Develop a Streamlit dashboard to visualize insights interactively, with widgets for country and metric selection.

## Repository Structure


solar-challenge-week1/
├── Notebooks/
│ ├── benin_eda.ipynb # EDA and cleaning for Benin dataset
│ ├── sierraleone_eda.ipynb # EDA and cleaning for Sierra Leone dataset
│ ├── togo_eda.ipynb # EDA and cleaning for Togo dataset
│ ├── compare_countries.ipynb # Cross-country comparison of solar metrics
│ └── README.md # Documentation for Notebooks folder
├── app/
│ ├── init.py # Marks app/ as a Python package
│ ├── main.py # Main Streamlit application script
│ └── utils.py # Utility functions for data processing and visualization
├── data/ # Ignored in .gitignore
│ ├── benin_clean.csv # Cleaned dataset for Benin
│ ├── sierra_leone_clean.csv # Cleaned dataset for Sierra Leone
│ └── togo_clean.csv # Cleaned dataset for Togo
├── scripts/
│ ├── init.py # Marks scripts/ as a Python package
│ └── README.md # Documentation for Streamlit dashboard
├── .gitignore # Ignores data/ and other unnecessary files
└── requirements.txt # Python dependencies

## Setup Instructions

### Prerequisites

-   **Python**: Version 3.9 or higher (3.13.3 recommended).
-   **Git**: For cloning the repository.
-   **Virtualenv**: For creating an isolated Python environment.
-   **Datasets**: Cleaned CSV files (`benin_clean.csv`, `sierra_leone_clean.csv`, `togo_clean.csv`) in the `data/` directory.

### Steps to Reproduce

1.  **Clone the Repository**:
    ```bash
    git clone https://github.com/Eyoab11/solar-challenge-week1.git
    cd solar-challenge-week1
    ```

2.  **Set Up a Virtual Environment**:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3.  **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4.  **Prepare Datasets**:
    Place the cleaned datasets (`benin_clean.csv`, `sierra_leone_clean.csv`, `togo_clean.csv`) in the `data/` directory.
    *Note: The `data/` directory is ignored in `.gitignore` to avoid committing large or sensitive data files.*

5.  **Run the Project**:

    *   **Run Notebooks**:
        Start Jupyter Notebook:
        ```bash
        jupyter notebook
        ```
        Open and execute notebooks in the `Notebooks/` folder:
        `benin_eda.ipynb`, `sierraleone_eda.ipynb`, `togo_eda.ipynb` for Tasks 1 and 2 (EDA and cleaning).
        `compare_countries.ipynb` for Task 3 (cross-country comparison).

    *   **Run Streamlit Dashboard**:
        Launch the Streamlit app:
        ```bash
        streamlit run app/main.py
        ```
        Open the provided URL (e.g., `http://localhost:8501`) in a web browser.

## Tasks and Outputs

### Task 1: Data Profiling

-   **Notebooks**: `benin_eda.ipynb`, `sierraleone_eda.ipynb`, `togo_eda.ipynb`
-   **Objective**: Perform exploratory data analysis on each country's dataset to analyze solar metrics (GHI, DNI, DHI, etc.).
-   **Outputs**:
    -   Summary statistics (mean, median, standard deviation, etc.).
    -   Visualizations (e.g., time series, histograms, correlation heatmaps, wind rose plots).
    -   Missing value reports and data quality checks.
-   **Location**: Visualizations saved in `data/plots/` (e.g., `benin_ghi_timeseries.png`).

### Task 2: Data Cleaning

-   **Notebooks**: `benin_eda.ipynb`, `sierraleone_eda.ipynb`, `togo_eda.ipynb`
-   **Objective**: Clean datasets by handling missing values, outliers, and inconsistencies.
-   **Outputs**:
    -   Cleaned CSV files saved as `data/benin_clean.csv`, `data/sierra_leone_clean.csv`, `data/togo_clean.csv`.
    -   Documentation of cleaning steps in notebook Markdown cells.

### Task 3: Cross-Country Comparison

-   **Notebook**: `compare_countries.ipynb`
-   **Objective**: Compare GHI, DNI, and DHI across Benin, Sierra Leone, and Togo.
-   **Outputs**:
    -   Boxplots for GHI, DNI, and DHI, saved in `data/plots/compare_countries/`.
    -   Summary table with mean, median, and standard deviation, saved as `data/plots/compare_countries/summary_table.csv`.
    -   Statistical tests (ANOVA or Kruskal-Wallis) with p-values printed in the notebook.
    -   GHI ranking bar chart (bonus), saved as `data/plots/compare_countries/ghi_ranking.png`.
    -   Key observations summarizing findings (e.g., highest GHI, variability, statistical significance).

### Bonus: Interactive Dashboard

-   **Scripts**: `app/main.py`, `app/utils.py`
-   **Objective**: Develop an interactive Streamlit dashboard to visualize solar potential data.
-   **Features**:
    -   Widgets to select countries and metrics (GHI, DNI, DHI).
    -   Boxplot of the selected metric across chosen countries.
    -   Summary table ranking countries by average GHI.
-   **Deployment**: Deployed to Streamlit Community Cloud (URL provided in `scripts/README.md`).
-   **Location**: Visualizations displayed dynamically in the Streamlit interface.

## Deployment Instructions

To deploy the Streamlit dashboard to Streamlit Community Cloud:

1.  Ensure the repository is pushed to GitHub:
    ```bash
    git push origin main
    ```
2.  Log in to [Streamlit Community Cloud](https://share.streamlit.io/).
3.  Create a new app, linking to `https://github.com/Eyoab11/solar-challenge-week1`.
4.  Specify `app/main.py` as the main script.
5.  Ensure `requirements.txt` includes:
    -   `streamlit`
    -   `pandas`
    -   `matplotlib`
    -   `seaborn`
6.  Deploy the app and access it via the provided public URL.
7.  Update `scripts/README.md` with the deployed URL.

## Git Hygiene

-   The `data/` directory is ignored in `.gitignore` to prevent committing large CSV files.
-   Commits are organized by task:
    -   `Task 3: feat: add cross-country comparison notebook`
    -   `Bonus: feat: basic Streamlit UI (on dashboard-dev branch)`
-   Pull requests are created for each task/branch to ensure clean integration.

## Contributing

To contribute to the project:

1.  Create a new branch (e.g., `git checkout -b feature/new-analysis`).
2.  Add or modify notebooks in `Notebooks/` or scripts in `app/`.
3.  Document changes in the relevant `README.md` files.
4.  Commit with descriptive messages (e.g., `git commit -m "feat: add Benin EDA notebook"`).
5.  Push the branch and create a pull request to `main`.

## Notes

-   Ensure cleaned datasets are placed in `data/` before running notebooks or the Streamlit app.
-   Outputs (e.g., plots, tables) are saved in `data/plots/` for notebooks but displayed dynamically in the Streamlit app.
-   Check `Notebooks/README.md` and `scripts/README.md` for detailed documentation of each component.

