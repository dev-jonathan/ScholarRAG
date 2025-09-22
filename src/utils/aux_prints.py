import json


def print_graph_summary(json_path):
    with open(json_path, "r", encoding="utf-8") as f:
        graph = json.load(f)

    nodes = graph.get("nodes", [])
    relationships = graph.get("relationships", [])

    num_documents = 0
    num_chunks = 0

    print(f"\n[INFO] Total de nós: {len(nodes)}")
    print(f"[INFO] Total de relações: {len(relationships)}")

    print("\n[DETAIL] Metadados dos nós do tipo 'document':")
    for node in nodes:
        node_type = node.get("type") or node.get("properties", {}).get("type")
        if node_type == "document":
            num_documents += 1
            metadata = node.get("properties", {}).get("document_metadata", {})
            print(f"  - title: {metadata.get('title')}")
            print(f"    type: {metadata.get('document_type')}")
            print(f"    week: {metadata.get('week')}")
            print(f"    path: {metadata.get('path')}")
            print(f"    original_link: {metadata.get('original_link')}")
            print(f"    related_files: {metadata.get('related_files')}\n")
        elif node_type == "chunk":
            num_chunks += 1

    print(f"\n[SUMMARY] Nós do tipo 'document': {num_documents}")
    print(f"[SUMMARY] Nós do tipo 'chunk': {num_chunks}")


if __name__ == "__main__":
    print_graph_summary(r"src\graphs\knowledge_graph_week_3.json")
