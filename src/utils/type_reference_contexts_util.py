import pandas as pd
import json
import ast
import re


def normalize_text(text):
    """
    Substitui qualquer sequência de espaços em branco (incluindo \n, \t, etc.)
    por um único espaço e remove espaços no início/fim.
    """
    if not isinstance(text, str):
        return ""
    return re.sub(r"\s+", " ", text).strip()


def add_reference_context_info(graph_path, testset_csv, output_csv=None):
    # 1. Carregar grafo
    with open(graph_path, "r", encoding="utf-8") as f:
        graph = json.load(f)

    # --- ETAPA DE PRÉ-PROCESSAMENTO AVANÇADO ---
    # Vamos criar mais mapas para facilitar as buscas estruturais

    # Mapas para match de texto (como antes)
    content_type_map = {}
    content_path_map = {}

    # Mapas para busca estrutural (usando IDs)
    id_to_node_map = {}
    normalized_content_to_id_map = {}
    child_to_parent_map = (
        {}
    )  # Mapeia ID do chunk (target) para ID do documento (source)

    # 2. Iterar sobre os NÓS para popular os mapas
    document_nodes = []  # Ainda útil para o fallback de texto
    for node in graph["nodes"]:
        node_id = node.get("id")
        content = node["properties"].get("page_content", "")
        normalized_content = normalize_text(content)

        if not node_id or not normalized_content:
            continue

        # Popular mapas baseados em ID
        id_to_node_map[node_id] = node
        normalized_content_to_id_map[normalized_content] = node_id

        # Popular mapas baseados em conteúdo
        node_type = node.get("type", "").lower()
        path = node["properties"].get("document_metadata", {}).get("path", "")
        content_type_map[normalized_content] = node_type
        content_path_map[normalized_content] = path

        if node_type == "document":
            document_nodes.append((normalized_content, path))

    # 3. Iterar sobre os RELACIONAMENTOS para mapear filhos aos pais
    for rel in graph.get("relationships", []):
        if rel.get("type") == "child" and rel.get("source") and rel.get("target"):
            # O source é o documento pai, o target é o chunk filho
            child_id = rel["target"]
            parent_id = rel["source"]
            child_to_parent_map[child_id] = parent_id

    # 4. Carregar testset
    df = pd.read_csv(testset_csv)

    # A função get_type pode permanecer a mesma, pois o match de texto é suficiente
    def get_type(ref_contexts):
        try:
            contexts = ast.literal_eval(ref_contexts)
            if isinstance(contexts, list) and contexts:
                context = normalize_text(contexts[0])
                if context in content_type_map:
                    return content_type_map[context]
                for k_norm, v_type in content_type_map.items():
                    if context in k_norm or k_norm in context:
                        return v_type
        except Exception:
            pass
        return "unknown"

    def get_path(ref_contexts):
        try:
            contexts = ast.literal_eval(ref_contexts)
            if not (isinstance(contexts, list) and contexts):
                return ""

            context = normalize_text(contexts[0])
            if not context:
                return ""

            # --- ESTRATÉGIA 1: Match de Texto Normalizado (Rápido) ---
            if context in content_path_map and content_path_map[context]:
                return content_path_map[context]

            for doc_content_normalized, doc_path in document_nodes:
                if context in doc_content_normalized:
                    return doc_path

            # --- ESTRATÉGIA 2: Fallback usando a Estrutura do Grafo (Preciso) ---
            # Se o match de texto falhou, vamos usar os IDs e relações

            # a. Encontrar o ID do chunk pelo seu conteúdo
            chunk_id = normalized_content_to_id_map.get(context)
            if not chunk_id:
                # Se nem sequer encontramos um nó com este conteúdo, não há mais o que fazer
                return ""

            # b. Encontrar o ID do pai usando o mapa de relações
            parent_id = child_to_parent_map.get(chunk_id)
            if not parent_id:
                # O chunk existe mas não tem uma relação 'child' apontando para ele
                return ""

            # c. Obter o nó do pai pelo seu ID
            parent_node = id_to_node_map.get(parent_id)
            if not parent_node:
                return ""

            # d. Extrair o path do nó pai (que deve ser um documento)
            parent_path = (
                parent_node["properties"].get("document_metadata", {}).get("path", "")
            )
            return parent_path

        except Exception as e:
            # print(f"Erro em get_path: {e} para o contexto: {ref_contexts[:100]}...") # Descomente para depurar
            pass
        return ""

    # 5. Aplicar funções
    df["reference_context_type"] = df["reference_contexts"].apply(get_type)
    df["reference_context_path"] = df["reference_contexts"].apply(get_path)

    desired_order = [
        "user_input",  # A entrada ou pergunta do usuário (gerado sinteticamente pelo ragas simulando um aluno).
        "reference",  # A resposta de referência ou gabarito para a entrada do usuário (gerado tbm sinteticamente por llm).
        "reference_contexts",  # Contextos (trechos dos documentos do curso educacional) usados para gerar a referência.
        "reference_context_type",  # O tipo do nó do grafo ao qual o contexto de referência pertence (ex: 'document', 'chunk').
        "reference_context_path",  # O caminho (path) do documento de origem do contexto de referência.
        "persona_name",  # O nome da persona associada à consulta.
        "query_style",  # O estilo da consulta (ex: 'informativo', 'transacional').
        "query_length",  # O comprimento da consulta do usuário.
        "synthesizer_name",  # O nome do sintetizador ou modelo usado para gerar a resposta.
    ]
    cols = [col for col in desired_order if col in df.columns] + [
        col for col in df.columns if col not in desired_order
    ]
    df = df[cols]

    # 7. Salvar
    if output_csv is None:
        output_csv = testset_csv
    df.to_csv(output_csv, index=False)
    print(f"Arquivo salvo em {output_csv}")
