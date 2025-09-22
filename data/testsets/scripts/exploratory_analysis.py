import os
import pandas as pd


# DATA_FILE_PATH = os.path.join("data", "testsets", "processed", "testset_raw_unified.csv")
# DATA_FILE_PATH = os.path.join("data", "testsets", "processed", "testset_raw_unified_deduplicated.csv")
DATA_FILE_PATH = os.path.join("data", "testsets", "processed", "testset_stratified.csv")


# Load your dataset
df = pd.read_csv(DATA_FILE_PATH)

# Columns of interest
cols = [
    "reference_context_type",
    "reference_context_path",
    "persona_name",
    "query_style",
    "query_length",
    "synthesizer_name",
    "round",
]


# Function to generate frequency and percentage table
def freq_percent_table(df, col):
    freq = df[col].value_counts(dropna=False)
    percent = df[col].value_counts(normalize=True, dropna=False) * 100
    summary = pd.DataFrame({"Frequency": freq, "Percentage (%)": percent.round(2)})
    return summary


# Generate and display tables for each column
for col in cols:
    print(f"\n==== Distribution for: {col} ====")
    print(freq_percent_table(df, col))

# Combined insights (example: by week and context type)
if "reference_context_type" in df.columns and "round" in df.columns:
    print("\n==== Cross-tab: reference_context_type x round ====")
    print(
        pd.crosstab(
            df["reference_context_type"], df["round"], margins=True, normalize="columns"
        ).round(2)
    )

if "persona_name" in df.columns and "reference_context_type" in df.columns:
    print("\n==== Cross-tab: persona_name x reference_context_type ====")
    print(
        pd.crosstab(
            df["persona_name"],
            df["reference_context_type"],
            margins=True,
            normalize="columns",
        ).round(2)
    )

# Top 10 most used context files
if "reference_context_path" in df.columns:
    print("\n==== Top 10 context files ====")
    print(df["reference_context_path"].value_counts().head(10))

# How many unique files per week
print("\n==== Number of unique files per week ====")
files_per_week = df.groupby("week")["reference_context_path"].nunique()
print(files_per_week)

# Name and frequency of each file per week
print("\n==== Frequency of each file per week ====")
for week, group in df.groupby("week"):
    print(f"\nWeek: {week}")
    freq = group["reference_context_path"].value_counts()
    for path, count in freq.items():
        print(f"  {path}: {count} time(s)")

print("\n==== Number of questions per week ====")
print(df["week"].value_counts())

# General summary
print("\n==== General summary ====")
print(df.describe(include="all").T)
