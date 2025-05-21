# Scripts

## Overview

The `scripts` directory contains supporting files and documentation for the Streamlit dashboard application located in the `app/` directory. The dashboard visualizes solar potential data (GHI, DNI, DHI) from Benin, Sierra Leone, and Togo, with interactive features for exploring insights.

## Purpose

This directory serves to:

- Document the development process and usage instructions for the Streamlit dashboard.
- Support the `app/` directory by providing a centralized location for related scripts and documentation.

## Directory Structure

- `README.md`: This file, providing documentation for the Streamlit dashboard development and usage.
- `__init__.py`: Marks this directory as a Python package (empty).

## Streamlit Dashboard Development Process

The Streamlit dashboard was developed to meet the following objectives:

1. **Interactive Visualization**: Create an intuitive interface to explore solar potential data (GHI, DNI, DHI) across Benin, Sierra Leone, and Togo.
2. **Modular Code**: Separate data processing and visualization logic into `app/utils.py` for reusability.
3. **User Engagement**: Implement interactive widgets (e.g., country and metric selectors) to allow dynamic exploration of data.
4. **Clean Design**: Use Streamlit and Seaborn for a professional, visually appealing interface.

### Development Steps

1. **Branch Creation**: Created a `dashboard-dev` branch for development.
2. **Folder Structure**:
   - Added `app/` with `main.py` (Streamlit app) and `utils.py` (data processing and visualization functions).
   - Added `scripts/` with this `README.md` for documentation.
3. **Implementation**:
   - `app/main.py`: Built the Streamlit app with a country selector, metric selector, GHI boxplot, and a summary table ranking countries by average GHI.
   - `app/utils.py`: Defined functions for loading data, generating boxplots, and creating a summary table.
4. **Testing**: Ran the app locally to verify functionality using `streamlit run app/main.py`.
5. **Git Hygiene**:
   - Ensured `data/` is ignored in `.gitignore`.
   - Committed changes with the message: `feat: basic Streamlit UI`.
6. **Deployment**: Prepared instructions for deployment to Streamlit Community Cloud.
