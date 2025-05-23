import pandas as pd

def load_data(country):
    file_map = {
        "Benin": "../data/benin_cleaned.csv",
        "Sierra Leone": "../data/sierraleone_cleaned.csv",
        "Togo": "../data/togo_cleaned.csv"
    }
    return pd.read_csv(file_map[country])

def get_summary(df):
    return df[["GHI", "DNI", "DHI"]].describe()

def get_top_regions(df, metric="GHI", top_n=5):
    return df.groupby("Region")[metric].mean().sort_values(ascending=False).head(top_n)
