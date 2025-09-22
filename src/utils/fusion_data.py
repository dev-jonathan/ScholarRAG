import os
import json
import pandas as pd
import unicodedata
import csv
import ast

# Define the paths for your files
csv_path = r"data\testsets\processed\testset_final_unified.csv"
json_dir = r"data\testsets\model_rag_answers"
output_csv_path = r"src\rag_with_both_llms_formatted.csv"
output_jsonl_path = r"src\rag_with_both_llms.jsonl"


def normalize_text(text):
    """Normalizes text for matching, without affecting analysis."""
    if not isinstance(text, str):
        return ""
    text = text.replace("“", '"').replace("”", '"').replace("‘", "'").replace("’", "'")
    text = unicodedata.normalize("NFKC", text)
    text = " ".join(text.split())
    return text


def extract_json_data(json_path, target_models):
    """
    Extracts data for a single chat, handling multiple LLM responses.
    Returns the user input, a dictionary of LLM responses, and retrieval info.
    """
    try:
        with open(json_path, "r", encoding="utf-8") as f:
            data = json.load(f)
    except (json.JSONDecodeError, FileNotFoundError) as e:
        print(f"Erro ao ler o arquivo JSON {json_path}: {e}")
        return None, {}, [], "", [], []

    chat = data.get("chat", {})
    messages = chat.get("history", {}).get("messages", {})

    user_input = None
    llm_responses = {model: "" for model in target_models}
    retrieved_contexts = []
    distances = []
    sources = []
    chat_title = chat.get("title", "")

    user_msg_node = next(
        (msg for msg in messages.values() if msg.get("role") == "user"), None
    )
    if user_msg_node:
        user_input = user_msg_node.get("content")
    else:
        return None, {}, [], "", [], []

    for msg in messages.values():
        if (
            msg.get("role") == "assistant"
            and msg.get("parentId") == user_msg_node["id"]
        ):
            model_name = msg.get("modelName", "")

            if model_name in llm_responses:
                llm_responses[model_name] = msg.get("content", "")

            if not retrieved_contexts and "sources" in msg and msg["sources"]:
                src = msg["sources"][0]
                retrieved_contexts = src.get("document", [])
                distances = src.get("distances", [])

                meta = src.get("metadata", [])
                sources = [m.get("name") or "" for m in meta]

    return user_input, llm_responses, retrieved_contexts, chat_title, distances, sources


def clean_context_string(s):
    """Cleans a string representation of a list of contexts."""
    try:
        # Check if the string looks like a list
        if s and s.startswith("['") and s.endswith("']"):
            # Safely evaluate as a Python literal and join into a single string
            list_of_contexts = ast.literal_eval(s)
            return "\n\n---\n\n".join(list_of_contexts)
        return s
    except (ValueError, SyntaxError):
        # Return original string if evaluation fails
        return s


# --- Main script execution ---
print("Lendo o CSV de origem e pré-processando...")
df = pd.read_csv(csv_path)

# Correctly preprocess the reference_contexts column
df["reference_contexts"] = df["reference_contexts"].apply(clean_context_string)

llms_to_extract = ["gemini-2.0-flash", "openai/gpt-oss-20b:free"]
llm_column_names = {
    llm: f"response_{llm.replace('/', '-').replace(':', '-')}"
    for llm in llms_to_extract
}

# Prepare new columns in the DataFrame
df["retrieved_contexts"] = [None] * len(df)
df["distances"] = [None] * len(df)
df["sources"] = [None] * len(df)
df["chat_title"] = [None] * len(df)
df[llm_column_names[llms_to_extract[0]]] = [None] * len(df)
df[llm_column_names[llms_to_extract[1]]] = [None] * len(df)


json_data_map = {}
json_files = {
    f: os.path.join(json_dir, f) for f in os.listdir(json_dir) if f.endswith(".json")
}

print(f"Total de arquivos JSON encontrados: {len(json_files)}")
print("Pré-processando arquivos JSON para extração de dados...")
for json_file, json_path in json_files.items():
    user_input, llm_responses, contexts, title, distances, sources = extract_json_data(
        json_path, llms_to_extract
    )
    if user_input:
        user_input_norm = normalize_text(user_input)
        json_data_map[user_input_norm] = {
            "llm_responses": llm_responses,
            "contexts": contexts,
            "title": title,
            "distances": distances,
            "sources": sources,
        }

print(f"Total de linhas no CSV: {len(df)}")
print("Unindo dados do CSV e JSONs...")
for idx, row in df.iterrows():
    user_input_csv_norm = normalize_text(row["user_input"])

    if user_input_csv_norm in json_data_map:
        json_data = json_data_map[user_input_csv_norm]

        for llm in llms_to_extract:
            df.at[idx, llm_column_names[llm]] = json_data["llm_responses"].get(llm, "")

        df.at[idx, "retrieved_contexts"] = json_data["contexts"]
        df.at[idx, "chat_title"] = json_data["title"]
        df.at[idx, "distances"] = json_data["distances"]
        df.at[idx, "sources"] = json_data["sources"]
        print(
            f"[{idx+1}/{len(df)}] Match encontrado e dados extraídos para o user_input."
        )
    else:
        print(
            f"[{idx+1}/{len(df)}] Nenhum JSON correspondente encontrado para o user_input."
        )


def save_to_jsonl(dataframe, filename):
    """Saves DataFrame to JSONL, ensuring list-like columns are handled."""
    with open(filename, "w", encoding="utf-8") as f:
        for _, row in dataframe.iterrows():
            record = row.to_dict()
            # Ensure list-like columns are properly formatted as lists
            for key in [
                "retrieved_contexts",
                "distances",
                "sources",
                "reference_contexts",
            ]:
                if key in record and isinstance(record[key], str):
                    try:
                        record[key] = ast.literal_eval(record[key])
                    except (ValueError, SyntaxError):
                        pass  # Keep as string if it fails

            # Use json.dumps to handle newlines and special characters correctly
            json_record = json.dumps(record, ensure_ascii=False)
            f.write(json_record + "\n")
    print(f"Dados salvos com sucesso em {filename}")


print("\nSalvando em JSONL...")
save_to_jsonl(df, output_jsonl_path)

print("Salvando em CSV...")
df.to_csv(output_csv_path, index=False, quoting=csv.QUOTE_ALL)
print("Processo de exportação concluído.")
