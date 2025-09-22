import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import ttest_ind, mannwhitneyu

# Load data
df_wide = pd.read_csv(
    r"C:\Users\Jonathan\Desktop\pet\ragas-evaluation\data\testsets\rag\rag_eval_results.csv"
)

# Rename columns for simplicity
df_wide = df_wide.rename(
    columns={
        "gemini_factual_correctness(mode=f1)": "gemini_factual_correctness",
        "gpt_factual_correctness(mode=f1)": "gpt_factual_correctness",
        "gemini_non_llm_context_precision_with_reference": "gemini_context_precision",
        "gpt_non_llm_context_precision_with_reference": "gpt_context_precision",
    }
)

# For the scatterplot, we need metric pairs in the same dataframe
df_final_scatter = pd.concat(
    [
        df_wide[["gemini_factual_correctness", "gemini_semantic_similarity"]].rename(
            columns={
                "gemini_factual_correctness": "FactualCorrectness",
                "gemini_semantic_similarity": "SemanticSimilarity",
            }
        ),
        df_wide[["gpt_factual_correctness", "gpt_semantic_similarity"]].rename(
            columns={
                "gpt_factual_correctness": "FactualCorrectness",
                "gpt_semantic_similarity": "SemanticSimilarity",
            }
        ),
    ],
    ignore_index=True,
)

df_final_scatter["model"] = ["Gemini"] * len(df_wide) + ["GPT"] * len(df_wide)

# Boxplot of metrics by model
# First, melt the DataFrame for the boxplot
df_long = pd.melt(
    df_wide,
    value_vars=[
        "gemini_factual_correctness",
        "gpt_factual_correctness",
        "gemini_semantic_similarity",
        "gpt_semantic_similarity",
    ],
    var_name="metric",
    value_name="score",
)
df_long["model"] = df_long["metric"].apply(
    lambda x: "Gemini" if "gemini" in x else "GPT"
)
df_long["metric_name"] = df_long["metric"].apply(
    lambda x: "FactualCorrectness" if "factual" in x else "SemanticSimilarity"
)

# Descriptive table
print("Descriptive table:")
print(df_long.groupby(["model", "metric_name"])["score"].describe())

# ---

### Plots and Statistical Analysis

# Boxplot of metrics by model
plt.figure(figsize=(12, 5))
sns.boxplot(x="metric_name", y="score", hue="model", data=df_long)
plt.title("Boxplot of Metrics by Model")
plt.xlabel("Metric")
plt.ylabel("Score")
plt.tight_layout()
plt.show()


# Scatterplot
sns.lmplot(
    x="FactualCorrectness",
    y="SemanticSimilarity",
    hue="model",
    data=df_final_scatter,
    fit_reg=False,
    aspect=1.5,
)
plt.title("FactualCorrectness vs SemanticSimilarity")
plt.show()

# Statistical tests
gemini = df_final_scatter[df_final_scatter["model"] == "Gemini"]
gpt = df_final_scatter[df_final_scatter["model"] == "GPT"]

for metric in ["FactualCorrectness", "SemanticSimilarity"]:
    print(f"\nTest for {metric}:")
    # T-test
    t_stat, p_val_t = ttest_ind(gemini[metric], gpt[metric], equal_var=False)
    print(f"T-test: t={t_stat:.3f}, p={p_val_t:.4f}")
    if p_val_t < 0.05:
        print("Statistically significant difference (p < 0.05)")
    else:
        print("No statistically significant difference (p >= 0.05)")

    # Mann-Whitney
    u_stat, p_val_u = mannwhitneyu(gemini[metric], gpt[metric], alternative="two-sided")
    print(f"Mann-Whitney: U={u_stat:.3f}, p={p_val_u:.4f}")
