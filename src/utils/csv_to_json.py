# import pandas as pd

# csv_path = "./data/testsets/processed/testset_final_unified.csv"
# json_path = "./data/testsets/processed/testset_final_unified.json"

# df = pd.read_csv(csv_path, encoding="utf-8")
# df.to_json(json_path, orient="records", force_ascii=False, indent=2)

# print(f"Arquivo salvo em: {json_path}")
import pandas as pd
import tiktoken


# Função para contar tokens usando tiktoken
def count_tokens(text):
    enc = tiktoken.get_encoding("cl100k_base")
    return len(enc.encode(text))


csv_path = "./data/testsets/processed/testset_final_unified.csv"
df = pd.read_csv(csv_path, encoding="utf-8")

# Aplicar contagem de tokens na coluna 'reference'
token_counts = df["reference"].astype(str).apply(count_tokens)

media_tokens = token_counts.mean()
min_tokens = token_counts.min()
max_tokens = token_counts.max()

print(f"Média de tokens: {media_tokens}")
print(f"Mínimo de tokens: {min_tokens}")
print(f"Máximo de tokens: {max_tokens}")
