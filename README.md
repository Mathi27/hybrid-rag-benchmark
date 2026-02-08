# Hybrid Retrieval-Augmented Generation (RAG) System  
### Group ID: 125
### Group Members Name with Student ID:

| BITS ID     | Name                         | Contribution |
|-------------|----------------------------- |--------------|
| **2024AA05346** | **Tamilselvan S**              |     100%     |
| **2024AB05320** | **Mathi Yuvarajan T K**            |     100%     |
| **2024aa05279** | **Bhartendu Kumar**                 |     100%     |
| **2024aa05198** | **Rakesh Jha**          |     100%     |
| **2024aa05957** | **Shripad Prakash Kelapure**                   |     100%     |


This project is implemented and maintained as a **single Google Colab notebook**. 

The notebook contains the complete pipeline, including data collection, indexing, retrieval, response generation, evaluation, and reporting.

---

## 1. Project Overview

This notebook implements a **Hybrid RAG system** that combines:
- Dense semantic retrieval (FAISS + sentence embeddings)
- Sparse keyword retrieval (BM25)
- Reciprocal Rank Fusion (RRF)
- Open-source LLM-based answer generation
- Automated and innovative evaluation framework

The system operates on a **Wikipedia-based corpus of 500 articles** and evaluates performance using URL-level metrics and advanced analysis techniques.

---

## 2. Environment & Setup

### 2.1 Platform
- Google Colab (recommended)
- Python 3.x runtime
- GPU runtime recommended for faster LLM inference

### 2.2 Install Dependencies

Run the following cell at the beginning of the notebook:

```python
!pip install sentence-transformers faiss-cpu rank-bm25 transformers torch gradio pandas numpy matplotlib tqdm
```

## 3. Data Requirements

### 3.1 Fixed Wikipedia URLs (Mandatory)

The notebook uses a fixed set of 200 Wikipedia URLs that remain constant across all indexing and evaluation runs.

These URLs are stored directly in the notebook as a JSON object and can also be exported if required.

Example structure:
```
{
  "fixed_urls": [
    "https://en.wikipedia.org/wiki/Machine_learning",
    "https://en.wikipedia.org/wiki/Artificial_intelligence",
    "https://en.wikipedia.org/wiki/Neural_network"
  ]
}
```
### 3.2 Random Wikipedia URLs

For each indexing run, 300 additional Wikipedia URLs are randomly sampled using the MediaWiki API. 

These URLs change every time the notebook is re-run and are used to simulate a dynamic corpus.

---


## 4. Notebook Execution Flow

The notebook is organized into clearly labeled sections and should be run top to bottom.

### 4.1 Data Collection & Preprocessing

- Fetch Wikipedia pages using MediaWiki API
- Clean HTML and extract text
- Chunk text into 200–400 token segments with overlap
- Store chunk metadata (URL, title, chunk ID)

### 4.2 Indexing

- Generate sentence embeddings for chunks
- Build FAISS dense vector index
- Build BM25 sparse keyword index

### 4.3 Hybrid Retrieval

- Perform dense retrieval (FAISS)
- Perform sparse retrieval (BM25)
- Fuse rankings using Reciprocal Rank Fusion (RRF)

### 4.4 Response Generation

- Concatenate top-N retrieved chunks with user query
- Generate answers using an open-source LLM (e.g., Mistral)
- Ensure answers are grounded in retrieved context

### 4.5 User Interface

Gradio-based interactive UI
Displays:

- User query
- Generated answer
- Retrieved sources
- Response time

## 6. Running the Evaluation Pipeline

The notebook includes a single-command automated evaluation pipeline.

### 6.1 Evaluation Steps

Load 100 generated evaluation questions
Run Hybrid RAG once per question (cached)

### Compute metrics:

- MRR (URL-level)
- Recall@K (URL-level)
- Answer Faithfulness (heuristic proxy)
- Perform ablation studies
- Conduct error analysis
- Generate tables and visualizations

## 7. Evaluation Outputs

All evaluation outputs are generated within the notebook and optionally saved to Google Drive:

1. Summary metrics table

2. Detailed per-question results (DataFrame)

#### Visualizations:

1. Overall performance metrics

2. MRR distribution

3. Faithfulness distribution

4. Ablation study comparison

5. Error type distribution

## Notes

1. Caching is used to avoid repeated LLM inference during evaluation.
2. Faithfulness is computed using a lightweight heuristic to reduce runtime.
3. The notebook is modular and can be extended with additional retrievers or metrics.

## Usage Recommendation

For smooth execution:

1. Run all cells sequentially
2. Avoid restarting the runtime mid-execution
3. Save intermediate outputs to Google Drive if needed

## Acknowledgements

1. Wikipedia for the knowledge corpus
2. FAISS, Sentence-Transformers, HuggingFace Transformers
3. Research on Retrieval-Augmented Generation and Hybrid Retrieval