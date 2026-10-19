# phase-5: source file catalog

Source root: `/Users/joshua/Downloads/Phase5-main`

Generated from local files. Inclusion does not imply a file is active, tested, or production-ready. Backups and historical experiments are included when present. Descriptions are module docstrings or structural summaries, not an audit of correctness.

## `analyze_phase5_failures.py`

Local source: `/Users/joshua/Downloads/Phase5-main/analyze_phase5_failures.py` (source files are not included in this documentation push).

Python module; see defined symbols and source.

**Top-level definitions/type:** `load_jsonl`, `safe_float`, `final_attempt`, `get_final_output`, `get_final_validation`, `text_matches_any`, `extract_numeric_tokens`, `normalize_numeric_token`, `numeric_false_positive_candidate`, `verdict_mismatch_present`, `semantic_failure_present`, `unsupported_number_failure_present`, `citation_failure_present`, `get_semantic_mean`, `get_semantic_minimum`, `get_coverage_mean`, `classify_failure`, `write_csv`, `write_json`, `write_report`, `main`

## `build_reference_set.py`

Local source: `/Users/joshua/Downloads/Phase5-main/build_reference_set.py` (source files are not included in this documentation push).

Python module; see defined symbols and source.

**Top-level definitions/type:** `main`

## `config.yaml`

Local source: `/Users/joshua/Downloads/Phase5-main/config.yaml` (source files are not included in this documentation push).

Configuration file; values are intentionally not copied into this catalog.

**Top-level definitions/type:** Configuration

## `evaluate_phase5.py`

Local source: `/Users/joshua/Downloads/Phase5-main/evaluate_phase5.py` (source files are not included in this documentation push).

Python module; see defined symbols and source.

**Top-level definitions/type:** `load_jsonl`, `rouge_l`, `main`

## `normalize_phase5_inputs.py`

Local source: `/Users/joshua/Downloads/Phase5-main/normalize_phase5_inputs.py` (source files are not included in this documentation push).

Python module; see defined symbols and source.

**Top-level definitions/type:** `load_json`, `atomic_write_json`, `normalize_phase2`, `normalize_phase3`, `make_backup`, `main`

## `run_phase5.py`

Local source: `/Users/joshua/Downloads/Phase5-main/run_phase5.py` (source files are not included in this documentation push).

Python module; see defined symbols and source.

**Top-level definitions/type:** `main`

## `validate_inputs.py`

Local source: `/Users/joshua/Downloads/Phase5-main/validate_inputs.py` (source files are not included in this documentation push).

Python module; see defined symbols and source.

**Top-level definitions/type:** `main`

## `src/__init__.py`

Local source: `/Users/joshua/Downloads/Phase5-main/src/__init__.py` (source files are not included in this documentation push).

Python module; see defined symbols and source.

**Top-level definitions/type:** No top-level functions/classes.

## `src/adapters.py`

Local source: `/Users/joshua/Downloads/Phase5-main/src/adapters.py` (source files are not included in this documentation push).

Python module; see defined symbols and source.

**Top-level definitions/type:** `load_jsonish`, `load_predictions`, `_evidence_list`, `_float`, `_parse_evidence`, `_extract_claim_records`, `load_evidence_map`, `join_records`

## `src/grounding.py`

Local source: `/Users/joshua/Downloads/Phase5-main/src/grounding.py` (source files are not included in this documentation push).

Python module; see defined symbols and source.

**Top-level definitions/type:** `_norm_num`, `_is_identifier_context`, `_extract_numbers`, `_get_claim_text`, `_split_sentences`, `_communicates_nei`, `_is_nei_absence_sentence`, `SemanticGrounder`, `_compute_semantic_validation`, `validate_generated`

## `src/llm.py`

Local source: `/Users/joshua/Downloads/Phase5-main/src/llm.py` (source files are not included in this documentation push).

Python module; see defined symbols and source.

**Top-level definitions/type:** `OllamaClient`

## `src/models.py`

Local source: `/Users/joshua/Downloads/Phase5-main/src/models.py` (source files are not included in this documentation push).

Python module; see defined symbols and source.

**Top-level definitions/type:** `normalize_verdict`, `Evidence`, `ClaimRecord`

## `src/orchestrator.py`

Local source: `/Users/joshua/Downloads/Phase5-main/src/orchestrator.py` (source files are not included in this documentation push).

Python module; see defined symbols and source.

**Top-level definitions/type:** `Phase5Orchestrator`

## `src/prompting.py`

Local source: `/Users/joshua/Downloads/Phase5-main/src/prompting.py` (source files are not included in this documentation push).

Python module; see defined symbols and source.

**Top-level definitions/type:** `generation_prompt`, `repair_prompt`

## `src/utils.py`

Local source: `/Users/joshua/Downloads/Phase5-main/src/utils.py` (source files are not included in this documentation push).

Python module; see defined symbols and source.

**Top-level definitions/type:** `set_seed`, `load_yaml`, `normalize_text`, `claim_hash`, `first`, `atomic_json`, `atomic_jsonl`, `atomic_text`
