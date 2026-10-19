# Phase 2 — evidence retrieval

## Responsibility

Find candidate research relevant to a claim and preserve document identifiers, source attribution and relevance scores. Missing or unrelated evidence cannot be repaired simply by forcing a supported/refuted prediction.

## Source and original route

Root: `~/Downloads/phase2`. Important files include `retriever.py`, `validated_retriever.py`, `reranker.py`, `react_agent.py`, `run_phase2.py`, `config.py`, `build_faiss_index.py`, `build_35k_index.py`, `download_pubmed.py`, and corpus/retrieval audit scripts. [Complete file catalog](catalog/phase-2.md).

The base application uses `backend/adapters/phase2_adapter.py`, with optional live PubMed implemented in `backend/services/pubmed_search.py`. Environment configuration includes `BIOVERIFY_PHASE2_ROOT`, `BIOVERIFY_PHASE2_INDEX_DIR`, `BIOVERIFY_BM25_K`, `BIOVERIFY_CE_TOP_K`, and `BIOVERIFY_LIVE_PUBMED`.

## Improved dashboard route

`outputs/evidence-combiner/candidate.py` reads `~/Downloads/phase2/data/faiss_index_35k/abstract_metadata.pkl`, asserts exactly 35,183 records, and builds sparse BM25. The recorded corpus consists of 5,183 SciFact and 30,000 PubMed documents.

It retrieves 30 candidates, reranks full document texts with `cross-encoder/ms-marco-MiniLM-L-6-v2`, retains three, and selects passages with the trained evidence selector. This route does not query the dense FAISS index or run ReAct. Live PubMed is disabled by the dashboard wrapper.

## Checks and failure modes

Check corpus identity/count, source-prefixed IDs, candidate recall, document relevance, and annotated sentence recovery separately. More documents can introduce distractors; corpus growth alone does not guarantee higher accuracy. The hard-coded record count and artifact path must be revised intentionally before changing the corpus used by this candidate.
