### `src/utils`

This folder contains various utility scripts that support the main pipelines of the project. These scripts handle tasks such as data cleaning, file format conversions, and graph manipulation, making the main generation and evaluation processes more efficient.

---

### **Key Scripts**

- `type_reference_contexts_util.py`: This is a critical script for the RAG evaluation workflow. It processes a test set CSV and a knowledge graph JSON to enrich the test set with two new columns: `reference_context_type` and `reference_context_path`. This allows for a more detailed analysis of the RAG model's performance by linking each generated question back to its original document source and type. It's a key part of ensuring reproducibility and context-aware evaluation.

- `create_custom_graphs.py`: This script is used to modify existing knowledge graphs. Its primary function is to read a knowledge graph JSON, remove nodes of a specific type (e.g., `'transcription'`), and save the new, filtered graph. This is useful for creating custom test scenarios or excluding certain document types from the evaluation pipeline.

- `fusion_data.py`: This utility script merges data from different sources. It combines information from a generated test set CSV with LLM responses stored in a directory of JSON files. This is essential for preparing a unified dataset for evaluation, bringing together the questions, ground-truth answers, and model-generated responses into a single, comprehensive file.

- `aux_prints.py`: A simple helper script that provides a summary of a knowledge graph's contents, showing the total number of nodes and relationships, as well as a count of different node types. It's a quick tool for sanity checks during development and data generation.

- `add_type_reference_contexts.py`: A simplified version of `type_reference_contexts_util.py`, focusing solely on adding the `type_reference_contexts` column to a test set CSV.

- `markdown_to_html.py`: Converts Markdown text to HTML. This is particularly useful for preparing content for display in web-based applications or reports, ensuring that formatting like lists, tables, and code blocks are correctly rendered.

- `remove_node_duplicates.py`: A maintenance script for cleaning knowledge graph JSON files. It identifies and removes duplicate nodes based on their ID, ensuring data integrity and consistency within the graphs.
