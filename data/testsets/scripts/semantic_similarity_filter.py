import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
import asyncio
import os
import logging
from sentence_transformers import SentenceTransformer
from collections import deque

# --- Logging Configuration ---
logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
logger = logging.getLogger(__name__)

# --- Configuration Constants ---
DATA_FILE_PATH = os.path.join("data", "testsets", "testset_raw_unified.csv")
QUESTION_COLUMN = "user_input"
SIMILARITY_THRESHOLD = 0.78
NUM_QUESTIONS_TO_PROCESS = None  # Set to None to process all questions


# --- Script Functions ---
async def get_embeddings(texts: list[str], embedding_model) -> np.ndarray:
    """
    Generates embeddings for a list of texts using SentenceTransformer.
    Uses run_in_executor to avoid blocking the event loop during synchronous operations.
    """
    if not texts:
        logger.warning("No valid texts for embedding generation.")
        return np.array([])

    loop = asyncio.get_event_loop()
    embeddings = await loop.run_in_executor(
        None,  # Use the default ThreadPoolExecutor
        lambda: embedding_model.encode(
            texts,
            convert_to_numpy=True,
            normalize_embeddings=True,
            show_progress_bar=True,
        ),
    )
    return embeddings


async def find_similar_questions(
    questions: list[str], threshold: float, embedding_model
) -> list[dict]:
    """
    Calculates cosine similarity between all question pairs and returns those above the threshold.
    """
    if not questions:
        logger.info("Question list is empty, cannot find similar questions.")
        return []

    logger.info(f"Generating embeddings for {len(questions)} questions...")
    embeddings = await get_embeddings(questions, embedding_model)

    if embeddings.size == 0:
        logger.warning("Embeddings are empty, cannot calculate similarity.")
        return []

    logger.info("Calculating cosine similarity matrix...")
    similarity_matrix = cosine_similarity(embeddings)

    similar_pairs = []
    n = len(questions)

    logger.info(f"Identifying pairs with similarity >= {threshold:.2f}...")
    for i in range(n):
        for j in range(
            i + 1, n
        ):  # Compare each question only once with subsequent ones
            score = similarity_matrix[i, j]
            if score >= threshold:
                similar_pairs.append(
                    {
                        "index_q1": i,
                        "text_q1": questions[i],
                        "index_q2": j,
                        "text_q2": questions[j],
                        "score": score,
                    }
                )
    return similar_pairs


def deduplicate_questions(
    questions: list[str], similar_pairs: list[dict]
) -> tuple[list[str], list[int]]:
    """
    Deduplicates questions by grouping them by similarity and selecting a representative for each group.
    Returns the list of unique questions and the indices of removed questions.
    """
    num_questions = len(questions)

    # Create adjacency list to represent similarity connections
    adj_list = {i: [] for i in range(num_questions)}
    for pair in similar_pairs:
        q1_idx = pair["index_q1"]
        q2_idx = pair["index_q2"]
        adj_list[q1_idx].append(q2_idx)
        adj_list[q2_idx].append(q1_idx)  # Similarity is reciprocal

    visited = [False] * num_questions
    final_unique_questions_texts = []
    removed_questions_indices = []

    logger.info(
        "\n--- Starting Deduplication and Representative Identification Process ---"
    )
    for i in range(num_questions):
        if not visited[i]:
            representative_idx = i
            representative_text = questions[representative_idx]
            final_unique_questions_texts.append(representative_text)
            logger.info(
                f"Group Representative (Q{representative_idx}): '{representative_text}'"
            )

            queue = deque([representative_idx])
            visited[representative_idx] = True

            while queue:
                current_q_idx = queue.popleft()

                for neighbor_idx in adj_list[current_q_idx]:
                    if not visited[neighbor_idx]:
                        visited[neighbor_idx] = True
                        queue.append(neighbor_idx)
                        removed_questions_indices.append(
                            neighbor_idx
                        )  # Add the index of the removed question
                        logger.info(
                            f"  Removed Q{neighbor_idx}: '{questions[neighbor_idx]}' (similar to Q{representative_idx})"
                        )
    logger.info("--- Deduplication Process Completed ---")
    return final_unique_questions_texts, removed_questions_indices


# --- Main Execution ---
async def main():
    """Executes the semantic similarity detection and deduplication process."""
    logger.info("Starting semantic similarity and deduplication script.")

    try:
        df = pd.read_csv(DATA_FILE_PATH)
        all_questions = df[QUESTION_COLUMN].tolist()
        logger.info(f"Total questions loaded: {len(all_questions)}")
    except Exception as e:
        logger.error(f"Error loading data from file '{DATA_FILE_PATH}': {e}")
        return

    questions_to_process = all_questions
    if NUM_QUESTIONS_TO_PROCESS is not None and NUM_QUESTIONS_TO_PROCESS < len(
        all_questions
    ):
        questions_to_process = all_questions[:NUM_QUESTIONS_TO_PROCESS]
        logger.info(
            f"Limiting processing to the first {NUM_QUESTIONS_TO_PROCESS} questions."
        )

    try:
        embedding_model = SentenceTransformer("Qwen/Qwen3-Embedding-0.6B")
        logger.info(f"Embedding model '{embedding_model}' loaded successfully.")
    except Exception as e:
        logger.error(f"Error loading embedding model 'Qwen/Qwen3-Embedding-0.6B': {e}")
        logger.error("Please ensure the model is downloaded and configured correctly.")
        return

    # 1. Find all similar pairs
    similar_pairs = await find_similar_questions(
        questions_to_process, SIMILARITY_THRESHOLD, embedding_model
    )

    # --- Print similar pairs found before deduplication ---
    # if similar_pairs:
    #     logger.info(
    #         f"\n--- Details of {len(similar_pairs)} similar pairs found (threshold={SIMILARITY_THRESHOLD:.2f}): ---"
    #     )
    #     for pair in similar_pairs:
    #         logger.info(f"--- Similarity: {pair['score']:.3f} ---")
    #         logger.info(f"Q{pair['index_q1']}: {pair['text_q1']}")
    #         logger.info(f"Q{pair['index_q2']}: {pair['text_q2']}\n")
    # else:
    #     logger.info(
    #         f"No similar pairs found with threshold={SIMILARITY_THRESHOLD:.2f} before deduplication."
    #     )

    # 2. Deduplicate questions based on similar pairs
    final_unique_questions, removed_indices = deduplicate_questions(
        questions_to_process, similar_pairs
    )

    logger.info(
        f"\n--- Details of {len(similar_pairs)} similar pairs found (threshold={SIMILARITY_THRESHOLD:.2f}): ---"
    )
    logger.info(f"\n--- Deduplication Summary ---")
    logger.info(f"Original dataset size: {len(questions_to_process)} questions")
    logger.info(
        f"Dataset size after deduplication: {len(final_unique_questions)} unique questions"
    )
    logger.info(
        f"Number of questions removed: {len(questions_to_process) - len(final_unique_questions)}"
    )
    logger.info(f"First 5 final unique questions: {final_unique_questions[:5]}...")

    # --- NEW: Print indices of removed questions ---
    logger.info(f"\nIndices of removed questions: {removed_indices}")


# --- Script Entry Point ---
if __name__ == "__main__":
    asyncio.run(main())
