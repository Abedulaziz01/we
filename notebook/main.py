import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

from utils import load_data

st.set_page_config(page_title="Solar Dashboard", layout="wide")

st.title("☀️ Solar Potential Dashboard")
st.write("Compare solar metrics across countries and regions.")

# Sidebar filters
country = st.sidebar.selectbox("Select Country", ["Benin", "Sierra Leone", "Togo"])
metric = st.sidebar.selectbox("Select Metric", ["GHI", "DNI", "DHI"])

# Load data
df = load_data(country)

# Boxplot
st.subheader(f"{metric} Distribution in {country}")
fig, ax = plt.subplots()
sns.boxplot(data=df, y=metric, ax=ax)
st.pyplot(fig)

# Summary table
st.subheader("Summary Statistics")
st.write(df[[metric]].describe())

# Top regions (assuming 'Region' column exists)
if "Region" in df.columns:
    st.subheader(f"Top 5 Regions by {metric}")
    top_regions = df.groupby("Region")[metric].mean().sort_values(ascending=False).head(5)
    st.table(top_regions)

# Footer
st.markdown("---")
st.markdown("Developed by Abdulaziz Mohammed | Moonlight Energy Solutions")



date_range = st.sidebar.date_input(
    "Date Range", 
    [df['Timestamp'].min(), df['Timestamp'].max()]
)
if isinstance(date_range, tuple) and len(date_range) == 2:
    start_date, end_date = date_range
else:
    start_date = end_date = date_range if isinstance(date_range, pd.Timestamp) else df['Timestamp'].min()

