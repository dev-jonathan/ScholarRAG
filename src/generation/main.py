import os
import time

from ragas.testset.graph import KnowledgeGraph

from ..models.models import (
    load_google_llm,
    load_lmstudio_embedding_model,
)
from .graph_builder import build_and_save_graph
from .question_generator import generate_questions
from ..utils.type_reference_contexts_util import add_reference_context_info

# Change the variable to a list of weeks
SELECTED_WEEKS = [
    "9",
    "10",
    "ai",
]  # Add here all the weeks you want to process
NUM_QUESTIONS_PER_TESTSET = 15
WAIT_TIME_MINUTES = 2  # Set the wait time as a clear constant
WAIT_TIME_SECONDS = WAIT_TIME_MINUTES * 60

# The base path for the raw data CSV
CSV_PATH = r"c:\Users\Jonathan\Desktop\pet\ragas-evaluation\data\dataset.csv"


def main():
    # Load the models only once, outside the loop, for efficiency
    print("Loading LLM and Embedding models...")
    llm = load_google_llm(model_name="gemini-2.0-flash", temperature=0.6)
    embedding_model = load_lmstudio_embedding_model()
    print("Models loaded successfully.\n")

    # Create the main loop to iterate over each week
    for i, week in enumerate(SELECTED_WEEKS):
        print("=" * 50)
        print(f"STARTING PROCESSING FOR WEEK: {week}")
        print("=" * 50)

        # Set the specific paths for the current week INSIDE the loop
        KG_PATH = os.path.join(
            os.path.dirname(__file__),
            "..",
            "graphs/custom",
            f"knowledge_graph_week_{week}.json",
        )
        KG_PATH = os.path.abspath(KG_PATH)
        TESTSET_CSV = f"testset_week_{week}.csv"

        # Generate graph (or load if it already exists)
        print(f"Checking for graph at: {KG_PATH}")
        if not os.path.exists(KG_PATH):
            print("Graph not found. Building a new one...")
            build_and_save_graph(CSV_PATH, week, llm, KG_PATH)
            print("Graph built and saved.")
        else:
            print("Graph already exists. Loading...")

        kg = KnowledgeGraph.load(KG_PATH)
        print("Graph loaded.")

        # Generate questions/testset for the graph
        print(f"\nGenerating testset with {NUM_QUESTIONS_PER_TESTSET} questions...")
        df_testset = generate_questions(
            kg,
            llm,
            embedding_model,
            testset_size=NUM_QUESTIONS_PER_TESTSET,
            output_csv=TESTSET_CSV,
        )
        print(f"Testset saved to {TESTSET_CSV}\n")

        # 3. Automatically add type_reference_contexts column
        print("Adding context information (type and path)...")
        add_reference_context_info(KG_PATH, TESTSET_CSV)
        print("Context information added successfully.")

        print(f"\n--- Processing for Week {week} COMPLETED \n {df_testset.head}---")

        # --- End of Original Logic Block ---

        # Add timer
        # Check if this is NOT the last iteration of the loop
        if i < len(SELECTED_WEEKS) - 1:
            print(
                f"\nWaiting {WAIT_TIME_MINUTES} minutes before starting the next week..."
            )
            time.sleep(WAIT_TIME_SECONDS)
            print("Wait time finished.\n")

    print("\n" + "#" * 50)
    print("ALL PROCESSING COMPLETED!")
    print("#" * 50)


if __name__ == "__main__":
    main()
