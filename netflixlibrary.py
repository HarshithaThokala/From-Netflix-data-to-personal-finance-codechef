import pandas as pd

# Load Netflix Dataset
def load_data():
    df = pd.read_csv("netflix.csv")
    print(df[["title", "type", "release_year"]].head())
    return df

# Explore Dataset Structure
def explore_dataset(df):
    print("Shape of the dataset:", df.shape)
    print("Column Names:", list(df.columns))

# Analyze Content Distribution
def count_content_types(df):
    print(df["type"].value_counts())

# Filter Recent Content
def filter_recent_content(df):
    recent_df = df[df["release_year"] > 2015]
    print(recent_df[["title", "type", "release_year"]].head())
    return recent_df

# Find Popular Ratings
def top_ratings(df):
    print(df["rating"].value_counts().head())

# View Latest Netflix Content
def sort_by_release_year(df):
    latest_df = df.sort_values(by="release_year", ascending=False)
    print(latest_df[["title", "type", "release_year"]].head())
