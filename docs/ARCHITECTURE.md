# Architecture and execution modes

## Five-stage contract

Claim → retrieval → evidence hierarchy → verification → explanation → validated decision package and persistence.

Phase 1 additionally produces a diagnostic representation for text and optional images. `backend/pipeline.py` explicitly says its fused representation does not modify the authoritative Phase 4 verdict. Phase 5 must preserve that verdict.

## Original application

`BiomedicalVerifier/backend/pipeline.py` constructs phase adapters, loads configured resources, executes stages, checks status and persists validated results. `pipeline_config.py` selects roots, checkpoints, environment settings, and the legacy or biomedical-NLI verifier. Its defaults differ from the experimental dashboard wrapper.

## Improved dashboard integration

`outputs/evidence-combiner/dashboard_backend.py` injects `Retrieval` and `Verification` adapters into the original pipeline. `Shared.load()` explicitly constructs `Candidate(trained_selector=True)`.

The candidate engine performs BM25 over 35,183 documents → MiniLM reranking of 30 candidates → three documents → supervised sentence selection → PubMedBERT NLI → trained passage-feature boosted-tree classifier. The three evidence records then receive Phase 3 metadata. Verification validates that the evidence IDs are unchanged before exporting the stored candidate result. The explanation stage receives the final verdict.

The wrapper disables live PubMed for this mode. Phase 3 authority weights are contextual metadata, not inputs to the frozen candidate classifier. Candidate runtime is booked in Phase 2; Phase 4 exports its already-computed result. Phase timing charts therefore do not measure independent model runtimes.

Do not equate the base API command with the improved launcher: both use port 8000 but can construct different pipelines.
