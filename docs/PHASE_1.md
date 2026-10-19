# Phase 1 — diagnostic representation

## Responsibility

Encode text and optional images using the existing BioBERT/ViT representation branch. It is retained for diagnostic outputs and provenance, rather than controlling the final supported/refuted/NEI decision.

## Code and artifacts

Source root: `~/Downloads/kaggle_upload`. `src/models.py` defines model components; `dataset.py` and `transforms.py` prepare inputs; `losses.py`, `train.py`, and `utils.py` support training. `src/config.py` and root `config.yaml` hold configuration. See [all Phase 1 files](catalog/phase-1.md).

Application integration: `backend/adapters/phase1_adapter.py`; conversion utility: `tools/convert_phase1_checkpoint.py`; adapter tests: `tests/test_phase1_adapter.py` in BiomedicalVerifier.

`BIOVERIFY_PHASE1_ROOT`, `BIOVERIFY_PHASE1_CHECKPOINT`, and `BIOVERIFY_PHASE1_CONFIG` select resources. The configured default checkpoint is `~/Downloads/BiomedicalVerifier/models/phase1_converted.pt`.

## Inputs, outputs and limits

Input is claim text plus an optional image supported by the adapter. Output is a typed Phase 1 result with timing/provenance and diagnostic representation information. The downstream verifier is not trained to consume the fused representation in the current faithful pipeline.

The dedicated chest-X-ray option was removed at the user's request. Generic image attachment must not be described as validated medical-image diagnosis or evidence that alters the final verdict. The reported text-classification score does not evaluate this branch.
