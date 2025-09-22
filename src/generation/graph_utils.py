import os
import logging
from langchain_community.document_loaders import TextLoader
from ragas.testset.graph import KnowledgeGraph, Node, NodeType
import pandas as pd

logger = logging.getLogger(__name__)


def create_knowledge_graph(docs):
    kg = KnowledgeGraph()
    kg.nodes.extend(docs)

    return kg


def load_documents_from_csv(csv_path, week):
    df = pd.read_csv(csv_path)
    df_week = df[df["week"].astype(str) == str(week)]
    docs = []
    for _, row in df_week.iterrows():
        docs.append(
            Node(
                type=NodeType.DOCUMENT,
                properties={
                    "page_content": row["content"],
                    "document_metadata": {
                        "document_type": row["type"],
                        "week": row["week"],
                        "title": row["title"],
                        "original_link": row["link"],
                        "related_files": row.get("related_files"),
                        "path": row.get("path"),
                    },
                },
            )
        )
    return docs


def transform_knowledge_graph(kg, llm):
    from ragas.testset.transforms import Parallel, apply_transforms
    from ragas.testset.transforms import (
        HeadlinesExtractor,
        HeadlineSplitter,
        KeyphrasesExtractor,
        # OverlapScoreBuilder,
    )

    headline_extractor = HeadlinesExtractor(llm=llm, max_num=10)
    headline_splitter = HeadlineSplitter(min_tokens=600, max_tokens=2000)
    keyphrase_extractor = KeyphrasesExtractor(
        llm=llm,
        property_name="keyphrases",
        max_num=10,
    )

    # added in the relationship builder
    # overlap_builder = OverlapScoreBuilder(
    #     property_name="keyphrases",
    #     new_property_name="overlap_score",
    #     threshold=0.01,
    #     distance_threshold=0.9,
    # )

    transforms = [
        # Parallel(headline_extractor, headline_splitter, keyphrase_extractor),
        headline_extractor,
        headline_splitter,
        keyphrase_extractor,
        # overlap_builder,
    ]

    apply_transforms(kg, transforms=transforms)
    return kg


# Old used function, kept for reference/compatibility
# def load_documents_from_files(
#     data_dir=r"C:\Users\Jonathan\Desktop\pet\ragas-evaluation\data",
# ):
#     docs = []
#     for week in range(1):  # index week
#         week_dir = os.path.join(data_dir, f"week-{week}")
#         transcription_path = os.path.join(week_dir, f"week-{week}-transcription.md")
#         notes_path = os.path.join(week_dir, f"week-{week}-notes.md")
#         problemset_path = os.path.join(
#             week_dir, os.path.join("problemset", f"week-{week}-problemset.md")
#         )

#         try:
#             docs.extend(TextLoader(transcription_path, encoding="utf-8").load())
#             docs.extend(TextLoader(notes_path, encoding="utf-8").load())
#             docs.extend(TextLoader(problemset_path, encoding="utf-8").load())

#             # Load exercises
#             problemset_dir = os.path.join(week_dir, "problemset")
#             for filename in os.listdir(problemset_dir):
#                 if (
#                     filename.endswith(".md")
#                     and filename != f"week-{week}-problemset.md"
#                 ):
#                     exercise_path = os.path.join(problemset_dir, filename)
#                     docs.extend(TextLoader(exercise_path, encoding="utf-8").load())
#         except FileNotFoundError as e:
#             print(f"Arquivo não encontrado: {e}")
#         except UnicodeDecodeError as e:
#             print(f"Erro de codificação ao ler o arquivo: {e}")
#     logger.debug(f"Total de documentos carregados: {len(docs)}")

#     nodes = []
#     for doc in docs:
#         nodes.append(
#             Node(
#                 type=NodeType.DOCUMENT,
#                 properties={
#                     "page_content": doc.page_content,
#                     "document_metadata": doc.metadata,
#                 },
#             )
#         )
#     return nodes
