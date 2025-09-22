### `src/generation`

This folder contains the core scripts for generating synthetic data, including knowledge graphs and test questions, for RAG evaluation.

---

### **Overview**

This pipeline automates the creation of high-quality test data from raw documents. The process involves:

1.  **Building a Knowledge Graph:** Documents are loaded from a CSV and transformed into a knowledge graph. This graph is enriched with keyphrases and headlines, making it a structured and searchable representation of the data.
2.  **Generating Questions:** Using the structured knowledge graph, the pipeline generates a test set of questions. It leverages predefined **personas** based on Bloom's Taxonomy to create a diverse range of questions, from simple recall to complex analysis.
3.  **Saving the Output:** The generated knowledge graph is saved as a JSON file, and the test set is saved as a CSV file for later use in evaluation.

---

### **Key Scripts**

- `main.py`: The entry point for the entire generation pipeline. It orchestrates the process of building the graph, generating questions, and saving the output for a list of specified "weeks."
- `graph_builder.py`: Contains the logic for creating and saving the knowledge graph from raw documents.
- `graph_utils.py`: Provides utility functions for loading documents from a CSV and applying RAGAS transforms to the knowledge graph.
- `question_generator.py`: Manages the generation of test questions using the knowledge graph and other helper modules.
- `personas.py`: Defines the **user personas** used to generate questions of varying complexity. Each persona corresponds to a level of Bloom's Taxonomy.
- `query_distribution_factory.py`: Configures the **query synthesizers** and their weights, which dictate the types of questions to be generated.

---

### **How to Run**

To generate the test data, simply run the `main.py` script. Ensure you have the necessary environment variables set for your LLMs as specified in the `src/models/README.md` file.

```bash
python main.py
```
