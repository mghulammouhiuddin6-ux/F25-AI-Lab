# Lab 6 — NLP Fundamentals: Tokenization, Embeddings & Text Chunking

**Course:** CAI601400 — Artificial Intelligence Lab Manual  
**Lab:** 6 | **CLO:** CLO3 (C3: Apply)  
**Project folder:** `lab6_nlp`

## Overview
This standalone project implements the three assessed tasks: tokenization and FAQ retrieval (Task 1), source-preserving chunking and semantic suggestions (Task 2), and controlled document-retrieval evaluation (Task 3). The corpus and policies are synthetic teaching data, not actual university rules.

## Requirements and setup
Python 3.10 or newer is recommended. From this folder:

```bash
python -m venv .venv
# Windows PowerShell: .venv\Scripts\Activate.ps1
# macOS/Linux: source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python -m pip freeze > requirements-lock.txt
```

The first embedding run downloads `sentence-transformers/all-MiniLM-L6-v2`; it runs on CPU and does not need a GPU or paid API. If the model cannot be downloaded, TF-IDF tasks remain runnable. Do not claim embedding results until the embedding commands have actually run.

## Run commands

```bash
python task1_tokens.py
python guided_chatbot.py
python task1_chatbot_check.py
python task2_chunks.py
python task2_analysis.py
python guided_tokens.py
python guided_chunks.py
python guided_embeddings.py
python guided_limits.py
python guided_metrics.py
python guided_suggestions.py
python guided_suggestions.py --backend embedding --query "forgot login"
python task3_retrieval.py
python document_chatbot.py
```

Run scenario demonstrations with `python scenario1_handbook.py` through `python scenario5_equipment.py`. `python create_dataset.py` validates the committed dataset; it does not overwrite it.

To run the FAQ assistant with real sentence embeddings: `python guided_chatbot.py --backend embedding`. The document chatbot uses the embedding backend and requires the model. Task 3 attempts all six combinations (three chunking strategies × two retrieval backends), measures model loading separately, and prints a clear SKIPPED message if the embedding dependency or model is unavailable. A skipped run is not a completed embedding comparison; rerun on an internet-connected machine before final submission.

## Dataset and evaluation protocol
- `corpus.json`: five synthetic documents, each expanded to the requested 150–250-word range.
- `queries.json`: eight answerable queries (four development, four held-out test) and two unanswerable queries.
- Relevance requires both the correct document and the complete labeled evidence substring inside a retrieved chunk.
- `task3_retrieval.py` compares overlap-0 windows, overlap-10 windows, and sentence-aware chunks with TF-IDF and real sentence embeddings. It reports Hit@3 and MRR@3 on answerable queries and writes top-three ranked records to `retrieval_log.csv`.
- Model load/build time and query-search time are measured separately in the evaluation output. Timing depends on hardware, cache and environment.
- Unanswerable queries are retained in the log but excluded from answerable relevance metrics. A high score is not proof of answerability.

## Source traceability
Each chunk contains a document ID, chunk ID, source filename, character start/end offsets and exact source text. The code checks that chunk text is a source substring. The sentence splitter is intentionally simple and may split incorrectly around abbreviations; long sentences fall back to word windows.

## Limitations and responsible use
The sample corpus is small and synthetic. English MiniLM results do not establish Urdu retrieval quality. Similarity scores are not probabilities or truth checks. Metadata filters in the helper are retrieval filters, not security controls. Never use this teaching prototype to make consequential policy, legal, employment or account decisions. Inspect source evidence and refer uncertain cases to an authorised person.

## Submission contents
The folder includes source code, datasets, scenario scripts, guided examples, dependency file, README, generated evaluation log (when dependencies permit), and `Lab6_Report.docx`. Do not commit `.venv`, model caches, credentials or private data. Review the actual outputs on your own machine and capture genuine terminal screenshots before submission.
