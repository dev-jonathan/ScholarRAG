import json
import pandas as pd

# --- Load raw JSON ---
with open(
    "data/testsets/human_eval/testset_human_eval_raw.json", "r", encoding="utf-8"
) as f:
    raw_data = json.load(f)

# --- Parse data into DataFrame ---
rows = []
for item in raw_data:
    data = item["data"]
    row = {
        "id": data.get("id"),
        "user_input": data.get("user_input"),
        "response": data.get("response"),
        "ragas_faithfulness": data.get("faithfulness"),
        "ragas_answer_relevancy": data.get("answer_relevancy"),
        "ragas_question_quality": data.get("question_quality"),
        "exclude_human_explicit": False,
        "human_faithfulness": None,
        "human_response_relevancy": None,
        "human_question_quality": None,
        "human_comments": "",
    }
    for annotation in item.get("annotations", []):
        for result in annotation.get("result", []):
            if result["from_name"] == "faithfulness" and result["type"] == "choices":
                choice_text = (
                    result["value"]["choices"][0] if result["value"]["choices"] else ""
                )
                try:
                    row["human_faithfulness"] = int(choice_text.split()[0])
                except Exception:
                    row["human_faithfulness"] = None
            elif (
                result["from_name"] == "response_relevancy"
                and result["type"] == "choices"
            ):
                choice_text = (
                    result["value"]["choices"][0] if result["value"]["choices"] else ""
                )
                try:
                    row["human_response_relevancy"] = int(choice_text.split()[0])
                except Exception:
                    row["human_response_relevancy"] = None
            elif (
                result["from_name"] == "simple_criteria_score"
                and result["type"] == "choices"
            ):
                choice_text = (
                    result["value"]["choices"][0] if result["value"]["choices"] else ""
                )
                try:
                    row["human_question_quality"] = int(choice_text.split()[0])
                except Exception:
                    row["human_question_quality"] = None
            elif (
                result["from_name"] == "remove_question" and result["type"] == "choices"
            ):
                if "Remove question" in result["value"]["choices"]:
                    row["exclude_human_explicit"] = True
            elif result["from_name"] == "comments" and result["type"] == "textarea":
                row["human_comments"] = (
                    result["value"]["text"][0] if result["value"]["text"] else ""
                )
    rows.append(row)

df = pd.DataFrame(rows)

# --- Convert columns to numeric ---
for col in [
    "ragas_faithfulness",
    "ragas_answer_relevancy",
    "ragas_question_quality",
    "human_faithfulness",
    "human_response_relevancy",
    "human_question_quality",
]:
    df[col] = pd.to_numeric(df[col], errors="coerce")

# --- Print basic statistics ---
print("=== Basic Statistics ===")
for col in [
    "ragas_faithfulness",
    "ragas_answer_relevancy",
    "ragas_question_quality",
    "human_faithfulness",
    "human_response_relevancy",
    "human_question_quality",
]:
    print(
        f"{col}: n={df[col].notna().sum()}, mean={df[col].mean():.3f}, std={df[col].std():.3f}, min={df[col].min()}, max={df[col].max()}"
    )
print()

# --- Print all samples explicitly excluded by human ---
print("=== Explicitly Excluded by Human ===")
explicit = df[df["exclude_human_explicit"] == True]
print(f"Total: {len(explicit)}")
for idx, row in explicit.iterrows():
    print(f"Sample {idx}:")
    print(
        f"  RAGAS scores - Faithfulness: {row['ragas_faithfulness']}, Answer Relevancy: {row['ragas_answer_relevancy']}, Question Quality: {row['ragas_question_quality']}"
    )
    print(
        f"  Human scores - Faithfulness: {row['human_faithfulness']}, Response Relevancy: {row['human_response_relevancy']}, Question Quality: {row['human_question_quality']}"
    )
    print(f"  User Input: {row['user_input'][:80]}...")
    print(f"  Response: {row['response'][:80]}...")
    print(f"  Comments: {row['human_comments']}")
    print()

# --- Print samples that should be excluded by human score (≤3) but were NOT explicitly excluded ---
print("=== Should be Excluded by Human Score (≤3) but NOT Explicitly ===")
mask = (
    (df["human_faithfulness"] <= 3)
    | (df["human_response_relevancy"] <= 3)
    | (df["human_question_quality"] <= 3)
) & (df["exclude_human_explicit"] == False)
score_excluded = df[mask]
print(f"Total: {len(score_excluded)}")
for idx, row in score_excluded.iterrows():
    print(f"Sample {idx}:")
    print(
        f"  RAGAS scores - Faithfulness: {row['ragas_faithfulness']}, Answer Relevancy: {row['ragas_answer_relevancy']}, Question Quality: {row['ragas_question_quality']}"
    )
    print(
        f"  Human scores - Faithfulness: {row['human_faithfulness']}, Response Relevancy: {row['human_response_relevancy']}, Question Quality: {row['human_question_quality']}"
    )
    print(f"  User Input: {row['user_input'][:80]}...")
    print(f"  Response: {row['response'][:80]}...")
    print(f"  Comments: {row['human_comments']}")
    print()
