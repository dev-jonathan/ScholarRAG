"""
Human Evaluation Processing Pipeline for Synthetic QA Dataset

This script processes raw human evaluation data from Label Studio and performs
statistical analysis to compare automatic (RAGAS) and human evaluation metrics.

Author: [Your Name]
Date: [Date]
Version: 1.0

Scientific Context:
- Implements correlation analysis between automatic and human evaluation metrics
- Applies exclusion criteria based on empirical thresholds
- Provides statistical validation for dataset quality assessment
- Supports reproducibility in synthetic QA dataset evaluation research
"""

import ast
import os
import pandas as pd
import json
from scipy.stats import spearmanr
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from typing import List, Dict, Any, Optional


def safe_list(val: Any) -> List[str]:
    """
    Ensures that context values are always returned as lists of strings.

    Args:
        val: Input value that may be a list, string, or other type

    Returns:
        List of strings representing the context

    Scientific Justification:
    This function handles various data formats that may arise from different
    export formats or data processing steps, ensuring consistent data structure
    for downstream analysis.
    """
    if isinstance(val, list):
        return val
    if pd.isna(val):
        return []
    try:
        parsed_val = ast.literal_eval(val)
        if isinstance(parsed_val, list):
            return parsed_val
        return [parsed_val]
    except (ValueError, SyntaxError):
        return [val] if isinstance(val, str) and val.strip() else []


def parse_likert_score(choice_text: str) -> Optional[int]:
    """
    Robustly parses Likert scale scores from Label Studio choice text.

    Args:
        choice_text: Text like "5 - Completely faithful" or "3 - Partially relevant"

    Returns:
        Integer score (1-5) or None if parsing fails

    Scientific Justification:
    This function handles variations in Label Studio export formats and ensures
    consistent numerical representation of Likert scale responses for statistical analysis.
    """
    if not choice_text or not isinstance(choice_text, str):
        return None

    # Extract the first number from the choice text
    try:
        # Handle various formats: "5 - Completely faithful", "3", "3 - Partially relevant"
        score_str = choice_text.strip().split()[0]
        score = int(score_str)

        # Validate score range (Likert 1-5)
        if 1 <= score <= 5:
            return score
        else:
            print(f"Warning: Score {score} outside valid range (1-5)")
            return None
    except (ValueError, IndexError) as e:
        print(f"Warning: Could not parse score from '{choice_text}': {e}")
        return None


def validate_statistical_assumptions(
    data: pd.Series, metric_name: str
) -> Dict[str, Any]:
    """
    Validates statistical assumptions for correlation analysis.

    Args:
        data: Series containing metric values
        metric_name: Name of the metric for reporting

    Returns:
        Dictionary with validation results

    Scientific Justification:
    Correlation analysis requires certain assumptions about data distribution
    and sample size. This function provides transparency about these assumptions.
    """
    results = {
        "metric": metric_name,
        "sample_size": len(data.dropna()),
        "mean": data.mean(),
        "std": data.std(),
        "min": data.min(),
        "max": data.max(),
        "missing_values": data.isna().sum(),
    }

    # Check for sufficient sample size (n > 30 for normal approximation)
    results["sufficient_sample"] = results["sample_size"] > 30

    # Basic normality check (not strict, but informative)
    if results["sample_size"] > 10:
        results["normality_check"] = "Sample size sufficient for correlation analysis"
    else:
        results["normality_check"] = (
            "Warning: Small sample size may affect correlation reliability"
        )

    return results


# --- Configuration and Thresholds ---
# These thresholds were determined through empirical analysis and literature review
#
# EXCLUSION CRITERIA:
# 1. Human Explicit Exclusion: Samples manually marked for removal in Label Studio
# 2. RAGAS Automatic Exclusion: Samples with RAGAS scores <= threshold (60% quality standard)
#    - ragas_faithfulness <= 0.6
#    - ragas_answer_relevancy <= 0.6
#    - ragas_question_quality <= 3
#    NOTE: RAGAS exclusion is DISABLED to prioritize human evaluation
# 3. Human Score-Based Exclusion: Samples with human scores <= threshold (safety mechanism)
#    - human_faithfulness <= 3
#    - human_response_relevancy <= 3
#    - human_question_quality <= 3
#    Note: This catches cases where humans gave low scores but forgot to mark "exclude"
#
# FINAL EXCLUSION: Any sample meeting criteria 1 OR 3 (RAGAS exclusion disabled)

JSON_FILE_PATH = os.path.join(
    "data", "testsets", "human_eval", "testset_human_eval_raw.json"
)

# Exclusion thresholds based on empirical analysis and quality standards
# Aligned with 60% standard (consistent with Likert scale 3/5 = 60%)
# Using <= to include threshold values in exclusion (e.g., score = 3 is excluded)
FAITHFULNESS_RAGAS_THRESHOLD = 0.6  # Scores <= 0.6 are excluded (60% threshold)
ANSWER_RELEVANCY_RAGAS_THRESHOLD = 0.6  # Scores <= 0.6 are excluded (60% threshold)
QUESTION_QUALITY_RAGAS_THRESHOLD = 3  # Scores <= 3 are excluded (60% threshold)

# Human evaluation thresholds (Likert scale 1-5)
# Consistent with 60% standard (3/5 = 60%)
# Using <= to include threshold values in exclusion (e.g., score = 3 is excluded)
FAITHFULNESS_HUMAN_THRESHOLD = 3  # Scores <= 3 are excluded (60% threshold)
RESPONSE_RELEVANCY_HUMAN_THRESHOLD = 3  # Scores <= 3 are excluded (60% threshold)
QUESTION_QUALITY_HUMAN_THRESHOLD = 3  # Scores <= 3 are excluded (60% threshold)

print("Loading JSON dataset...")
with open(JSON_FILE_PATH, "r", encoding="utf-8") as f:
    raw_data = json.load(f)

# --- Data Preprocessing and Normalization ---
processed_samples = []
for item in raw_data:
    data = item["data"]

    # Extract automatic RAGAS metrics from 'data' field
    ragas_faithfulness = data.get("faithfulness")
    ragas_answer_relevancy = data.get("answer_relevancy")
    ragas_question_quality = data.get("question_quality")

    # Extract human annotations with robust parsing
    human_faithfulness = None
    human_response_relevancy = None
    human_question_quality = None
    exclude_human_explicit = False
    human_comments = ""

    for annotation in item.get("annotations", []):
        for result in annotation.get("result", []):
            if result["from_name"] == "faithfulness" and result["type"] == "choices":
                choice_text = (
                    result["value"]["choices"][0] if result["value"]["choices"] else ""
                )
                human_faithfulness = parse_likert_score(choice_text)
            elif (
                result["from_name"] == "response_relevancy"
                and result["type"] == "choices"
            ):
                choice_text = (
                    result["value"]["choices"][0] if result["value"]["choices"] else ""
                )
                human_response_relevancy = parse_likert_score(choice_text)
            elif (
                result["from_name"] == "simple_criteria_score"
                and result["type"] == "choices"
            ):
                choice_text = (
                    result["value"]["choices"][0] if result["value"]["choices"] else ""
                )
                human_question_quality = parse_likert_score(choice_text)
            elif (
                result["from_name"] == "remove_question" and result["type"] == "choices"
            ):
                if "Remove question" in result["value"]["choices"]:
                    exclude_human_explicit = True
            elif result["from_name"] == "comments" and result["type"] == "textarea":
                human_comments = (
                    result["value"]["text"][0] if result["value"]["text"] else ""
                )

    processed_samples.append(
        {
            "id": data["id"],
            "user_input": data["user_input"],
            "response": data["response"],
            "retrieved_contexts": safe_list(data["retrieved_contexts"]),
            "ragas_faithfulness": ragas_faithfulness,
            "ragas_answer_relevancy": ragas_answer_relevancy,
            "ragas_question_quality": ragas_question_quality,
            "human_faithfulness": human_faithfulness,
            "human_response_relevancy": human_response_relevancy,
            "human_question_quality": human_question_quality,
            "exclude_human_explicit": exclude_human_explicit,
            "human_comments": human_comments,
        }
    )

# Create DataFrame
df_processed = pd.DataFrame(processed_samples)

# --- Explicit conversion of columns to numeric (prevents comparison errors) ---
numeric_columns = [
    "ragas_faithfulness",
    "ragas_answer_relevancy",
    "ragas_question_quality",
    "human_faithfulness",
    "human_response_relevancy",
    "human_question_quality",
]

for col in numeric_columns:
    df_processed[col] = pd.to_numeric(df_processed[col], errors="coerce")

# --- Statistical Validation of Data Quality ---
print("\n=== Statistical Validation ===")
for col in numeric_columns:
    validation = validate_statistical_assumptions(df_processed[col], col)
    print(
        f"{validation['metric']}: n={validation['sample_size']}, "
        f"mean={validation['mean']:.3f}, std={validation['std']:.3f}, "
        f"missing={validation['missing_values']}"
    )

    # Report missing value details for transparency
    if validation["missing_values"] > 0:
        missing_indices = df_processed[df_processed[col].isna()].index.tolist()
        print(f"  Missing indices for {col}: {missing_indices}")
        print(
            f"  Missing percentage: {validation['missing_values']/len(df_processed)*100:.1f}%"
        )

# --- Exclusion Criteria Application ---

# Mark for automatic exclusion by RAGAS metrics (DISABLED - prioritizing human evaluation)
df_processed["exclude_auto_ragas"] = False
# RAGAS exclusion disabled to prioritize human evaluation - samples with RAGAS <=0.6 but high human scores are kept
# df_processed.loc[
#     df_processed["ragas_faithfulness"] <= FAITHFULNESS_RAGAS_THRESHOLD,
#     "exclude_auto_ragas",
# ] = True
# df_processed.loc[
#     df_processed["ragas_answer_relevancy"] <= ANSWER_RELEVANCY_RAGAS_THRESHOLD,
#     "exclude_auto_ragas",
# ] = True
# df_processed.loc[
#     df_processed["ragas_question_quality"] <= QUESTION_QUALITY_RAGAS_THRESHOLD,
#     "exclude_auto_ragas",
# ] = True

# Mark for automatic exclusion by human metrics (safety mechanism for missed explicit exclusions)
df_processed["exclude_auto_human_metrics"] = False
# Only apply if human value is not NaN to avoid comparison issues
df_processed.loc[
    (df_processed["human_faithfulness"].notna())
    & (df_processed["human_faithfulness"] <= FAITHFULNESS_HUMAN_THRESHOLD),
    "exclude_auto_human_metrics",
] = True
df_processed.loc[
    (df_processed["human_response_relevancy"].notna())
    & (df_processed["human_response_relevancy"] <= RESPONSE_RELEVANCY_HUMAN_THRESHOLD),
    "exclude_auto_human_metrics",
] = True
df_processed.loc[
    (df_processed["human_question_quality"].notna())
    & (df_processed["human_question_quality"] <= QUESTION_QUALITY_HUMAN_THRESHOLD),
    "exclude_auto_human_metrics",
] = True

# Final exclusion column (combines all three criteria)
df_processed["remove_final"] = (
    df_processed["exclude_human_explicit"]
    | df_processed["exclude_auto_ragas"]
    | df_processed["exclude_auto_human_metrics"]
)

# Create cleaned dataset
df_cleaned = df_processed[~df_processed["remove_final"]].copy()

# --- Detailed Exclusion Analysis ---
print("\n=== Detailed Exclusion Analysis ===")

# Find samples with RAGAS scores <=60% but NOT excluded by human (RAGAS exclusion disabled)
ragas_low_but_not_excluded = df_processed[
    (
        (df_processed["ragas_faithfulness"] <= FAITHFULNESS_RAGAS_THRESHOLD)
        | (df_processed["ragas_answer_relevancy"] <= ANSWER_RELEVANCY_RAGAS_THRESHOLD)
        | (df_processed["ragas_question_quality"] <= QUESTION_QUALITY_RAGAS_THRESHOLD)
    )
    & (df_processed["exclude_human_explicit"] == False)
]

print(f"Samples <=60% in RAGAS but NOT by human: {len(ragas_low_but_not_excluded)}")
if len(ragas_low_but_not_excluded) > 0:
    print("Details of samples with low RAGAS scores but kept due to human evaluation:")
    for idx, row in ragas_low_but_not_excluded.iterrows():
        print(f"  Sample {idx}:")
        print(
            f"    RAGAS scores - Faithfulness: {row['ragas_faithfulness']:.3f}, "
            f"Answer Relevancy: {row['ragas_answer_relevancy']:.3f}, "
            f"Question Quality: {row['ragas_question_quality']:.3f}"
        )
        print(
            f"    Human scores - Faithfulness: {row['human_faithfulness']}, "
            f"Response Relevancy: {row['human_response_relevancy']}, "
            f"Question Quality: {row['human_question_quality']}"
        )
        print(f"    User Input: {row['user_input'][:100]}...")
        print(f"    Response: {row['response'][:100]}...")
        print()

# Find samples excluded by human but NOT by RAGAS (RAGAS exclusion disabled)
human_only_excluded = df_processed[
    (df_processed["exclude_human_explicit"] == True)
    # & (df_processed["exclude_auto_ragas"] == False)  # RAGAS exclusion disabled
]

print(f"Samples excluded by human but NOT by RAGAS: {len(human_only_excluded)}")
if len(human_only_excluded) > 0:
    print("Details of human-only exclusions:")
    for idx, row in human_only_excluded.iterrows():
        print(f"  Sample {idx}:")
        print(
            f"    RAGAS scores - Faithfulness: {row['ragas_faithfulness']:.3f}, "
            f"Answer Relevancy: {row['ragas_answer_relevancy']:.3f}, "
            f"Question Quality: {row['ragas_question_quality']:.3f}"
        )
        print(
            f"    Human scores - Faithfulness: {row['human_faithfulness']}, "
            f"Response Relevancy: {row['human_response_relevancy']}, "
            f"Question Quality: {row['human_question_quality']}"
        )
        print(f"    Human Comments: {row['human_comments']}")
        print(f"    User Input: {row['user_input'][:100]}...")
        print(f"    Response: {row['response'][:100]}...")
        print()

# Find samples excluded by human score-based criteria but NOT explicitly marked for removal
human_score_excluded_but_not_explicit = df_processed[
    (df_processed["exclude_auto_human_metrics"] == True)
    & (df_processed["exclude_human_explicit"] == False)
]

print(
    f"Samples excluded by human score-based criteria but NOT explicitly marked: {len(human_score_excluded_but_not_explicit)}"
)
if len(human_score_excluded_but_not_explicit) > 0:
    print("Details of human score-based exclusions (safety mechanism):")
    for idx, row in human_score_excluded_but_not_explicit.iterrows():
        print(f"  Sample {idx}:")
        print(
            f"    Human scores - Faithfulness: {row['human_faithfulness']}, "
            f"Response Relevancy: {row['human_response_relevancy']}, "
            f"Question Quality: {row['human_question_quality']}"
        )
        print(
            f"    RAGAS scores - Faithfulness: {row['ragas_faithfulness']:.3f}, "
            f"Answer Relevancy: {row['ragas_answer_relevancy']:.3f}, "
            f"Question Quality: {row['ragas_question_quality']:.3f}"
        )
        print(f"    Human Comments: {row['human_comments']}")
        print(f"    User Input: {row['user_input'][:100]}...")
        print(f"    Response: {row['response'][:100]}...")
        print(
            "    NOTE: This sample was automatically excluded due to low human scores"
        )
        print("          but was NOT explicitly marked for removal in the annotation.")
        print(
            "          This suggests the human evaluator may have forgotten to mark 'exclude'."
        )
        print()

# Create column for any RAGAS low score (for analysis only, not for exclusion)
df_processed["any_ragas_low_score"] = (
    (df_processed["ragas_faithfulness"] <= FAITHFULNESS_RAGAS_THRESHOLD)
    | (df_processed["ragas_answer_relevancy"] <= ANSWER_RELEVANCY_RAGAS_THRESHOLD)
    | (df_processed["ragas_question_quality"] <= QUESTION_QUALITY_RAGAS_THRESHOLD)
)

# --- Summary Statistics ---
print(f"\n=== Dataset Processing Summary ===")
print(f"Original samples: {len(df_processed)}")
print(f"Explicitly excluded by human: {df_processed['exclude_human_explicit'].sum()}")
print(
    f"RAGAS low scores (<=60%) but kept due to human evaluation: {df_processed['any_ragas_low_score'].sum()}"
)
print(
    f"Automatically excluded by human metrics: {df_processed['exclude_auto_human_metrics'].sum()}"
)
print(f"Total excluded (final): {df_processed['remove_final'].sum()}")
print(f"Final cleaned dataset size: {len(df_cleaned)}")
print(f"Retention rate: {len(df_cleaned)/len(df_processed)*100:.1f}%")

# Detailed breakdown of exclusion reasons
print(f"\n=== Detailed Exclusion Breakdown ===")
print("Exclusion by specific criteria:")
print(f"  - Human explicit exclusion only: {len(human_only_excluded)}")
print(
    f"  - RAGAS low scores (<=60%) but kept due to human evaluation: {len(ragas_low_but_not_excluded)}"
)
print(
    f"  - Human score-based exclusion only: {len(human_score_excluded_but_not_explicit)}"
)

# Count samples excluded by multiple criteria (RAGAS exclusion disabled)
multiple_criteria = df_processed[
    (df_processed["exclude_human_explicit"] == True)
    # & (df_processed["exclude_auto_ragas"] == True)  # RAGAS exclusion disabled
]
print(
    f"  - Human explicit exclusion (RAGAS exclusion disabled): {len(multiple_criteria)}"
)

multiple_criteria2 = df_processed[
    (df_processed["exclude_human_explicit"] == True)
    & (df_processed["exclude_auto_human_metrics"] == True)
]
print(
    f"  - Both human explicit AND human score-based exclusion: {len(multiple_criteria2)}"
)

# multiple_criteria3 = df_processed[
#     (df_processed["exclude_auto_ragas"] == True)
#     & (df_processed["exclude_auto_human_metrics"] == True)
# ]
# print(f"  - Both RAGAS AND human score-based exclusion: {len(multiple_criteria3)}")
print(f"  - RAGAS exclusion disabled - no samples excluded by RAGAS criteria")

# Save cleaned dataset
output_cleaned_path = os.path.join(
    "data", "testsets", "human_eval", "testset_human_eval_cleaned.csv"
)
os.makedirs(os.path.dirname(output_cleaned_path), exist_ok=True)
df_cleaned.to_csv(output_cleaned_path, index=False)
print(f"Cleaned dataset saved to: {output_cleaned_path}")

# --- Correlation Analysis (Spearman) ---

# Create individual subsets for each metric to avoid cross-contamination
df_faithfulness_subset = df_processed[
    (df_processed["human_faithfulness"].notna())
    & (df_processed["ragas_faithfulness"].notna())
].copy()

df_relevancy_subset = df_processed[
    (df_processed["human_response_relevancy"].notna())
    & (df_processed["ragas_answer_relevancy"].notna())
].copy()

df_quality_subset = df_processed[
    (df_processed["human_question_quality"].notna())
    & (df_processed["ragas_question_quality"].notna())
].copy()

print(f"\n=== Correlation Analysis ===")
print(f"Faithfulness: {len(df_faithfulness_subset)} samples")
print(f"Response Relevancy: {len(df_relevancy_subset)} samples")
print(f"Question Quality: {len(df_quality_subset)} samples")

if len(df_faithfulness_subset) > 1:
    # Correlation for Faithfulness
    corr_faithfulness_spearman, p_faithfulness = spearmanr(
        df_faithfulness_subset["ragas_faithfulness"],
        df_faithfulness_subset["human_faithfulness"],
    )
    print(
        f"Spearman correlation (RAGAS vs Human Faithfulness): {corr_faithfulness_spearman:.3f} (p={p_faithfulness:.3f})"
    )

    # Correlation for Response Relevancy
    corr_relevancy_spearman, p_relevancy = spearmanr(
        df_relevancy_subset["ragas_answer_relevancy"],
        df_relevancy_subset["human_response_relevancy"],
    )
    print(
        f"Spearman correlation (RAGAS vs Human Response Relevancy): {corr_relevancy_spearman:.3f} (p={p_relevancy:.3f})"
    )

    # Correlation for Question Quality
    corr_question_quality_spearman, p_question_quality = spearmanr(
        df_quality_subset["ragas_question_quality"],
        df_quality_subset["human_question_quality"],
    )
    print(
        f"Spearman correlation (RAGAS vs Human Question Quality): {corr_question_quality_spearman:.3f} (p={p_question_quality:.3f})"
    )

    # Statistical significance interpretation
    print(f"\n=== Statistical Significance ===")
    alpha = 0.05
    correlations = [
        ("Faithfulness", corr_faithfulness_spearman, p_faithfulness),
        ("Response Relevancy", corr_relevancy_spearman, p_relevancy),
        ("Question Quality", corr_question_quality_spearman, p_question_quality),
    ]

    for metric, corr, p_val in correlations:
        significance = "significant" if p_val < alpha else "not significant"
        print(f"{metric}: r={corr:.3f}, p={p_val:.3f} ({significance} at α={alpha})")

    # --- Visualization of Correlations ---
    print("\nGenerating correlation plots...")

    def plot_correlation(
        df: pd.DataFrame,
        metric_ragas: str,
        metric_human: str,
        title: str,
        ax: plt.Axes,
        corr_value: float = None,
        p_value: float = None,
    ):
        """Create scatter plot with correlation line and confidence interval."""
        # Remove NaN values for plotting
        valid_data = df[[metric_ragas, metric_human]].dropna()

        # Print sample count for verification
        print(f"{title}: {len(valid_data)} samples plotted (from {len(df)} total)")

        if len(valid_data) > 0:
            # Add jitter for discrete variables to reduce overplotting
            x_data = valid_data[metric_ragas].copy()
            y_data = valid_data[metric_human].copy()

            # Apply jitter to discrete variables (Likert scales)
            if "question_quality" in metric_ragas:
                # Both axes are Likert scale - add jitter to both
                jitter_amount = 0.1
                x_data = x_data + np.random.normal(0, jitter_amount, len(x_data))
                y_data = y_data + np.random.normal(0, jitter_amount, len(y_data))
            else:
                # Only Y-axis is Likert scale - add jitter only to Y
                jitter_amount = 0.1
                y_data = y_data + np.random.normal(0, jitter_amount, len(y_data))

            # Calculate distance from regression line for color intensity
            z = np.polyfit(valid_data[metric_ragas], valid_data[metric_human], 1)
            p = np.poly1d(z)
            predicted_y = p(valid_data[metric_ragas])
            distances = np.abs(valid_data[metric_human] - predicted_y)

            # Normalize distances for color mapping (0 = close to line, 1 = far from line)
            max_dist = distances.max()
            if max_dist > 0:
                normalized_distances = distances / max_dist
            else:
                normalized_distances = np.zeros_like(distances)

            # Create color map: blue (close to line) to red (far from line)
            colors = plt.cm.RdYlBu_r(normalized_distances)

            # Create scatter plot with colored data
            scatter = ax.scatter(
                x_data,
                y_data,
                c=colors,
                alpha=0.7,
                s=40,
                edgecolors="black",
                linewidth=0.5,
            )

            # Add regression line without confidence interval for cleaner look
            x_range = np.linspace(
                valid_data[metric_ragas].min(), valid_data[metric_ragas].max(), 100
            )
            ax.plot(x_range, p(x_range), "r-", linewidth=2, label="Regression Line")

            # Add perfect correlation line for reference (dashed)
            if "question_quality" in metric_ragas:
                # Both scales are 1-5
                ax.plot(
                    [1, 5],
                    [1, 5],
                    "k--",
                    alpha=0.5,
                    linewidth=1,
                    label="Perfect Correlation",
                )
            else:
                # RAGAS 0-1, Human 1-5
                ax.plot(
                    [0, 1],
                    [1, 5],
                    "k--",
                    alpha=0.5,
                    linewidth=1,
                    label="Perfect Correlation",
                )

            # Set proper axis scales based on metric types
            if "question_quality" in metric_ragas:
                # Question Quality: Likert scale 1-5 for both RAGAS and Human
                ax.set_xlim(0.5, 5.5)
                ax.set_ylim(0.5, 5.5)
                ax.set_xticks([1, 2, 3, 4, 5])
                ax.set_yticks([1, 2, 3, 4, 5])
            else:
                # Faithfulness/Response Relevancy: RAGAS 0-1, Human 1-5
                ax.set_xlim(-0.05, 1.05)
                ax.set_ylim(0.5, 5.5)
                ax.set_xticks([0.0, 0.2, 0.4, 0.6, 0.8, 1.0])
                ax.set_yticks([1, 2, 3, 4, 5])

            # Add correlation statistics to plot
            if corr_value is not None and p_value is not None:
                significance = (
                    "***"
                    if p_value < 0.001
                    else "**" if p_value < 0.01 else "*" if p_value < 0.05 else ""
                )

                stats_text = f"Correlation (r) = {corr_value:.3f}{significance}\np-value = {p_value:.3f}\nSamples: {len(valid_data)}"
                ax.text(
                    0.02,
                    0.98,
                    stats_text,
                    transform=ax.transAxes,
                    verticalalignment="top",
                    fontsize=9,
                    bbox=dict(
                        boxstyle="round", facecolor="white", alpha=0.9, edgecolor="gray"
                    ),
                    fontweight="bold",
                )

            ax.set_title(title, fontsize=12, fontweight="bold")
            ax.set_xlabel(
                f'{metric_ragas.replace("ragas_", "").replace("_", " ").title()} (RAGAS)',
                fontsize=10,
            )
            ax.set_ylabel(
                f'{metric_human.replace("human_", "").replace("_", " ").title()} (Human)',
                fontsize=10,
            )
            ax.grid(True, linestyle="--", alpha=0.7)
            ax.legend(fontsize=8)

            # Add colorbar to show distance interpretation
            sm = plt.cm.ScalarMappable(
                cmap=plt.cm.RdYlBu_r, norm=plt.Normalize(0, max_dist)
            )
            sm.set_array([])
            cbar = plt.colorbar(sm, ax=ax, shrink=0.8, aspect=20)
            cbar.set_label("Distance from Regression Line", fontsize=8)
        else:
            ax.text(
                0.5,
                0.5,
                f"No valid data for {title}",
                ha="center",
                va="center",
                transform=ax.transAxes,
            )
            ax.set_title(title, fontsize=12, fontweight="bold")

    # Create combined correlation plot
    fig, axes = plt.subplots(1, 3, figsize=(18, 5))

    # Plot each correlation with statistics
    plot_correlation(
        df_faithfulness_subset,  # Use individual subset
        "ragas_faithfulness",
        "human_faithfulness",
        "Faithfulness\n(RAGAS vs Human)",
        axes[0],
        corr_value=corr_faithfulness_spearman,
        p_value=p_faithfulness,
    )

    plot_correlation(
        df_relevancy_subset,  # Use individual subset
        "ragas_answer_relevancy",
        "human_response_relevancy",
        "Response Relevancy\n(RAGAS vs Human)",
        axes[1],
        corr_value=corr_relevancy_spearman,
        p_value=p_relevancy,
    )

    plot_correlation(
        df_quality_subset,  # Use individual subset
        "ragas_question_quality",
        "human_question_quality",
        "Question Quality\n(RAGAS vs Human)",
        axes[2],
        corr_value=corr_question_quality_spearman,
        p_value=p_question_quality,
    )

    plt.tight_layout()
    plt.show()

    print(f"\nCombined correlation analysis:")
    print(
        f"- Faithfulness: r={corr_faithfulness_spearman:.3f} (p={p_faithfulness:.3f})"
    )
    print(
        f"- Response Relevancy: r={corr_relevancy_spearman:.3f} (p={p_relevancy:.3f})"
    )
    print(
        f"- Question Quality: r={corr_question_quality_spearman:.3f} (p={p_question_quality:.3f})"
    )

    # --- Low Correlation Analysis ---
    print("\n=== Low Correlation Analysis ===")

    # Function to find samples with largest deviations from regression line
    def find_low_correlation_samples(
        df_subset, metric_ragas, metric_human, metric_name
    ):
        """Find samples with largest deviations from regression line for analysis"""
        if len(df_subset) < 2:
            return []

        # Calculate regression line
        x = df_subset[metric_ragas].values
        y = df_subset[metric_human].values
        z = np.polyfit(x, y, 1)
        p = np.poly1d(z)
        predicted_y = p(x)

        # Calculate distances from regression line
        distances = np.abs(y - predicted_y)

        # Find top 5 samples with largest deviations
        top_indices = np.argsort(distances)[-5:][::-1]

        low_corr_samples = []
        for idx in top_indices:
            sample_idx = df_subset.index[idx]
            sample_data = df_subset.loc[sample_idx]
            low_corr_samples.append(
                {
                    "sample_idx": sample_idx,
                    "ragas_score": sample_data[metric_ragas],
                    "human_score": sample_data[metric_human],
                    "predicted_human": predicted_y[idx],
                    "deviation": distances[idx],
                    "user_input": sample_data["user_input"],
                    "response": sample_data["response"],
                }
            )

        return low_corr_samples

    # Analyze each metric for low correlation samples
    metrics_to_analyze = [
        (
            df_faithfulness_subset,
            "ragas_faithfulness",
            "human_faithfulness",
            "Faithfulness",
        ),
        (
            df_relevancy_subset,
            "ragas_answer_relevancy",
            "human_response_relevancy",
            "Response Relevancy",
        ),
        (
            df_quality_subset,
            "ragas_question_quality",
            "human_question_quality",
            "Question Quality",
        ),
    ]

    for df_subset, metric_ragas, metric_human, metric_name in metrics_to_analyze:
        low_corr_samples = find_low_correlation_samples(
            df_subset, metric_ragas, metric_human, metric_name
        )

        print(f"\nTop 5 samples with largest deviations in {metric_name}:")
        for i, sample in enumerate(low_corr_samples, 1):
            print(f"  {i}. Sample {sample['sample_idx']}:")
            print(
                f"     RAGAS: {sample['ragas_score']:.3f}, Human: {sample['human_score']}, "
                f"Predicted: {sample['predicted_human']:.2f}, Deviation: {sample['deviation']:.2f}"
            )
            print(f"     User Input: {sample['user_input'][:80]}...")
            print(f"     Response: {sample['response'][:80]}...")
            print()

    # Find samples with extreme score differences (RAGAS vs Human)
    print("=== Extreme Score Differences Analysis ===")

    def find_extreme_differences(df_subset, metric_ragas, metric_human, metric_name):
        """Find samples with extreme differences between RAGAS and human scores"""
        if len(df_subset) < 2:
            return []

        # Calculate normalized differences (accounting for different scales)
        if "question_quality" in metric_ragas:
            # Both scales are 1-5, so direct difference
            normalized_diff = np.abs(df_subset[metric_ragas] - df_subset[metric_human])
        else:
            # RAGAS 0-1, Human 1-5, normalize to 0-1 scale
            normalized_ragas = df_subset[metric_ragas]
            normalized_human = (df_subset[metric_human] - 1) / 4  # Convert 1-5 to 0-1
            normalized_diff = np.abs(normalized_ragas - normalized_human)

        # Find top 5 samples with largest differences
        top_indices = np.argsort(normalized_diff)[-5:][::-1]

        extreme_samples = []
        for idx in top_indices:
            sample_idx = df_subset.index[idx]
            sample_data = df_subset.loc[sample_idx]
            extreme_samples.append(
                {
                    "sample_idx": sample_idx,
                    "ragas_score": sample_data[metric_ragas],
                    "human_score": sample_data[metric_human],
                    "normalized_diff": normalized_diff[idx],
                    "user_input": sample_data["user_input"],
                    "response": sample_data["response"],
                }
            )

        return extreme_samples

    for df_subset, metric_ragas, metric_human, metric_name in metrics_to_analyze:
        extreme_samples = find_extreme_differences(
            df_subset, metric_ragas, metric_human, metric_name
        )

        print(f"\nTop 5 samples with extreme score differences in {metric_name}:")
        for i, sample in enumerate(extreme_samples, 1):
            print(f"  {i}. Sample {sample['sample_idx']}:")
            print(
                f"     RAGAS: {sample['ragas_score']:.3f}, Human: {sample['human_score']}, "
                f"Normalized Difference: {sample['normalized_diff']:.3f}"
            )
            print(f"     User Input: {sample['user_input'][:80]}...")
            print(f"     Response: {sample['response'][:80]}...")
            print()

    # --- Contingency Analysis ---
    # Create contingency table
    contingency_table = pd.crosstab(
        df_processed["exclude_human_explicit"],
        df_processed["any_ragas_low_score"],
        rownames=["Explicitly Excluded by Human"],
        colnames=["Any RAGAS Metric Below Threshold"],
    )

    print(f"\n=== Contingency Analysis ===")
    print("Contingency Table (Human Explicit Exclusion vs. RAGAS Low Scores):")
    print(contingency_table)

    # Chi-square test for independence
    from scipy.stats import chi2_contingency

    if contingency_table.shape == (2, 2) and contingency_table.values.min() > 0:
        chi2, p_val, dof, expected = chi2_contingency(contingency_table)
        print(f"Chi-square test: χ²={chi2:.3f}, p={p_val:.3f}, df={dof}")
        if p_val < 0.05:
            print("Significant association between human exclusion and RAGAS scores")
        else:
            print("No significant association between human exclusion and RAGAS scores")

    # Create figure with two subplots side by side
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(20, 8))

    # --- Plot 1: Improved Contingency Analysis (Side by side bars) ---
    # Prepare data for side-by-side bars
    categories = ["Not Excluded", "Excluded"]
    ragas_no = [
        contingency_table.iloc[0, 0],
        contingency_table.iloc[1, 0],
    ]  # RAGAS didn't flag
    ragas_yes = [
        contingency_table.iloc[0, 1],
        contingency_table.iloc[1, 1],
    ]  # RAGAS flagged

    x = np.arange(len(categories))
    width = 0.35

    # Create side-by-side bars
    bars1 = ax1.bar(
        x - width / 2,
        ragas_no,
        width,
        label="RAGAS: No Low Score",
        color="lightcoral",
        alpha=0.8,
    )
    bars2 = ax1.bar(
        x + width / 2,
        ragas_yes,
        width,
        label="RAGAS: Low Score Detected",
        color="lightgreen",
        alpha=0.8,
    )

    # Add value labels on bars with percentages
    def add_value_labels(bars, ax):
        for bar in bars:
            height = bar.get_height()
            total_samples = (
                ragas_no[0] + ragas_yes[0]
                if bar.get_x() < 0.5
                else ragas_no[1] + ragas_yes[1]
            )
            percentage = (height / total_samples) * 100 if total_samples > 0 else 0
            ax.text(
                bar.get_x() + bar.get_width() / 2.0,
                height + 0.5,
                f"{int(height)} ({percentage:.1f}%)",
                ha="center",
                va="bottom",
                fontsize=10,
                fontweight="bold",
            )

    add_value_labels(bars1, ax1)
    add_value_labels(bars2, ax1)

    ax1.set_xlabel("Human Exclusion Decision", fontsize=12, fontweight="bold")
    ax1.set_ylabel("Number of Samples", fontsize=12, fontweight="bold")
    ax1.set_title("Human vs RAGAS Agreement Analysis", fontsize=14, fontweight="bold")
    ax1.set_xticks(x)
    ax1.set_xticklabels(categories)
    ax1.legend()
    ax1.grid(axis="y", linestyle="--", alpha=0.7)

    # Add summary statistics as text (positioned below legend)
    total_not_excluded = ragas_no[0] + ragas_yes[0]
    total_excluded = ragas_no[1] + ragas_yes[1]
    ragas_agreement_rate = (
        (ragas_yes[1] / total_excluded) * 100 if total_excluded > 0 else 0
    )

    summary_text = f"""Summary:
• Not Excluded: {total_not_excluded} samples
• Excluded: {total_excluded} samples
• RAGAS Agreement: {ragas_agreement_rate:.1f}%
• False Negatives: {ragas_no[1]} samples"""

    ax1.text(
        0.72,
        0.89,
        summary_text,
        transform=ax1.transAxes,
        verticalalignment="top",
        fontsize=10,
        bbox=dict(boxstyle="round", facecolor="wheat", alpha=0.8),
    )

    # --- Plot 2: Correlation Matrix ---
    def plot_correlation_matrix(df_processed, ax):
        """Plot correlation matrix heatmap"""
        # Select numeric columns
        numeric_cols = [
            "ragas_faithfulness",
            "ragas_answer_relevancy",
            "ragas_question_quality",
            "human_faithfulness",
            "human_response_relevancy",
            "human_question_quality",
        ]

        # Create correlation matrix
        corr_matrix = df_processed[numeric_cols].corr(method="spearman")

        # Create heatmap
        im = sns.heatmap(
            corr_matrix,
            annot=True,
            cmap="coolwarm",
            center=0,
            square=True,
            fmt=".3f",
            ax=ax,
            cbar_kws={"shrink": 0.8},
        )

        ax.set_title(
            "Correlation Matrix: RAGAS vs Human Metrics",
            fontsize=14,
            fontweight="bold",
            pad=20,
        )

        # Rotate x-axis labels for better readability
        ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha="right")
        ax.set_yticklabels(ax.get_yticklabels(), rotation=0)

    plot_correlation_matrix(df_processed, ax2)

    plt.tight_layout()
    plt.show()

    print(f"\nContingency Chart Analysis:")
    print(f"- Samples NOT excluded by human: {contingency_table.iloc[0].sum()}")
    print(f"- Samples EXCLUDED by human: {contingency_table.iloc[1].sum()}")
    print(
        f"- RAGAS missed {contingency_table.iloc[1, 0]} problems that humans detected"
    )
    print(f"- RAGAS correctly flagged {contingency_table.iloc[1, 1]} problems")
    print(
        f"- RAGAS agreement rate: {(contingency_table.iloc[1, 1] / contingency_table.iloc[1].sum()) * 100:.1f}%"
    )

else:
    print("Insufficient samples with complete data for correlation analysis.")

print("\n=== Processing Complete ===")
