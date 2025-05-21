import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from utils import load_cleaned_data, generate_boxplot, compute_summary_table

# Streamlit app configuration
st.set_page_config(page_title="Solar Potential Dashboard", layout="wide")

# Title and description
st.title("Solar Potential Dashboard")
st.markdown("Explore solar potential (GHI, DNI, DHI) in Benin, Sierra Leone, and Togo with interactive visualizations.")

# Configuration
CONFIG = {
    'countries': ['Benin', 'Sierra Leone', 'Togo'],
    'data_files': {
        'Benin': '../data/benin_clean.csv',
        'Sierra Leone': '../data/sierraleone_clean.csv',
        'Togo': '../data/togo_clean.csv'
    },
    'metrics': ['GHI', 'DNI', 'DHI']
}

# Sidebar for user inputs
st.sidebar.header("Select Options")
selected_countries = st.sidebar.multiselect(
    "Select Countries", CONFIG['countries'], default=CONFIG['countries']
)
selected_metric = st.sidebar.selectbox("Select Metric for Boxplot", CONFIG['metrics'], index=0)

# Load data
try:
    data = load_cleaned_data()
except FileNotFoundError as e:
    st.error(f"Error: {str(e)}")
    st.stop()

# Filter data for selected countries
filtered_data = {country: df for country, df in data.items() if country in selected_countries}

# Display boxplot
if filtered_data and selected_metric:
    st.subheader(f"{selected_metric} Distribution Across Selected Countries")
    fig = generate_boxplot(filtered_data, selected_metric)
    st.pyplot(fig)
else:
    st.warning("Please select at least one country and a valid metric.")

# Display summary table (top regions by GHI)
st.subheader("Summary Table: Top Countries by GHI")
summary_table = compute_summary_table(data)
ghi_summary = summary_table[summary_table['Metric'] == 'GHI'].sort_values('Mean', ascending=False)
st.dataframe(ghi_summary, use_container_width=True)

# Footer
st.markdown("---")
st.markdown("Built with Streamlit | Data sourced from local CSV files")
