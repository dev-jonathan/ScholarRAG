# Synthetic QA Dataset Generation and Processing Pipeline

## Abstract

This document describes the systematic approach for generating, processing, and evaluating synthetic Question-Answering (QA) datasets for educational content. The pipeline implements a multi-stage methodology that ensures dataset quality, diversity, and statistical representativeness while maintaining scientific rigor for research publication.

## 1. Introduction

The generation of high-quality synthetic QA datasets for educational content requires careful consideration of multiple factors: content diversity, cognitive complexity, statistical representativeness, and evaluation methodology. This pipeline addresses these challenges through a systematic approach that combines Large Language Models (LLMs), knowledge graph construction, and human supervision.

## 2. File Organization Structure

```bash
data/
│   README.md                  # This documentation
│
├── course_raw/                # Original course content (never overwritten)
│   ├── dataset_cs50_course.csv
│   └── cs50_dataset_files/
├── final/                # Final Data
│   └── rag_with_both_llms_formatted.csv
│
├── knowledge_graphs/          # Knowledge graphs for each week and custom graphs
│   ├── knowledge_graph_week_0.json
│   ├── ...
│   └── custom/
│       ├── knowledge_graph_week_0.json
│       └── ...
│
├── testsets/
│   ├── evaluation/            # Automatic metrics RAGAS evaluation results
│   │   ├── stratified_with_qa_eval.csv
│   │   └── stratified_with_qa_eval_html.csv
│   ├── raw/                   # Direct outputs from QA generation rounds
│   │   ├── testsets_per_week/              # Round 1: Individual week files
│   │   │   ├── testset_week_0.csv
│   │   │   ├── ...
│   │   │   └── testset_custom_graphs/      # Round 2: Custom graph files
│   │   └── testsets_per_round/             # Round unification
│   │       ├── testset_round1.csv
│   │       └── testset_round2.csv
│   ├── processed/             # Unified, deduplicated, and stratified datasets
│   │   ├── testset_raw_unified.csv         # Combined rounds 1 and 2
│   │   ├── testset_raw_unified_deduplicated.csv  # After deduplication (similarity filter)
│   │   └── testset_stratified.csv          # Final stratified sample
│   ├── rag/             # RAG (gemini-flash and GPT-OSS) Data and eval results
│   │   ├── rag_eval_results.csv         # Combined rounds 1 and 2
│   │   ├── models_rag_answers # raw chats json
│   ├── model_rag_answers/     # RAG model-generated answers for each question
│   │   └── Q1-xxxx.json
│   │   └── ...
│   ├── human_eval/            # Human annotation in label-studio and used xml
│   │   ├── testset_human_eval_raw.json
│   │   ├── testset_human_eval_cleaned.csv
│   │   ├── template_label_studio.xml
│   ├── scripts/               # All scripts for processing, deduplication, sampling, and analysis
│   │   ├── analysis_label_studio.py       # Label analysis
│   │   ├── analysis_rag.py                # RAG analysis and plots
│   │   ├── exploratory_analysis.py        # Dataset analysis
│   │   ├── semantic_similarity_filter.py  # Deduplication
│   │   ├── stratified_sampling.py         # Sampling strategy
│   │   ├── union_testsets.py              # Dataset unification
│   │   └── process_label_studio.py
│   └── semantic-similarity.md # Technical documentation/logs for similarity filtering
```

## 3. Data Flow and Methodology

### 3.1 Course Content Ingestion

- All original course materials (markdown, CSV) are stored in `course_raw/`.
- These files are never overwritten and serve as the ground truth for all downstream processing.

### 3.2 Knowledge Graph Construction

- Knowledge graphs are built for each week and for custom configurations (e.g., excluding transcriptions) and stored in `knowledge_graphs/`.

## 4. Dataset Generation Methodology

### 4.1 Multi-Round Synthetic QA Generation Strategy

The dataset generation process was conducted in two distinct rounds to address limitations and improve quality:

#### Round 1: Initial Generation

- **Objective**: Establish baseline QA generation capabilities
- **Scope**: All available educational content (transcriptions, notes, problemsets)
- **Output**: Individual testset files per week (`testsets_per_week/`)
- **Rationale**: Traceability and API rate limiting considerations
- **Sample Size**: 337 QA pairs across 12 weeks

#### Round 2: Optimized Generation

- **Objective**: Improve dataset balance and quality
- **Modification**: Customized knowledge graphs excluding transcription files
- **Justification**: Transcription files were disproportionately large, causing distribution imbalances
- **Output**: Custom graph testsets (`testsets_per_week/testset_custom_graphs/`)
- **Note**: Both rounds are unified in `testsets/raw/testsets_per_round/`.

- **Sample Size**: 337 QA pairs across 12 weeks

### 4.2 Knowledge Graph Customization

The transition from Round 1 to Round 2 involved strategic knowledge graph modifications:

- **Problem Identified**: Transcription files contained excessive content, leading to over-representation in QA generation
- **Solution Implemented**: Selective exclusion of transcription files from knowledge graph construction
- **Impact**: Improved distribution balance across content types (notes, problemsets, etc.)

## 5. Data Processing Pipeline

### 5.1 Unification Process

The multi-round generation strategy necessitated a unification step:

- All generated QA pairs are unified into a single file: `testsets/processed/testset_raw_unified.csv`:

```
Round 1 Testsets + Round 2 Testsets → testset_raw_unified.csv
```

**File**: `union_testsets.py`

- **Purpose**: Combines datasets from both generation rounds
- **Methodology**: Concatenation with duplicate handling
- **Output**: Comprehensive dataset with 372 QA pairs
- **Validation**: Cross-checked for data integrity and completeness

### 5.2 Deduplication Strategy

The unified dataset contained semantic duplicates that required systematic removal:

**File**: `semantic-similarity-filter.py`

- **Methodology**: Cosine similarity analysis using sentence embeddings
- **Model**: Qwen/Qwen3-Embedding-0.6B (768-dimensional embeddings)
- **Threshold**: 0.78 (empirically validated through iterative refinement and human supervision)
- **Process**:
  1. Generate embeddings for all questions using Qwen3-Embedding-0.6B
  2. Calculate pairwise cosine similarity matrix
  3. Group similar questions using graph connectivity (connected components)
  4. Select representative questions from each group based on centrality metrics
- **Output**: `testset_raw_unified_deduplicated.csv`
- **Reduction**: 372 → 337 QA pairs (9.4% reduction)

**Threshold Validation Process**:
The 0.78 threshold was determined through an iterative empirical approach:

1. **Iterative Refinement**: Started with 0.99 and progressively lowered by 0.01 increments
2. **False Negative Analysis**: Human evaluation of algorithm-identified duplicates revealed 9 false negatives out of 43 removed questions (20.9% false negative rate)
3. **Literature Alignment**: Threshold aligns with semantic similarity literature for educational content (typically 0.75-0.85 range)
4. **Pipeline Context**: Acceptable precision given subsequent filtering stages (stratified sampling, comprehensive human evaluation)

**Scientific Justification**: The threshold balances semantic diversity preservation with duplicate removal. While not requiring perfect precision due to downstream quality filters, the 0.78 threshold provides a robust first-pass deduplication that maintains dataset integrity for subsequent evaluation stages.

### 5.3 Stratified Sampling

Given the computational and human evaluation constraints, a stratified sampling approach was implemented:

**File**: `stratified-sampling.py`

- **Objective**: Reduce dataset size while maintaining statistical representativeness
- **Target Size**: 120 QA pairs (determined by human evaluation feasibility and statistical power requirements)
- **Sampling Strategy**:
  - Fixed number of questions per week (10 questions/week × 12 weeks = 120 total)
  - Proportional representation of content types (80% chunk, 20% document)
  - Balance across personas and query styles
  - Maximum file coverage diversity

**Stratification Variables**:

- Week (temporal distribution across 12 weeks)
- Reference context type (document vs. chunk)
- Persona name (6 cognitive diversity levels based on Bloom's Taxonomy)
- Query style (4 linguistic diversity categories)
- Query length (3 complexity distribution levels)

**Output**: `testset_stratified.csv`
**Statistical Validation**: Chi-square tests confirmed proportional representation across strata (p < 0.05)

## 6. Evaluation Framework

### 6.1 Automatic Evaluation

The stratified dataset underwent automatic evaluation using RAGAS metrics:

**Metrics Selected**:

- **Faithfulness**: Measures answer fidelity to provided context (scale: 0-1)
- **ResponseRelevancy**: Assesses answer relevance to the question (scale: 0-1)
- **Question Quality**: Custom metric for question clarity and grounding (scale: 1-5)

**Output**: `testsets/evaluation/stratified_with_qa_eval.csv`

### 6.2 Human Evaluation Integration

To validate automatic metrics and ensure dataset quality, human evaluation was conducted:

**Tool**: Label Studio
**Methodology**: Likert scale evaluation (1-5) with standardized criteria
**Criteria Alignment**: Direct correspondence with RAGAS metrics
**Input**: `testsets/evaluation/stratified_with_qa_eval_html.csv` (HTML-formatted for XML rendering)
**Output**: `testsets/human_eval/testset_human_eval_raw.json` (Raw exports JSON with human evaluation)

- The script `process_label_studio.py` documents and executes all processing steps.

### 6.3 Quality Threshold Justification

**Exclusion Thresholds**:

- **RAGAS Metrics**: 0.6 threshold for Faithfulness and ResponseRelevancy (<= 60% cutoff)
- **Human Metrics**: 3.0 threshold for all Likert-scale evaluations (<= 60% cutoff)

**Threshold Rationale**:

1. **Conservative Quality Standards**: Thresholds prioritize high-quality QA pairs to ensure "garbage in, garbage out" principle for RAG evaluation
2. **Dual Validation System**: Combines automatic RAGAS metrics with human evaluation based on RAGAS criteria
3. **Moderate Correlation Evidence**: Statistical analysis shows moderate correlation between automatic and human evaluations
4. **Cross-Validation Pattern**: When human evaluators exclude questions, at least one automatic metric typically indicates quality issues
5. **Pipeline Context**: Conservative thresholds are appropriate given the critical role of QA pairs in RAG system evaluation

**Scientific Justification**: The 50% threshold for automatic metrics and 60% threshold for human evaluation represent conservative quality standards that prioritize dataset integrity over quantity, ensuring reliable RAG system assessment.

## 7. Statistical Analysis

### 7.1 Dataset Distribution Analysis

**File**: `exploratory_analysis.py`

- **Purpose**: Comprehensive statistical analysis of dataset characteristics
- **Analyses**:
  - Frequency distributions across stratification variables
  - Cross-tabulation analysis
  - File coverage statistics (61 unique source files)
  - Temporal distribution patterns

### 7.2 Quality Metrics

The final dataset achieved the following characteristics:

- **Size**: 120 QA pairs (optimal for human evaluation with 95% confidence level)
- **Coverage**: 61 unique source files across 12 weeks
- **Balance**: Proportional representation across weeks and content types
- **Diversity**: 6 personas, 4 query styles, 3 complexity levels
- **Statistical Power**: Sufficient for correlation analysis (n > 30 per stratum)

## 8. Scientific Contributions

This pipeline contributes to the field of synthetic QA dataset generation through:

1. **Multi-Round Generation Strategy**: Addresses API limitations while maintaining quality
2. **Semantic Deduplication**: Ensures dataset diversity through embedding-based similarity analysis
3. **Stratified Sampling**: Maintains statistical representativeness while reducing size
4. **Hybrid Evaluation**: Combines automatic metrics with human supervision
5. **Reproducible Methodology**: Complete documentation for scientific replication

## 9. Limitations and Future Work

### 9.1 Current Limitations

- Dependency on specific LLM APIs (Google Gemini)
- Manual threshold determination for deduplication (0.78) - validated through human supervision
- Limited to educational content domain (CS50 course)
- Human evaluation limited to single annotator (no inter-annotator agreement)
- Conservative quality thresholds may reduce dataset size but ensure high quality

### 9.2 Future Improvements

- Automated threshold optimization using validation sets
- Cross-domain generalization to other educational content
- Advanced sampling strategies with adaptive allocation
- Multi-annotator evaluation with inter-rater reliability analysis
- Sensitivity analysis for different threshold values
- Comprehensive confusion matrix analysis for deduplication algorithm

## 10. Reproducibility

All scripts and configurations are provided to ensure complete reproducibility:

- Processing scripts with detailed comments and error handling
- Configuration parameters clearly documented with justifications
- Input/output file specifications with checksums
- Statistical analysis procedures with significance testing
- Environment requirements and dependency versions

## 11. Conclusion

This systematic approach to synthetic QA dataset generation provides a robust foundation for educational content evaluation research. The multi-stage pipeline ensures quality, diversity, and statistical validity while maintaining scientific rigor suitable for academic publication.

---

**Citation**: This methodology is part of ongoing research on synthetic QA dataset quality evaluation for educational content. Please cite this work appropriately in academic publications.

---

**Contact**: For questions or collaboration, contact the project maintainer by github issues.
