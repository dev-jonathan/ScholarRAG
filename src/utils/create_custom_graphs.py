import os
import json
import shutil

# --- CONFIGURAÇÕES ---
# Assumindo que este script está em um diretório como 'scripts' e a pasta 'graphs' está um nível acima.
# Ajuste se a estrutura do seu projeto for diferente.
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SOURCE_GRAPH_DIR = os.path.abspath(os.path.join(BASE_DIR, "..", "graphs"))
CUSTOM_GRAPH_DIR = os.path.join(SOURCE_GRAPH_DIR, "custom")
DOCUMENT_TYPE_TO_REMOVE = "transcription"


def create_custom_graph(source_path, output_path):
    """
    Lê um grafo, remove os nós do tipo 'transcription' e seus chunks filhos,
    e salva o novo grafo no caminho de saída.
    """
    print(f"Processando: {os.path.basename(source_path)}")

    # 1. Carregar o grafo original
    with open(source_path, "r", encoding="utf-8") as f:
        graph = json.load(f)

    # 2. Identificar todos os nós que devem ser removidos
    ids_to_remove = set()
    transcription_parent_ids = set()

    # --- PASSO A: Encontrar os nós de documento 'transcription' ---
    for node in graph["nodes"]:
        try:
            # Verifica se é um nó de documento e se o tipo é o que queremos remover
            if (
                node.get("type") == "document"
                and node["properties"].get("document_metadata", {}).get("document_type")
                == DOCUMENT_TYPE_TO_REMOVE
            ):
                node_id = node.get("id")
                if node_id:
                    ids_to_remove.add(node_id)
                    transcription_parent_ids.add(node_id)
        except (KeyError, AttributeError):
            # Ignora nós que não têm a estrutura esperada
            continue

    if not transcription_parent_ids:
        print(
            f"  -> Nenhum nó do tipo '{DOCUMENT_TYPE_TO_REMOVE}' encontrado. Copiando o arquivo original."
        )
        shutil.copy(source_path, output_path)
        return

    print(
        f"  -> Encontrados {len(transcription_parent_ids)} nós '{DOCUMENT_TYPE_TO_REMOVE}' para remover."
    )

    # --- PASSO B: Encontrar os nós 'chunk' que são filhos dos nós de transcrição ---
    chunks_removed_count = 0
    for relationship in graph.get("relationships", []):
        # Verifica se é uma relação 'child' e se o pai (source) é um dos nós de transcrição
        if (
            relationship.get("type") == "child"
            and relationship.get("source") in transcription_parent_ids
        ):
            child_id = relationship.get("target")
            if child_id:
                ids_to_remove.add(child_id)
                chunks_removed_count += 1

    print(f"  -> Encontrados {chunks_removed_count} chunks filhos para remover.")

    # 3. Construir o novo grafo filtrado
    custom_graph = {
        # Copia metadados do nível superior, se existirem (ex: version)
        **{k: v for k, v in graph.items() if k not in ["nodes", "relationships"]},
        "nodes": [],
        "relationships": [],
    }

    # Manter apenas os nós cujos IDs NÃO estão na lista de remoção
    custom_graph["nodes"] = [
        node for node in graph["nodes"] if node.get("id") not in ids_to_remove
    ]

    # Manter apenas as relações onde AMBOS, source e target, ainda existem no grafo
    custom_graph["relationships"] = [
        rel
        for rel in graph.get("relationships", [])
        if rel.get("source") not in ids_to_remove
        and rel.get("target") not in ids_to_remove
    ]

    # 4. Salvar o novo grafo
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(custom_graph, f, indent=2, ensure_ascii=False)

    print(f"  -> Grafo customizado salvo em: {output_path}")
    print(
        f"  -> Resumo: {len(graph['nodes'])} -> {len(custom_graph['nodes'])} nós | {len(graph['relationships'])} -> {len(custom_graph['relationships'])} relações"
    )


def main():
    """
    Função principal que encontra todos os grafos e inicia o processo de customização.
    """
    print("=" * 60)
    print("INICIANDO SCRIPT PARA CRIAR GRAFOS CUSTOMIZADOS (SEM TRANSCRIÇÕES)")
    print(f"Diretório de origem: {SOURCE_GRAPH_DIR}")
    print(f"Diretório de destino: {CUSTOM_GRAPH_DIR}")
    print("=" * 60)

    # Criar o diretório de destino se ele não existir
    os.makedirs(CUSTOM_GRAPH_DIR, exist_ok=True)

    # Listar todos os arquivos JSON no diretório de origem
    try:
        files_in_source = os.listdir(SOURCE_GRAPH_DIR)
    except FileNotFoundError:
        print(f"ERRO: O diretório de origem '{SOURCE_GRAPH_DIR}' não foi encontrado.")
        return

    graph_files = [
        f
        for f in files_in_source
        if f.startswith("knowledge_graph_week_") and f.endswith(".json")
    ]

    if not graph_files:
        print(
            "Nenhum arquivo de grafo (`knowledge_graph_week_*.json`) encontrado para processar."
        )
        return

    for filename in graph_files:
        source_file_path = os.path.join(SOURCE_GRAPH_DIR, filename)

        # Montar o novo nome do arquivo
        custom_filename = f"custom_{filename}"
        output_file_path = os.path.join(CUSTOM_GRAPH_DIR, custom_filename)

        create_custom_graph(source_file_path, output_file_path)
        print("-" * 20)

    print("\n" + "#" * 60)
    print("PROCESSO DE CUSTOMIZAÇÃO DE GRAFOS CONCLUÍDO!")
    print("#" * 60)


if __name__ == "__main__":
    main()
