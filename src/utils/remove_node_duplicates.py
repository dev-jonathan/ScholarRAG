import json
import glob
import os

# Caminho dos arquivos JSON (agora pega todos os arquivos desejados)
json_files = glob.glob("knowledge_graph_week_*.json")

for file_path in json_files:
    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    if "nodes" in data:
        seen_ids = set()
        unique_nodes = []
        for node in data["nodes"]:
            node_id = node.get("id")
            if node_id and node_id not in seen_ids:
                unique_nodes.append(node)
                seen_ids.add(node_id)
        if len(unique_nodes) != len(data["nodes"]):
            print(
                f"Removendo duplicatas em {file_path}: {len(data['nodes']) - len(unique_nodes)} removidas"
            )
        data["nodes"] = unique_nodes

        # Salva o arquivo corrigido (sobrescreve o original)
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
    else:
        print(f"'nodes' não encontrado em {file_path}")
