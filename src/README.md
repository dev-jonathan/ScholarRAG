### `src/`

This folder contains the main source code for the project's data generation and evaluation pipelines. The code is organized into distinct sub-modules to ensure clarity and maintainability.

```bash
/src
├── .env
├── README.md
├── __init__.py
├── evaluation/
│   ├── eval_qa_pipeline.py
│   ├── eval_rag_pipeline.py
│   ├── README.md
│   └── __init__.py
├── experimental/
│   ├── custom_single_hop.py
│   └── README.md
├── generation/
│   ├── graph_builder.py
│   ├── graph_utils.py
│   ├── main.py
│   ├── personas.py
│   ├── query_distribution_factory.py
│   ├── question_generator.py
│   └── README.md
├── models/
│   ├── models.py
│   └── README.md
└── utils/
    ├── add_type_reference_contexts.py
    ├── aux_prints.py
    ├── create_custom_graphs.py
    ├── csv_to_json.py
    ├── extract_messages.py
    ├── fusion_data.py
    ├── markdown_to_html.py
    ├── README.md
    ├── remove_node_duplicates.py
    └── type_reference_contexts_util.py

```

---

### **Project Structure**

- **`generation/`**:
  This module contains all scripts for generating synthetic data, including knowledge graphs and test questions for RAG evaluation.

  [[Read the detailed README for `generation/`](./generation/README.md)]

- **`evaluation/`**:
  This module is dedicated to evaluating the performance of the RAG pipeline using metrics from the Ragas framework. It's used to assess both the quality of the generated data and the effectiveness of different LLMs.

  [[Read the detailed README for `evaluation/`](./evaluation/README.md)]

- **`models/`**:
  This module manages the configuration and loading of all Large Language Models (LLMs) and embedding models used throughout the project.

  [[Read the detailed README for `models/`](./models/README.md)]

- **`utils/`**:
  This folder houses a collection of utility scripts that support the main pipelines. These scripts handle tasks such as data cleaning, file format conversions, and knowledge graph manipulation.

  [[Read the detailed README for `utils/`](./utils/README.md)]

---
