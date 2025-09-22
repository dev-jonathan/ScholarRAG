import ast
import os
import pandas as pd
from ragas.dataset_schema import SingleTurnSample, EvaluationDataset
from ragas import evaluate
from ragas.metrics import (
    Faithfulness,
    SimpleCriteriaScore,
    ResponseRelevancy,
)
from src.models.models import load_google_llm, load_hf_embedding_model
from ragas.run_config import RunConfig

# Path to the data file
DATA_FILE_PATH = os.path.join("data", "testsets", "processed", "testset_stratified.csv")

# Load the dataset
print("Loading dataset...")
df = pd.read_csv(DATA_FILE_PATH)

# Row interval (adjust as needed)
# df = df.iloc[0:30]
# df = df.iloc[90:120]
selected_indices = [90]

# Select specific rows
df = df.iloc[selected_indices]


# Function to ensure contexts are lists
def safe_list(val):
    if isinstance(val, list):
        return val
    if pd.isna(val):
        return []
    try:
        return ast.literal_eval(val)
    except Exception:
        return [val] if isinstance(val, str) and val else []


# Convert to EvaluationDataset
samples = [
    SingleTurnSample(
        user_input=row["user_input"],
        response=row["reference"],
        retrieved_contexts=safe_list(row["reference_contexts"]),
    )
    for _, row in df.iterrows()
]
dataset = EvaluationDataset(samples)

# Load Google Gemini LLM and embedding model
print("Loading Google Gemini model and embeddings...")
evaluator_llm = load_google_llm(model_name="gemini-2.0-flash", temperature=0.3)
embedding_model = load_hf_embedding_model(model_name="Qwen/Qwen3-Embedding-0.6B")

# Define SimpleCriteriaScore for question quality with respect to context
question_quality = SimpleCriteriaScore(
    name="question_quality",
    definition=(
        "Score from 0 to 5 the following question based on how clear, relevant, and well-grounded it is in the provided context(s).\n"
        "A score of 0 means the question is completely unrelated or nonsensical given the context.\n"
        "A score of 1 means the question is barely related or very unclear.\n"
        "A score of 2 means the question is somewhat related but lacks clarity or relevance.\n"
        "A score of 3 means the question is generally relevant and clear, but could be improved.\n"
        "A score of 4 means the question is clear and relevant, with minor issues.\n"
        "A score of 5 means the question is perfectly clear, highly relevant, and directly based on the context.\n"
        "Consider whether the question could plausibly be asked by a real student after reading the context. "
        "Examples:\n"
        "0: 'What is the capital of France?' (context: JavaScript arrays)\n"
        "1: 'Explain arrays in JavaScript.' (context: JavaScript variables)\n"
        "3: 'How do you declare a variable in JavaScript?' (context: JavaScript variables, but question is vague)\n"
        "5: 'What is the difference between let and var in JavaScript?' (context: variable declarations)\n"
        "Answer only with a number from 0 to 5 (likert scale)."
    ),
    llm=evaluator_llm,
)


# Instantiate metrics
metrics = [
    Faithfulness(llm=evaluator_llm),
    ResponseRelevancy(llm=evaluator_llm, embeddings=embedding_model),
    question_quality,
]

run_config = RunConfig(
    max_workers=1,
    timeout=60,
    max_retries=5,
    max_wait=30,
    log_tenacity=True,
)

# Evaluate
print("Running automatic evaluation with Ragas...")
results = evaluate(
    dataset,
    metrics=metrics,
    embeddings=embedding_model,
    run_config=run_config,
)

results_df = results.to_pandas()

start, stop = df.index[0], df.index[-1]

# Save results
output_path = os.path.join(
    "data", "testsets", f"testset_stratified_eval_{start}-{stop}.csv"
)
results_df.to_csv(output_path, index=False)
print(f"Results saved to {output_path}")
