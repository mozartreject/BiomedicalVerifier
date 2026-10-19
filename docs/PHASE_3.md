# Phase 3 — evidence hierarchy

## Responsibility

Classify the type/authority of retrieved evidence and attach hierarchy information. Evidence authority is distinct from whether a passage supports a particular claim.

## Code

Root: `~/Downloads/Phase3-main`. Key modules include `evidence_classifier.py`, `llm_classifier.py`, `hierarchy_weights.py`, `run_phase3.py`, and successive taxonomy and evaluation scripts. `backend/adapters/phase3_adapter.py` integrates this stage. [Complete file catalog](catalog/phase-3.md).

The folder includes multiple historical taxonomy versions, forensic audits and Phase 4 preparation scripts. A filename or the newest version number is not proof that a file is used in production; inspect the adapter imports and configuration.

## Configuration and contract

`BIOVERIFY_PHASE3_ROOT`, `BIOVERIFY_PHASE3_CONFIG`, `BIOVERIFY_PHASE3_TOP_K`, and the Phase 3 Ollama model/URL settings configure this stage. The default local model is `qwen2.5:7b`.

In the improved dashboard, this stage adds context to the three selected evidence records. The wrapper's Phase 4 adapter checks that all selected evidence IDs survive without duplicates. It refuses stale classification when the selected evidence set changes. The fixed candidate classifier does not consume Phase 3 hierarchy weights.

Evaluate taxonomy quality independently; the headline claim-classification score does not establish the correctness of every authority label.
