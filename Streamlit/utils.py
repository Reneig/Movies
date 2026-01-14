import streamlit as st
from pathlib import Path
import pandas as pd

# Define the output directory
BASE_DIR = Path(__file__).resolve().parent.parent
OUTPUT_DIR = BASE_DIR / "Data_visualization" / "output"

# Function to load data with caching
@st.cache_data
def load_parquet_data(file_name):
    """
    Loads a parquet file from the predefined output directory.
    Uses Streamlit caching to optimize performance.
    """
    file_path = OUTPUT_DIR / file_name
    return pd.read_parquet(file_path)