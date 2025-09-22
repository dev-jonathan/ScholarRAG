import ast
import csv
import json
import os
import pandas as pd
import re

from ragas.metrics import (
    FactualCorrectness,
    SemanticSimilarity,
    NonLLMContextPrecisionWithReference,
)
from ragas import evaluate
from ragas.dataset_schema import EvaluationDataset, SingleTurnSample
from ragas.run_config import RunConfig

from src.models.models import (
    load_google_llm,
    load_lmstudio_embedding_model,
)

DATA_START_IDX = 33
DATA_END_IDX = 50

# --- Path and LLMs Configuration ---
input_jsonl_path = r"src\rag_with_both_llms.jsonl"
output_csv_path = rf"src\evaluation\eval_results_{DATA_START_IDX}_{DATA_END_IDX}.csv"
output_jsonl_path = (
    rf"src\evaluation\eval_results_{DATA_START_IDX}_{DATA_END_IDX}.jsonl"
)
os.makedirs(os.path.dirname(output_csv_path), exist_ok=True)

# Load your custom LLMs and embedding models
print("Loading Google Gemini model and embeddings...")
evaluator_llm = load_google_llm(model_name="gemini-2.0-flash", temperature=0.3)

try:
    embedding_model = load_lmstudio_embedding_model(
        model_name="text-embedding-qwen3-embedding-0.6b@f16"
    )
    ragas_embeddings = embedding_model
except Exception as e:
    print(f"Error loading embedding model: {e}. Check your configuration.")
    ragas_embeddings = None


def safe_list_eval(val):
    """Converts strings that look like lists into real lists, if possible."""
    if isinstance(val, list):
        return val
    if pd.isna(val) or val is None:
        return []
    try:
        evaluated = ast.literal_eval(val)
        return evaluated if isinstance(evaluated, list) else [evaluated]
    except (ValueError, SyntaxError):
        return [val]


def clean_gpt_response(response):
    """Removes <details ... </details> tag from the start of the response, if present."""
    if not isinstance(response, str):
        return response
    # Regex to match <details ...>...</details> at the start
    pattern = r"^\s*<details[\s\S]*?</details>\s*"
    return re.sub(pattern, "", response, count=1, flags=re.IGNORECASE)


def create_samples_for_model(df, model_name):
    """Creates a list of SingleTurnSample for a specific model."""
    samples = []
    response_col = f"response_{model_name.replace('/', '-').replace(':', '-')}"

    if response_col not in df.columns:
        print(
            f"Response column '{response_col}' not found in DataFrame. Skipping evaluation for this model."
        )
        return []

    for _, row in df.iterrows():
        response = row[response_col]
        # Special cleaning for GPT
        if "gpt" in model_name or "openai" in model_name:
            response = clean_gpt_response(response)
        sample = SingleTurnSample(
            user_input=row["user_input"],
            response=response,
            retrieved_contexts=safe_list_eval(row["retrieved_contexts"]),
            reference=row["reference"],
            reference_contexts=safe_list_eval(row["reference_contexts"]),
        )
        samples.append(sample)
    return samples


def get_model_prefix(model_name):
    """Generates a short, friendly prefix for the model name."""
    if "gemini" in model_name:
        return "gemini"
    elif "gpt" in model_name or "openai" in model_name:
        return "gpt"
    else:
        return model_name.replace("/", "_").replace(":", "_")


# --- Main execution flow ---
print("Loading input dataset from JSONL...")
records = []
with open(input_jsonl_path, "r", encoding="utf-8") as f:
    for line in f:
        records.append(json.loads(line))
df = pd.DataFrame(records)
print(f"Dataset loaded with {len(df)} rows.")

df = df.iloc[DATA_START_IDX:DATA_END_IDX]

# Define evaluation metrics
metrics_to_run = [
    FactualCorrectness(llm=evaluator_llm),
    SemanticSimilarity(embeddings=embedding_model),
    NonLLMContextPrecisionWithReference(),
]

run_config = RunConfig(
    max_workers=1,
    timeout=120,
    max_retries=10,
    max_wait=60,
    log_tenacity=True,
)


# Models to evaluate
llms_to_evaluate = ["gemini-2.0-flash", "openai/gpt-oss-20b:free"]

# DataFrame to store combined results
# Keeps the original columns from the DataFrame
final_results_df = df[
    ["user_input", "retrieved_contexts", "reference", "reference_contexts"]
].copy()

for model_name in llms_to_evaluate:
    print(f"\n--- Starting evaluation for model: {model_name} ---")

    samples = create_samples_for_model(df, model_name)
    if not samples:
        continue

    dataset = EvaluationDataset(samples)

    results = evaluate(
        dataset,
        metrics=metrics_to_run,
        run_config=run_config,
    )

    results_df = results.to_pandas()
    print("Columns in results_df:", results_df.columns)

    # Prepare a dictionary to rename columns
    prefix = get_model_prefix(model_name)

    # Iterate over metric column names to rename
    metrics_cols_to_rename = [
        "faithfulness",
        "answer_correctness",
        "response_relevancy",
        "factual_correctness(mode=f1)",
        "noise_sensitivity",
        "non_llm_context_precision_with_reference",
        "semantic_similarity",
    ]

    rename_dict = {
        col: f"{prefix}_{col}"
        for col in metrics_cols_to_rename
        if col in results_df.columns
    }

    # Add the model response column and renamed metric columns
    response_col_name = f"{prefix}_response"
    results_df[response_col_name] = [s.response for s in samples]

    # Ensure alignment by index
    results_df = results_df.set_index(df.index)

    # Concatenate result columns to the final DataFrame
    final_results_df = pd.concat(
        [
            final_results_df,
            results_df[[response_col_name] + list(rename_dict.keys())].rename(
                columns=rename_dict
            ),
        ],
        axis=1,
    )


# Save combined results to CSV and JSONL
if not final_results_df.empty:
    print("\nSaving combined results...")

    # CSV with quoting to preserve formatting
    final_results_df.to_csv(output_csv_path, index=False, quoting=csv.QUOTE_ALL)
    print(f"Evaluation completed. Results saved to '{output_csv_path}'.")

    # JSONL
    with open(output_jsonl_path, "w", encoding="utf-8") as f:
        for _, row in final_results_df.iterrows():
            json_record = json.dumps(row.to_dict(), ensure_ascii=False)
            f.write(json_record + "\n")
    print(f"Results also saved to '{output_jsonl_path}'.")
else:
    print("\nNo evaluation results were generated.")
