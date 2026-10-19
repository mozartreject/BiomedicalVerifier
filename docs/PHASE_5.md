# Phase 5 — grounded explanation

## Responsibility

Explain a fixed verification verdict using the supplied evidence and citations. The explanation model must not become a second verdict authority.

## Source and integration

Root: `~/Downloads/Phase5-main`. `src/orchestrator.py` coordinates generation; `prompting.py` constructs prompts; `llm.py` handles model interaction; `grounding.py` checks grounding; `models.py` and `adapters.py` define/support contracts. Root scripts validate/normalize inputs, build reference sets and evaluate failures. [Complete file catalog](catalog/phase-5.md).

`backend/adapters/phase5_adapter.py` connects it to the application. Default generator is local Ollama `qwen2.5:7b` at `http://localhost:11434/api/chat`.

## Configuration

`BIOVERIFY_PHASE5_ROOT`, `BIOVERIFY_PHASE5_CONFIG`, `BIOVERIFY_PHASE5_OLLAMA_MODEL`, `BIOVERIFY_PHASE5_OLLAMA_URL`, timeout, retry, repair-attempt, semantic-threshold and coverage-threshold variables are defined in `backend/pipeline_config.py`. Inspect the adapter/configuration actually loaded before assuming environment defaults apply throughout legacy modules.

## Validation

Check preserved verdict, valid evidence IDs, citation accuracy and whether each explanatory claim follows from the cited passage. A fluent explanation is not proof of grounding. The 67.0% classifier result does not measure explanation accuracy; explanation quality needs a separate evaluation.
