import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Configuration (same as in compare_countries.ipynb for consistency)
CONFIG = {
    'countries': ['Benin', 'Sierra Leone', 'Togo'],
    'data_files': {
        'Benin': 'data/benin_clean.csv',
        'Sierra Leone': 'data/sierra_leone_clean.csv',
        'Togo': 'data/togo_clean.csv'
    },
    'metrics': ['GHI', 'DNI', 'DHI']
}

def load_cleaned_data() -> dict:
    """Load cleaned datasets for each country."""
    data = {}
    for country, file_path in CONFIG['data_files'].items():
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"Cleaned data not found at {file_path}")
        data[country] = pd.read_csv(file_path, parse_dates=['Timestamp'])
    return data

def generate_boxplot(data: dict, metric: str) -> plt.Figure:
    """Generate a boxplot for the specified metric across countries."""
    plt.figure(figsize=(10, 6))
    plot_data = []
    for country, df in data.items():
        if metric in df.columns:
            temp = df[[metric]].copy()
            temp['Country'] = country
            plot_data.append(temp)
    if plot_data:
        plot_df = pd.concat(plot_data)
        sns.boxplot(x='Country', y=metric, data=plot_df, palette='Set2')
        plt.title(f'{metric} Distribution Across Countries')
        plt.ylabel(f'{metric} (W/m²)')
        plt.xlabel('Country')
    return plt.gcf()

def compute_summary_table(data: dict) -> pd.DataFrame:
    """Compute summary table with mean, median, and SD for GHI, DNI, DHI."""
    summary = []
    for country, df in data.items():
        for metric in CONFIG['metrics']:
            if metric in df.columns:
                summary.append({
                    'Country': country,
                    'Metric': metric,
                    'Mean': df[metric].mean().round(2),
                    'Median': df[metric].median().round(2),
                    'Std': df[metric].std().round(2)
                })
    return pd.DataFrame(summary)