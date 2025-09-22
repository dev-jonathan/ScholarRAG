from .graph_utils import (
    load_documents_from_csv,
    create_knowledge_graph,
    transform_knowledge_graph,
)


def build_and_save_graph(csv_path, week, llm, output_path):
    docs = load_documents_from_csv(csv_path, week)
    print(f"[INFO] {len(docs)} documentos carregados. Week: {week}")
    kg = create_knowledge_graph(docs)
    print(f"[INFO] Grafo inicial criado com {len(kg.nodes)} nós.")
    kg = transform_knowledge_graph(kg, llm)
    # kg = transform_knowledge_graph(kg, llm, embedding_model)

    print(f"[INFO] {len(docs)} documentos carregados. Week: {week}")
    print(
        f"[INFO] Total de nós após transformação: {len(kg.nodes)} e {len(kg.relationships)} relações."
    )

    # Count nodes of type 'document' and 'chunk'
    num_documents = sum(
        1 for node in kg.nodes if getattr(node, "type", None) == "document"
    )
    num_chunks = sum(1 for node in kg.nodes if getattr(node, "type", None) == "chunk")

    print(f"[SUMMARY] Nós do tipo 'document': {num_documents}")
    print(f"[SUMMARY] Nós do tipo 'chunk': {num_chunks}")

    # Print details of each document node's metadata
    print("\n[DETAIL] Metadados dos nós do tipo 'document':")
    for node in kg.nodes:
        if getattr(node, "type", None) == "document":
            metadata = node.properties.get("document_metadata", {})
            print(f"  - title: {metadata.get('title')}")
            print(f"    type: {metadata.get('document_type')}")
            print(f"    week: {metadata.get('week')}")
            print(f"    path: {metadata.get('path')}")
            print(f"    original_link: {metadata.get('original_link')}")

    kg.save(output_path)
    print(f"[SUCCESS] Grafo de conhecimento salvo em: {output_path}\n")
    return kg
