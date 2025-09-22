import os
import pandas as pd
import numpy as np
import re

DATA_FILE_PATH = os.path.join(
    "data", "testsets", "testset_raw_unified_deduplicated.csv"
)

# Load your dataset
df = pd.read_csv(DATA_FILE_PATH)


# Function to extract the week from the path
def extract_week(path):
    match = re.search(r"/week-([a-z0-9]+)", str(path))
    return match.group(1) if match else "unknown"


df["week"] = df["reference_context_path"].apply(extract_week)

# Parameters
N_PER_WEEK = 10  # Now 10 questions per week
PROP_DOCUMENT = 0.16  # adjust to 0.15, 0.16, 0.17 as desired
PROP_CHUNK = 1 - PROP_DOCUMENT


# Function for balanced sampling between personas and query_style
def balanced_sample(df_group, n, exclude_paths=None):
    if exclude_paths is not None:
        df_group = df_group[~df_group["reference_context_path"].isin(exclude_paths)]
    if len(df_group) == 0 or n == 0:
        return pd.DataFrame()
    personas = df_group["persona_name"].unique()
    styles = df_group["query_style"].unique()
    n_persona = max(1, n // len(personas))
    n_style = max(1, n // len(styles))
    samples = []
    # Sample from each persona
    for p in personas:
        group_p = df_group[df_group["persona_name"] == p]
        if not group_p.empty:
            n_p = min(n_persona, len(group_p))
            samples.append(group_p.sample(n=n_p, random_state=42))
    # Sample from each style (complete if missing)
    current = pd.concat(samples) if samples else pd.DataFrame()
    if len(current) < n:
        remaining = df_group.drop(current.index)
        for s in styles:
            group_s = remaining[remaining["query_style"] == s]
            n_s = min(n_style, n - len(current), len(group_s))
            if n_s > 0:
                samples.append(group_s.sample(n=n_s, random_state=42))
            if len(pd.concat(samples)) >= n:
                break
    result = pd.concat(samples).drop_duplicates().head(n)
    # If still missing, complete randomly
    if len(result) < n:
        extra = df_group.drop(result.index)
        if not extra.empty:
            result = pd.concat(
                [result, extra.sample(n=n - len(result), random_state=42)]
            )
    return result


# New logic: ensure maximum diversity of paths and balance of extra columns
final_samples = []
weeks = df["week"].unique()
for week in weeks:
    df_week = df[df["week"] == week].copy()
    df_week["orig_index"] = df_week.index
    paths = df_week["reference_context_path"].unique()
    if len(paths) > N_PER_WEEK:
        # Balance paths per persona
        persona_paths = (
            df_week.groupby("persona_name")["reference_context_path"].unique().to_dict()
        )
        n_personas = len(persona_paths)
        n_per_persona = N_PER_WEEK // n_personas
        selected_paths = []
        # Randomly select paths for each persona
        for persona, p_paths in persona_paths.items():
            n = min(n_per_persona, len(p_paths))
            selected = np.random.choice(p_paths, n, replace=False)
            selected_paths.extend(selected)
        # If still not reached N_PER_WEEK, complete randomly
        if len(selected_paths) < N_PER_WEEK:
            remaining = list(set(paths) - set(selected_paths))
            extra = np.random.choice(
                remaining, N_PER_WEEK - len(selected_paths), replace=False
            )
            selected_paths.extend(extra)
        week_sample = df_week[df_week["reference_context_path"].isin(selected_paths)]
        week_sample = (
            week_sample.groupby("reference_context_path")
            .apply(lambda x: x.sample(1, random_state=42))
            .reset_index(drop=True)
        )
    else:
        week_sample = (
            df_week.groupby("reference_context_path")
            .apply(lambda x: x.sample(1, random_state=42))
            .reset_index(drop=True)
        )
    n_remaining = N_PER_WEEK - len(week_sample)
    if n_remaining > 0:
        remaining = df_week.drop(week_sample["orig_index"])
        if len(remaining) > 0:
            extra = remaining.sample(
                n=min(n_remaining, len(remaining)), random_state=42
            )
            week_sample = pd.concat([week_sample, extra])
    if len(week_sample) > N_PER_WEEK:
        week_sample = week_sample.sample(n=N_PER_WEEK, random_state=42)
    if "orig_index" in week_sample.columns:
        week_sample = week_sample.drop(columns=["orig_index"])
    final_samples.append(week_sample)

# Concatenate everything and shuffle
final_df = (
    pd.concat(final_samples).sample(frac=1, random_state=42).reset_index(drop=True)
)

# Save result
final_df.to_csv("sampled_stratified_go.csv", index=False)

# Show final distribution
print("Final distribution per week:")
print(final_df["week"].value_counts())
print("\nFinal distribution per reference_context_type:")
print(final_df["reference_context_type"].value_counts(normalize=True).round(2))
print("\nFinal distribution per persona_name:")
print(final_df["persona_name"].value_counts(normalize=True).round(2))
print("\nFinal distribution per query_style:")
print(final_df["query_style"].value_counts(normalize=True).round(2))
print("\nFile coverage:")
print(final_df["reference_context_path"].value_counts())
