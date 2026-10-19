# Phase 4 — evidence-grounded verification

## Responsibility and labels

Produce the authoritative claim class. Canonical order is `0=REFUTED`, `1=NEI`, `2=SUPPORTED`. Model-specific NLI labels must be mapped explicitly; neutral does not mean false.

## Original code

Root: `~/Downloads/Phase4-main`. Includes `src/model.py`, `src/dataset.py`, `src/trainer.py`, `src/checkpoint.py`, training scripts, retrieval-conditioned training, and evaluation/audit scripts. [Complete file catalog](catalog/phase-4.md).

Application adapters are `backend/adapters/phase4_adapter.py` for the legacy checkpoint and `biomedical_nli_adapter.py` for the base application's biomedical NLI route. `BIOVERIFY_VERIFIER` selects these base modes.

## Improved dashboard classifier

The wrapper uses `outputs/evidence-combiner/candidate.py` instead. A supervised MiniLM selector at `outputs/clean-selector/model/best` chooses evidence sentences. `pritamdeka/PubMedBERT-MNLI-MedNLI` scores selected premises against the claim. `passage_features.py` constructs features; `clean-selector-combiner/experimental-model.joblib` produces the final three-class scores.

The candidate validates the combiner's class order and maps contradiction/neutral/entailment from model configuration. The wrapper records artifact identity and exports pairwise scores separately from the final combined scores.

## Evidence and limits

The recorded integrated result is 201/300 (67.0%) on reused development cases, macro-F1 0.6503. This is not an independent test estimate or proof of 80% accuracy. Scores are uncalibrated model outputs. See [evaluation](EVALUATION.md).

The candidate caches up to 16 exact local claims and returns deep copies. Live-source requests bypass this cache. Check serving/cached-feature parity when changing models, sentence formatting, truncation or feature ordering.
