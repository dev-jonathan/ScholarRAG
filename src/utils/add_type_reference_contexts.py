import pandas as pd
import json
import ast

GRAPH_PATH = "src/graphs/knowledge_graph_week_5.json"
TESTSET_CSV = "src/testset_week_5.csv"
OUTPUT_CSV = "src/testset_week_5_with_type.csv"

# 1. Carregar grafo
with open(GRAPH_PATH, "r", encoding="utf-8") as f:
    graph = json.load(f)

# 2. Criar dict: page_content -> type
content_type_map = {}
for node in graph["nodes"]:
    content = node["properties"].get("page_content", "")
    node_type = node.get("type", "").lower()
    content_type_map[content.strip()] = node_type

# 3. Carregar testset
df = pd.read_csv(TESTSET_CSV)


def get_type(ref_contexts):
    # ref_contexts é uma string de lista, ex: '["texto markdown..."]'
    try:
        contexts = ast.literal_eval(ref_contexts)
        if isinstance(contexts, list) and contexts:
            context = contexts[0].strip()
            # Busca exata
            if context in content_type_map:
                return content_type_map[context]
            # Busca por substring (caso haja pequenas diferenças)
            for k in content_type_map:
                if context == k or context in k or k in context:
                    return content_type_map[k]
    except Exception:
        pass
    return "unknown"


# 4. Aplicar função e salvar novo CSV
df["type_reference_contexts"] = df["reference_contexts"].apply(get_type)
df.to_csv(OUTPUT_CSV, index=False)
print(f"Arquivo salvo em {OUTPUT_CSV}")
