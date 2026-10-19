# workspace: source file catalog

Source root: `/Users/joshua/Documents/Codex/2026-09-29/can-x20-2`

Generated from local files. Inclusion does not imply a file is active, tested, or production-ready. Backups and historical experiments are included when present. Descriptions are module docstrings or structural summaries, not an audit of correctness.

## `start_project.command`

Local source: `/Users/joshua/Documents/Codex/2026-09-29/can-x20-2/start_project.command` (source files are not included in this documentation push).

Shell entry point; inspect paths and arguments before running.

**Top-level definitions/type:** Shell

## `outputs/advanced-evidence/backend/pipeline.py`

Local source: `/Users/joshua/Documents/Codex/2026-09-29/can-x20-2/outputs/advanced-evidence/backend/pipeline.py` (source files are not included in this documentation push).

Python module; see defined symbols and source.

**Top-level definitions/type:** `_utc_now`, `_enum_value`, `_assert_success`, `_collect_models`, `BiomedicalVerificationPipeline`

## `outputs/advanced-evidence/backend/pipeline_config.py`

Local source: `/Users/joshua/Documents/Codex/2026-09-29/can-x20-2/outputs/advanced-evidence/backend/pipeline_config.py` (source files are not included in this documentation push).

Python module; see defined symbols and source.

**Top-level definitions/type:** `_env_path`, `_env_int`, `_env_float`, `Phase1Config`, `Phase2Config`, `Phase3Config`, `Phase4Config`, `Phase5Config`, `RuntimeConfig`, `PipelineConfig`, `load_pipeline_config`, `ensure_runtime_directories`, `validate_static_paths`

## `outputs/advanced-evidence/backend/schemas.py`

Local source: `/Users/joshua/Documents/Codex/2026-09-29/can-x20-2/outputs/advanced-evidence/backend/schemas.py` (source files are not included in this documentation push).

Python module; see defined symbols and source.

**Top-level definitions/type:** `Verdict`, `UserFacingVerdict`, `PhaseName`, `PhaseStatus`, `ExplanationStatus`, `AuthorityTier`, `Modality`, `BaseSchema`, `InferenceRequest`, `PhaseError`, `PhaseTiming`, `ModelArtifact`, `Phase1Result`, `EvidenceLineage`, `EvidenceRecord`, `RetrievalTrace`, `Phase2Result`, `Phase3Result`, `ClassProbabilities`, `PairwiseVerification`, `Phase4Result`, `GroundingMetrics`, `Phase5Result`, `PipelineProvenance`, `DecisionPackage`, `verdict_to_user_facing`

## `outputs/advanced-evidence/backend/adapters/biomedical_nli_adapter.py`

Local source: `/Users/joshua/Documents/Codex/2026-09-29/can-x20-2/outputs/advanced-evidence/backend/adapters/biomedical_nli_adapter.py` (source files are not included in this documentation push).

Biomedical NLI verifier with explicit label mapping and relevance discounting. This is a separate deployment mode, not the historical Phase 4 checkpoint. Scores are uncalibrated model outputs. The original adapter remain

**Top-level definitions/type:** `relevance_discount`, `evidence_passage`, `BiomedicalNliAdapter`

## `outputs/advanced-evidence/backend/adapters/phase2_adapter.py`

Local source: `/Users/joshua/Documents/Codex/2026-09-29/can-x20-2/outputs/advanced-evidence/backend/adapters/phase2_adapter.py` (source files are not included in this documentation push).

Python module; see defined symbols and source.

**Top-level definitions/type:** `_utc_now`, `_iso_utc`, `_sigmoid`, `Phase2ImportBundle`, `_prepare_phase2_modules`, `_restore_phase2_modules`, `Phase2Adapter`

## `outputs/advanced-evidence/backend/adapters/phase3_adapter.py`

Local source: `/Users/joshua/Documents/Codex/2026-09-29/can-x20-2/outputs/advanced-evidence/backend/adapters/phase3_adapter.py` (source files are not included in this documentation push).

Python module; see defined symbols and source.

**Top-level definitions/type:** `_utc_now`, `_iso_utc`, `_load_module_from_file`, `Phase3Adapter`

## `outputs/advanced-evidence/backend/api/routes/system.py`

Local source: `/Users/joshua/Documents/Codex/2026-09-29/can-x20-2/outputs/advanced-evidence/backend/api/routes/system.py` (source files are not included in this documentation push).

Python module; see defined symbols and source.

**Top-level definitions/type:** `_utc_now_iso`, `health`, `models`

## `outputs/advanced-evidence/backend/services/persistence.py`

Local source: `/Users/joshua/Documents/Codex/2026-09-29/can-x20-2/outputs/advanced-evidence/backend/services/persistence.py` (source files are not included in this documentation push).

Python module; see defined symbols and source.

**Top-level definitions/type:** `PersistenceError`, `DuplicateRequestError`, `AuditPhaseRecord`, `AuditRecord`, `PersistenceResult`, `_enum_value`, `_sha256_bytes`, `_sha256_text`, `_safe_request_id`, `_canonical_json_bytes`, `_fsync_directory`, `_atomic_write_new`, `_phase_record`, `_extract_checkpoint_sha256`, `_model_artifact_summary`, `_build_invariant_checks`, `DecisionPackagePersistence`

## `outputs/advanced-evidence/backend/services/pubmed_search.py`

Local source: `/Users/joshua/Documents/Codex/2026-09-29/can-x20-2/outputs/advanced-evidence/backend/services/pubmed_search.py` (source files are not included in this documentation push).

Bounded PubMed search with explicit provenance and an offline-safe cache. Search terms are transmitted to NCBI only when this client is enabled by the adapter. Never accepts arbitrary URLs. Never assigns a fact-checking 

**Top-level definitions/type:** `search_terms`, `parse_articles`, `PubMedSearch`

## `outputs/advanced-evidence/backups/persistence.py`

Local source: `/Users/joshua/Documents/Codex/2026-09-29/can-x20-2/outputs/advanced-evidence/backups/persistence.py` (source files are not included in this documentation push).

Python module; see defined symbols and source.

**Top-level definitions/type:** `PersistenceError`, `DuplicateRequestError`, `AuditPhaseRecord`, `AuditRecord`, `PersistenceResult`, `_enum_value`, `_sha256_bytes`, `_sha256_text`, `_safe_request_id`, `_canonical_json_bytes`, `_fsync_directory`, `_atomic_write_new`, `_phase_record`, `_extract_checkpoint_sha256`, `_model_artifact_summary`, `_build_invariant_checks`, `DecisionPackagePersistence`

## `outputs/advanced-evidence/backups/phase3_adapter.py`

Local source: `/Users/joshua/Documents/Codex/2026-09-29/can-x20-2/outputs/advanced-evidence/backups/phase3_adapter.py` (source files are not included in this documentation push).

Python module; see defined symbols and source.

**Top-level definitions/type:** `_utc_now`, `_iso_utc`, `_load_module_from_file`, `Phase3Adapter`

## `outputs/advanced-evidence/backups/pipeline.py`

Local source: `/Users/joshua/Documents/Codex/2026-09-29/can-x20-2/outputs/advanced-evidence/backups/pipeline.py` (source files are not included in this documentation push).

Python module; see defined symbols and source.

**Top-level definitions/type:** `_utc_now`, `_enum_value`, `_assert_success`, `_collect_models`, `BiomedicalVerificationPipeline`

## `outputs/advanced-evidence/backups/pipeline_config.py`

Local source: `/Users/joshua/Documents/Codex/2026-09-29/can-x20-2/outputs/advanced-evidence/backups/pipeline_config.py` (source files are not included in this documentation push).

Python module; see defined symbols and source.

**Top-level definitions/type:** `_env_path`, `_env_int`, `_env_float`, `Phase1Config`, `Phase2Config`, `Phase3Config`, `Phase4Config`, `Phase5Config`, `RuntimeConfig`, `PipelineConfig`, `load_pipeline_config`, `ensure_runtime_directories`, `validate_static_paths`

## `outputs/advanced-evidence/backups/schemas.py`

Local source: `/Users/joshua/Documents/Codex/2026-09-29/can-x20-2/outputs/advanced-evidence/backups/schemas.py` (source files are not included in this documentation push).

Python module; see defined symbols and source.

**Top-level definitions/type:** `Verdict`, `UserFacingVerdict`, `PhaseName`, `PhaseStatus`, `ExplanationStatus`, `AuthorityTier`, `Modality`, `BaseSchema`, `InferenceRequest`, `PhaseError`, `PhaseTiming`, `ModelArtifact`, `Phase1Result`, `EvidenceLineage`, `EvidenceRecord`, `RetrievalTrace`, `Phase2Result`, `Phase3Result`, `ClassProbabilities`, `PairwiseVerification`, `Phase4Result`, `GroundingMetrics`, `Phase5Result`, `PipelineProvenance`, `DecisionPackage`, `verdict_to_user_facing`

## `outputs/advanced-evidence/backups/adapters/phase2_adapter.py`

Local source: `/Users/joshua/Documents/Codex/2026-09-29/can-x20-2/outputs/advanced-evidence/backups/adapters/phase2_adapter.py` (source files are not included in this documentation push).

Python module; see defined symbols and source.

**Top-level definitions/type:** `_utc_now`, `_iso_utc`, `_sigmoid`, `Phase2ImportBundle`, `_prepare_phase2_modules`, `_restore_phase2_modules`, `Phase2Adapter`

## `outputs/advanced-evidence/backups/api/routes/system.py`

Local source: `/Users/joshua/Documents/Codex/2026-09-29/can-x20-2/outputs/advanced-evidence/backups/api/routes/system.py` (source files are not included in this documentation push).

Python module; see defined symbols and source.

**Top-level definitions/type:** `_utc_now_iso`, `health`, `models`

## `outputs/advanced-evidence/preapply-backup/pipeline.py`

Local source: `/Users/joshua/Documents/Codex/2026-09-29/can-x20-2/outputs/advanced-evidence/preapply-backup/pipeline.py` (source files are not included in this documentation push).

Python module; see defined symbols and source.

**Top-level definitions/type:** `_utc_now`, `_enum_value`, `_assert_success`, `_collect_models`, `BiomedicalVerificationPipeline`

## `outputs/advanced-evidence/preapply-backup/pipeline_config.py`

Local source: `/Users/joshua/Documents/Codex/2026-09-29/can-x20-2/outputs/advanced-evidence/preapply-backup/pipeline_config.py` (source files are not included in this documentation push).

Python module; see defined symbols and source.

**Top-level definitions/type:** `_env_path`, `_env_int`, `_env_float`, `Phase1Config`, `Phase2Config`, `Phase3Config`, `Phase4Config`, `Phase5Config`, `RuntimeConfig`, `PipelineConfig`, `load_pipeline_config`, `ensure_runtime_directories`, `validate_static_paths`

## `outputs/advanced-evidence/preapply-backup/schemas.py`

Local source: `/Users/joshua/Documents/Codex/2026-09-29/can-x20-2/outputs/advanced-evidence/preapply-backup/schemas.py` (source files are not included in this documentation push).

Python module; see defined symbols and source.

**Top-level definitions/type:** `Verdict`, `UserFacingVerdict`, `PhaseName`, `PhaseStatus`, `ExplanationStatus`, `AuthorityTier`, `Modality`, `BaseSchema`, `InferenceRequest`, `PhaseError`, `PhaseTiming`, `ModelArtifact`, `Phase1Result`, `EvidenceLineage`, `EvidenceRecord`, `RetrievalTrace`, `Phase2Result`, `Phase3Result`, `ClassProbabilities`, `PairwiseVerification`, `Phase4Result`, `GroundingMetrics`, `Phase5Result`, `PipelineProvenance`, `DecisionPackage`, `verdict_to_user_facing`

## `outputs/advanced-evidence/preapply-backup/adapters/phase2_adapter.py`

Local source: `/Users/joshua/Documents/Codex/2026-09-29/can-x20-2/outputs/advanced-evidence/preapply-backup/adapters/phase2_adapter.py` (source files are not included in this documentation push).

Python module; see defined symbols and source.

**Top-level definitions/type:** `_utc_now`, `_iso_utc`, `_sigmoid`, `Phase2ImportBundle`, `_prepare_phase2_modules`, `_restore_phase2_modules`, `Phase2Adapter`

## `outputs/advanced-evidence/preapply-backup/adapters/phase3_adapter.py`

Local source: `/Users/joshua/Documents/Codex/2026-09-29/can-x20-2/outputs/advanced-evidence/preapply-backup/adapters/phase3_adapter.py` (source files are not included in this documentation push).

Python module; see defined symbols and source.

**Top-level definitions/type:** `_utc_now`, `_iso_utc`, `_load_module_from_file`, `Phase3Adapter`

## `outputs/advanced-evidence/preapply-backup/api/routes/system.py`

Local source: `/Users/joshua/Documents/Codex/2026-09-29/can-x20-2/outputs/advanced-evidence/preapply-backup/api/routes/system.py` (source files are not included in this documentation push).

Python module; see defined symbols and source.

**Top-level definitions/type:** `_utc_now_iso`, `health`, `models`

## `outputs/advanced-evidence/preapply-backup/services/persistence.py`

Local source: `/Users/joshua/Documents/Codex/2026-09-29/can-x20-2/outputs/advanced-evidence/preapply-backup/services/persistence.py` (source files are not included in this documentation push).

Python module; see defined symbols and source.

**Top-level definitions/type:** `PersistenceError`, `DuplicateRequestError`, `AuditPhaseRecord`, `AuditRecord`, `PersistenceResult`, `_enum_value`, `_sha256_bytes`, `_sha256_text`, `_safe_request_id`, `_canonical_json_bytes`, `_fsync_directory`, `_atomic_write_new`, `_phase_record`, `_extract_checkpoint_sha256`, `_model_artifact_summary`, `_build_invariant_checks`, `DecisionPackagePersistence`

## `outputs/advanced-evidence/tests/test_integration.py`

Local source: `/Users/joshua/Documents/Codex/2026-09-29/can-x20-2/outputs/advanced-evidence/tests/test_integration.py` (source files are not included in this documentation push).

Python module; see defined symbols and source.

**Top-level definitions/type:** `TestPipeline`

## `outputs/advanced-evidence/tests/test_nli.py`

Local source: `/Users/joshua/Documents/Codex/2026-09-29/can-x20-2/outputs/advanced-evidence/tests/test_nli.py` (source files are not included in this documentation push).

Python module; see defined symbols and source.

**Top-level definitions/type:** `TestNli`

## `outputs/advanced-evidence/tests/test_pubmed_search.py`

Local source: `/Users/joshua/Documents/Codex/2026-09-29/can-x20-2/outputs/advanced-evidence/tests/test_pubmed_search.py` (source files are not included in this documentation push).

Python module; see defined symbols and source.

**Top-level definitions/type:** `Response`, `Session`, `Tests`

## `outputs/aggregation-experiment/run.py`

Local source: `/Users/joshua/Documents/Codex/2026-09-29/can-x20-2/outputs/aggregation-experiment/run.py` (source files are not included in this documentation push).

Exploratory development aggregation diagnostics on cached predictions. No retrieval, neural inference, deployment changes, or final-test access.

**Top-level definitions/type:** `softmax`, `inputs`, `features`, `fixed_methods`, `main`

## `outputs/aggregation-experiment/run_aggregation.command`

Local source: `/Users/joshua/Documents/Codex/2026-09-29/can-x20-2/outputs/aggregation-experiment/run_aggregation.command` (source files are not included in this documentation push).

Shell entry point; inspect paths and arguments before running.

**Top-level definitions/type:** Shell

## `outputs/aggregation-experiment/test_aggregation.py`

Local source: `/Users/joshua/Documents/Codex/2026-09-29/can-x20-2/outputs/aggregation-experiment/test_aggregation.py` (source files are not included in this documentation push).

Python module; see defined symbols and source.

**Top-level definitions/type:** `Tests`

## `outputs/biomedical-verifier-blue/app.js`

Local source: `/Users/joshua/Documents/Codex/2026-09-29/can-x20-2/outputs/biomedical-verifier-blue/app.js` (source files are not included in this documentation push).

Frontend/source asset; follow the source link for implementation.

**Top-level definitions/type:** js

## `outputs/biomedical-verifier-blue/index.html`

Local source: `/Users/joshua/Documents/Codex/2026-09-29/can-x20-2/outputs/biomedical-verifier-blue/index.html` (source files are not included in this documentation push).

Frontend/source asset; follow the source link for implementation.

**Top-level definitions/type:** html

## `outputs/biomedical-verifier-blue/insights.js`

Local source: `/Users/joshua/Documents/Codex/2026-09-29/can-x20-2/outputs/biomedical-verifier-blue/insights.js` (source files are not included in this documentation push).

Frontend/source asset; follow the source link for implementation.

**Top-level definitions/type:** js

## `outputs/biomedical-verifier-blue/netlify.toml`

Local source: `/Users/joshua/Documents/Codex/2026-09-29/can-x20-2/outputs/biomedical-verifier-blue/netlify.toml` (source files are not included in this documentation push).

Configuration file; values are intentionally not copied into this catalog.

**Top-level definitions/type:** Configuration

## `outputs/biomedical-verifier-blue/serve.py`

Local source: `/Users/joshua/Documents/Codex/2026-09-29/can-x20-2/outputs/biomedical-verifier-blue/serve.py` (source files are not included in this documentation push).

Local-only preview with a fixed backend bridge. Not a Netlify server.

**Top-level definitions/type:** `Handler`

## `outputs/biomedical-verifier-blue/styles.css`

Local source: `/Users/joshua/Documents/Codex/2026-09-29/can-x20-2/outputs/biomedical-verifier-blue/styles.css` (source files are not included in this documentation push).

Frontend/source asset; follow the source link for implementation.

**Top-level definitions/type:** css

## `outputs/clean-selector/audit_evidence.py`

Local source: `/Users/joshua/Documents/Codex/2026-09-29/can-x20-2/outputs/clean-selector/audit_evidence.py` (source files are not included in this documentation push).

Python module; see defined symbols and source.

**Top-level definitions/type:** No top-level functions/classes.

## `outputs/corpus-connection/phase2_adapter.before.py`

Local source: `/Users/joshua/Documents/Codex/2026-09-29/can-x20-2/outputs/corpus-connection/phase2_adapter.before.py` (source files are not included in this documentation push).

Python module; see defined symbols and source.

**Top-level definitions/type:** `_utc_now`, `_iso_utc`, `_sigmoid`, `Phase2ImportBundle`, `_prepare_phase2_modules`, `_restore_phase2_modules`, `Phase2Adapter`

## `outputs/corpus-connection/phase2_adapter.py`

Local source: `/Users/joshua/Documents/Codex/2026-09-29/can-x20-2/outputs/corpus-connection/phase2_adapter.py` (source files are not included in this documentation push).

Python module; see defined symbols and source.

**Top-level definitions/type:** `_utc_now`, `_iso_utc`, `_sigmoid`, `Phase2ImportBundle`, `_prepare_phase2_modules`, `_restore_phase2_modules`, `Phase2Adapter`

## `outputs/corpus-connection/pipeline_config.before.py`

Local source: `/Users/joshua/Documents/Codex/2026-09-29/can-x20-2/outputs/corpus-connection/pipeline_config.before.py` (source files are not included in this documentation push).

Python module; see defined symbols and source.

**Top-level definitions/type:** `_env_path`, `_env_int`, `_env_float`, `Phase1Config`, `Phase2Config`, `Phase3Config`, `Phase4Config`, `Phase5Config`, `RuntimeConfig`, `PipelineConfig`, `load_pipeline_config`, `ensure_runtime_directories`, `validate_static_paths`

## `outputs/corpus-connection/pipeline_config.py`

Local source: `/Users/joshua/Documents/Codex/2026-09-29/can-x20-2/outputs/corpus-connection/pipeline_config.py` (source files are not included in this documentation push).

Python module; see defined symbols and source.

**Top-level definitions/type:** `_env_path`, `_env_int`, `_env_float`, `Phase1Config`, `Phase2Config`, `Phase3Config`, `Phase4Config`, `Phase5Config`, `RuntimeConfig`, `PipelineConfig`, `load_pipeline_config`, `ensure_runtime_directories`, `validate_static_paths`

## `outputs/day-run/run_today.command`

Local source: `/Users/joshua/Documents/Codex/2026-09-29/can-x20-2/outputs/day-run/run_today.command` (source files are not included in this documentation push).

Shell entry point; inspect paths and arguments before running.

**Top-level definitions/type:** Shell

## `outputs/day-run/summarize.py`

Local source: `/Users/joshua/Documents/Codex/2026-09-29/can-x20-2/outputs/day-run/summarize.py` (source files are not included in this documentation push).

Python module; see defined symbols and source.

**Top-level definitions/type:** No top-level functions/classes.

## `outputs/deberta-verifier/run_experiment.py`

Local source: `/Users/joshua/Documents/Codex/2026-09-29/can-x20-2/outputs/deberta-verifier/run_experiment.py` (source files are not included in this documentation push).

Stronger NLI with sentence/context inputs; training-only policy selection.

**Top-level definitions/type:** `save`, `context_text`, `main`

## `outputs/evidence-combiner/analyze_results.py`

Local source: `/Users/joshua/Documents/Codex/2026-09-29/can-x20-2/outputs/evidence-combiner/analyze_results.py` (source files are not included in this documentation push).

Matched development comparison with document-group bootstrap uncertainty.

**Top-level definitions/type:** `main`

## `outputs/evidence-combiner/audit_corpus.py`

Local source: `/Users/joshua/Documents/Codex/2026-09-29/can-x20-2/outputs/evidence-combiner/audit_corpus.py` (source files are not included in this documentation push).

Read-only structural audit of the corpus and dense index.

**Top-level definitions/type:** No top-level functions/classes.

## `outputs/evidence-combiner/candidate.py`

Local source: `/Users/joshua/Documents/Codex/2026-09-29/can-x20-2/outputs/evidence-combiner/candidate.py` (source files are not included in this documentation push).

Standalone experimental full-corpus classifier; no server/deployment changes.

**Top-level definitions/type:** `Candidate`, `main`

## `outputs/evidence-combiner/compare_learners.py`

Local source: `/Users/joshua/Documents/Codex/2026-09-29/can-x20-2/outputs/evidence-combiner/compare_learners.py` (source files are not included in this documentation push).

Select a fixed small learner family on grouped TRAINING predictions only.

**Top-level definitions/type:** `main`

## `outputs/evidence-combiner/core.py`

Local source: `/Users/joshua/Documents/Codex/2026-09-29/can-x20-2/outputs/evidence-combiner/core.py` (source files are not included in this documentation push).

Label-independent sparse retrieval and evidence-combination features.

**Top-level definitions/type:** `SparseBM25`, `feature_vector`, `baselines`, `claim_label`, `linked_groups`

## `outputs/evidence-combiner/dashboard_backend.py`

Local source: `/Users/joshua/Documents/Codex/2026-09-29/can-x20-2/outputs/evidence-combiner/dashboard_backend.py` (source files are not included in this documentation push).

Opt-in dashboard integration; original project files are never edited.

**Top-level definitions/type:** `Shared`, `Retrieval`, `Verification`, `create_app`

## `outputs/evidence-combiner/evaluate_live.py`

Local source: `/Users/joshua/Documents/Codex/2026-09-29/can-x20-2/outputs/evidence-combiner/evaluate_live.py` (source files are not included in this documentation push).

Resumable live-retrieval evaluation; never changes dashboard defaults.

**Top-level definitions/type:** No top-level functions/classes.

## `outputs/evidence-combiner/evaluate_selected.py`

Local source: `/Users/joshua/Documents/Codex/2026-09-29/can-x20-2/outputs/evidence-combiner/evaluate_selected.py` (source files are not included in this documentation push).

Python module; see defined symbols and source.

**Top-level definitions/type:** No top-level functions/classes.

## `outputs/evidence-combiner/fit_decision_policy.py`

Local source: `/Users/joshua/Documents/Codex/2026-09-29/can-x20-2/outputs/evidence-combiner/fit_decision_policy.py` (source files are not included in this documentation push).

Python module; see defined symbols and source.

**Top-level definitions/type:** No top-level functions/classes.

## `outputs/evidence-combiner/passage_features.py`

Local source: `/Users/joshua/Documents/Codex/2026-09-29/can-x20-2/outputs/evidence-combiner/passage_features.py` (source files are not included in this documentation push).

Generic relevance diagnostics; no benchmark annotations or IDs in features.

**Top-level definitions/type:** `tokens`, `overlap_features`, `extract`

## `outputs/evidence-combiner/predict.py`

Local source: `/Users/joshua/Documents/Codex/2026-09-29/can-x20-2/outputs/evidence-combiner/predict.py` (source files are not included in this documentation push).

Experimental combiner inference, deliberately not wired into production.

**Top-level definitions/type:** `predict`

## `outputs/evidence-combiner/run.py`

Local source: `/Users/joshua/Documents/Codex/2026-09-29/can-x20-2/outputs/evidence-combiner/run.py` (source files are not included in this documentation push).

Full-corpus retrieval experiment; training-only learned aggregation.

**Top-level definitions/type:** `sha`, `save`, `read_lines`, `metrics`, `main`

## `outputs/evidence-combiner/run_clean_selector.py`

Local source: `/Users/joshua/Documents/Codex/2026-09-29/can-x20-2/outputs/evidence-combiner/run_clean_selector.py` (source files are not included in this documentation push).

Keep retrieval fixed; test whether neighboring sentences repair lost context.

**Top-level definitions/type:** No top-level functions/classes.

## `outputs/evidence-combiner/run_context.py`

Local source: `/Users/joshua/Documents/Codex/2026-09-29/can-x20-2/outputs/evidence-combiner/run_context.py` (source files are not included in this documentation push).

Keep retrieval fixed; test whether neighboring sentences repair lost context.

**Top-level definitions/type:** No top-level functions/classes.

## `outputs/evidence-combiner/run_evidence_first.py`

Local source: `/Users/joshua/Documents/Codex/2026-09-29/can-x20-2/outputs/evidence-combiner/run_evidence_first.py` (source files are not included in this documentation push).

Rank candidate documents with both abstract and selected-evidence relevance.

**Top-level definitions/type:** No top-level functions/classes.

## `outputs/evidence-combiner/run_experiment.command`

Local source: `/Users/joshua/Documents/Codex/2026-09-29/can-x20-2/outputs/evidence-combiner/run_experiment.command` (source files are not included in this documentation push).

Shell entry point; inspect paths and arguments before running.

**Top-level definitions/type:** Shell

## `outputs/evidence-combiner/run_joint_passages.py`

Local source: `/Users/joshua/Documents/Codex/2026-09-29/can-x20-2/outputs/evidence-combiner/run_joint_passages.py` (source files are not included in this documentation push).

Verify two selected sentences jointly, preserving complete first passage.

**Top-level definitions/type:** No top-level functions/classes.

## `outputs/evidence-combiner/run_wide150.py`

Local source: `/Users/joshua/Documents/Codex/2026-09-29/can-x20-2/outputs/evidence-combiner/run_wide150.py` (source files are not included in this documentation push).

Full-corpus retrieval experiment; training-only learned aggregation.

**Top-level definitions/type:** `sha`, `save`, `read_lines`, `metrics`, `main`

## `outputs/evidence-combiner/start_backend.command`

Local source: `/Users/joshua/Documents/Codex/2026-09-29/can-x20-2/outputs/evidence-combiner/start_backend.command` (source files are not included in this documentation push).

Shell entry point; inspect paths and arguments before running.

**Top-level definitions/type:** Shell

## `outputs/evidence-combiner/start_frontend.command`

Local source: `/Users/joshua/Documents/Codex/2026-09-29/can-x20-2/outputs/evidence-combiner/start_frontend.command` (source files are not included in this documentation push).

Shell entry point; inspect paths and arguments before running.

**Top-level definitions/type:** Shell

## `outputs/evidence-combiner/start_project.py`

Local source: `/Users/joshua/Documents/Codex/2026-09-29/can-x20-2/outputs/evidence-combiner/start_project.py` (source files are not included in this documentation push).

Start the local research dashboard; never terminate pre-existing servers.

**Top-level definitions/type:** `get`, `listening`, `start`, `wait_for`, `backend_ready`, `frontend_ready`, `main`

## `outputs/evidence-combiner/summarize_oct8.py`

Local source: `/Users/joshua/Documents/Codex/2026-09-29/can-x20-2/outputs/evidence-combiner/summarize_oct8.py` (source files are not included in this documentation push).

Summarize completed experiments without modifying serving configuration.

**Top-level definitions/type:** No top-level functions/classes.

## `outputs/evidence-combiner/test_core.py`

Local source: `/Users/joshua/Documents/Codex/2026-09-29/can-x20-2/outputs/evidence-combiner/test_core.py` (source files are not included in this documentation push).

Python module; see defined symbols and source.

**Top-level definitions/type:** `Tests`

## `outputs/evidence-combiner/test_dashboard.py`

Local source: `/Users/joshua/Documents/Codex/2026-09-29/can-x20-2/outputs/evidence-combiner/test_dashboard.py` (source files are not included in this documentation push).

Python module; see defined symbols and source.

**Top-level definitions/type:** `Tests`

## `outputs/evidence-combiner/test_passage_features.py`

Local source: `/Users/joshua/Documents/Codex/2026-09-29/can-x20-2/outputs/evidence-combiner/test_passage_features.py` (source files are not included in this documentation push).

Python module; see defined symbols and source.

**Top-level definitions/type:** `Tests`

## `outputs/evidence-combiner/test_predict.py`

Local source: `/Users/joshua/Documents/Codex/2026-09-29/can-x20-2/outputs/evidence-combiner/test_predict.py` (source files are not included in this documentation push).

Python module; see defined symbols and source.

**Top-level definitions/type:** `Tests`

## `outputs/evidence-combiner/test_prediction_cache.py`

Local source: `/Users/joshua/Documents/Codex/2026-09-29/can-x20-2/outputs/evidence-combiner/test_prediction_cache.py` (source files are not included in this documentation push).

Python module; see defined symbols and source.

**Top-level definitions/type:** `CacheTests`

## `outputs/evidence-combiner/train_clean_selector_combiner.py`

Local source: `/Users/joshua/Documents/Codex/2026-09-29/can-x20-2/outputs/evidence-combiner/train_clean_selector_combiner.py` (source files are not included in this documentation push).

Training-selected combiner with explicit selected-passage relevance features.

**Top-level definitions/type:** `main`

## `outputs/evidence-combiner/train_context_combiner.py`

Local source: `/Users/joshua/Documents/Codex/2026-09-29/can-x20-2/outputs/evidence-combiner/train_context_combiner.py` (source files are not included in this documentation push).

Training-selected combiner with explicit selected-passage relevance features.

**Top-level definitions/type:** `main`

## `outputs/evidence-combiner/train_dual_context.py`

Local source: `/Users/joshua/Documents/Codex/2026-09-29/can-x20-2/outputs/evidence-combiner/train_dual_context.py` (source files are not included in this documentation push).

Training-selected combiner with explicit selected-passage relevance features.

**Top-level definitions/type:** `main`

## `outputs/evidence-combiner/train_evidence_first.py`

Local source: `/Users/joshua/Documents/Codex/2026-09-29/can-x20-2/outputs/evidence-combiner/train_evidence_first.py` (source files are not included in this documentation push).

Training-selected combiner with explicit selected-passage relevance features.

**Top-level definitions/type:** `main`

## `outputs/evidence-combiner/train_joint_passages.py`

Local source: `/Users/joshua/Documents/Codex/2026-09-29/can-x20-2/outputs/evidence-combiner/train_joint_passages.py` (source files are not included in this documentation push).

Training-selected combiner with explicit selected-passage relevance features.

**Top-level definitions/type:** `main`

## `outputs/evidence-combiner/train_multipassage.py`

Local source: `/Users/joshua/Documents/Codex/2026-09-29/can-x20-2/outputs/evidence-combiner/train_multipassage.py` (source files are not included in this documentation push).

Training-selected combiner with explicit selected-passage relevance features.

**Top-level definitions/type:** `main`

## `outputs/evidence-combiner/train_passage_combiner.py`

Local source: `/Users/joshua/Documents/Codex/2026-09-29/can-x20-2/outputs/evidence-combiner/train_passage_combiner.py` (source files are not included in this documentation push).

Training-selected combiner with explicit selected-passage relevance features.

**Top-level definitions/type:** `main`

## `outputs/evidence-combiner/train_regularized.py`

Local source: `/Users/joshua/Documents/Codex/2026-09-29/can-x20-2/outputs/evidence-combiner/train_regularized.py` (source files are not included in this documentation push).

Training-selected combiner with explicit selected-passage relevance features.

**Top-level definitions/type:** `main`

## `outputs/evidence-combiner/train_wide150_combiner.py`

Local source: `/Users/joshua/Documents/Codex/2026-09-29/can-x20-2/outputs/evidence-combiner/train_wide150_combiner.py` (source files are not included in this documentation push).

Training-selected combiner with explicit selected-passage relevance features.

**Top-level definitions/type:** `main`

## `outputs/evidence-combiner/verify_run.py`

Local source: `/Users/joshua/Documents/Codex/2026-09-29/can-x20-2/outputs/evidence-combiner/verify_run.py` (source files are not included in this documentation push).

Verify trained JSON artifact, separation and complete inference results.

**Top-level definitions/type:** `read`, `main`

## `outputs/grounded-verifier/run.py`

Local source: `/Users/joshua/Documents/Codex/2026-09-29/can-x20-2/outputs/grounded-verifier/run.py` (source files are not included in this documentation push).

Fixed-prompt local evidence verifier. No gold evidence supplied to inference.

**Top-level definitions/type:** `save`, `norm`, `validate`, `main`

## `outputs/grounded-verifier/run_v2.py`

Local source: `/Users/joshua/Documents/Codex/2026-09-29/can-x20-2/outputs/grounded-verifier/run_v2.py` (source files are not included in this documentation push).

Fixed-prompt local evidence verifier. No gold evidence supplied to inference.

**Top-level definitions/type:** `save`, `norm`, `validate`, `main`

## `outputs/healthver-adaptation/run.py`

Local source: `/Users/joshua/Documents/Codex/2026-09-29/can-x20-2/outputs/healthver-adaptation/run.py` (source files are not included in this documentation push).

Training-only biomedical NLI adaptation; no development-guided model choice.

**Top-level definitions/type:** `save`, `lines`, `main`

## `outputs/medical-vision/analyzer.py`

Local source: `/Users/joshua/Documents/Codex/2026-09-29/can-x20-2/outputs/medical-vision/analyzer.py` (source files are not included in this documentation push).

Research-only frontal chest-X-ray scores, kept separate from text verdicts.

**Top-level definitions/type:** `preprocess`, `analyze`

## `outputs/medical-vision/test_analyzer.py`

Local source: `/Users/joshua/Documents/Codex/2026-09-29/can-x20-2/outputs/medical-vision/test_analyzer.py` (source files are not included in this documentation push).

Python module; see defined symbols and source.

**Top-level definitions/type:** `Tests`

## `outputs/multipassage/run.py`

Local source: `/Users/joshua/Documents/Codex/2026-09-29/can-x20-2/outputs/multipassage/run.py` (source files are not included in this documentation push).

Two independently scored evidence sentences per retrieved document.

**Top-level definitions/type:** No top-level functions/classes.

## `outputs/multivers-probe/download.py`

Local source: `/Users/joshua/Documents/Codex/2026-09-29/can-x20-2/outputs/multivers-probe/download.py` (source files are not included in this documentation push).

Python module; see defined symbols and source.

**Top-level definitions/type:** No top-level functions/classes.

## `outputs/multivers-probe/download_parallel.py`

Local source: `/Users/joshua/Documents/Codex/2026-09-29/can-x20-2/outputs/multivers-probe/download_parallel.py` (source files are not included in this documentation push).

Bounded, resumable download of the authors' version-pinned checkpoint.

**Top-level definitions/type:** `fetch`

## `outputs/multivers-probe/inference.py`

Local source: `/Users/joshua/Documents/Codex/2026-09-29/can-x20-2/outputs/multivers-probe/inference.py` (source files are not included in this documentation push).

Inference-only port of the pinned MIT-licensed MultiVerS architecture. See upstream/model.py, data.py and LICENSE for original implementation.

**Top-level definitions/type:** `Head`, `Network`, `Verifier`

## `outputs/multivers-probe/screen.py`

Local source: `/Users/joshua/Documents/Codex/2026-09-29/can-x20-2/outputs/multivers-probe/screen.py` (source files are not included in this documentation push).

Runtime and training-split screen; never evaluates development labels.

**Top-level definitions/type:** No top-level functions/classes.

## `outputs/multivers-probe/test_encoding.py`

Local source: `/Users/joshua/Documents/Codex/2026-09-29/can-x20-2/outputs/multivers-probe/test_encoding.py` (source files are not included in this documentation push).

Check the inference port against the authors' pinned preprocessing class.

**Top-level definitions/type:** `Tests`

## `outputs/multivers-probe/upstream/allennlp_feedforward.py`

Local source: `/Users/joshua/Documents/Codex/2026-09-29/can-x20-2/outputs/multivers-probe/upstream/allennlp_feedforward.py` (source files are not included in this documentation push).

Python module; see defined symbols and source.

**Top-level definitions/type:** `ConfigurationError`, `FeedForward`

## `outputs/multivers-probe/upstream/data.py`

Local source: `/Users/joshua/Documents/Codex/2026-09-29/can-x20-2/outputs/multivers-probe/upstream/data.py` (source files are not included in this documentation push).

Module to handle data for inference.

**Top-level definitions/type:** `get_tokenizer`, `MultiVerSDataset`, `MultiVerSReader`, `Collator`, `get_dataloader`

## `outputs/multivers-probe/upstream/model.py`

Local source: `/Users/joshua/Documents/Codex/2026-09-29/can-x20-2/outputs/multivers-probe/upstream/model.py` (source files are not included in this documentation push).

Python module; see defined symbols and source.

**Top-level definitions/type:** `masked_binary_cross_entropy_with_logits`, `MultiVerSModel`

## `outputs/passage-experiment/passages.py`

Local source: `/Users/joshua/Documents/Codex/2026-09-29/can-x20-2/outputs/passage-experiment/passages.py` (source files are not included in this documentation push).

Claim-conditioned extractive passages. No labels or annotations accepted.

**Top-level definitions/type:** `windows`, `select_passage`

## `outputs/passage-experiment/run.py`

Local source: `/Users/joshua/Documents/Codex/2026-09-29/can-x20-2/outputs/passage-experiment/run.py` (source files are not included in this documentation push).

Python module; see defined symbols and source.

**Top-level definitions/type:** `report`, `main`

## `outputs/passage-experiment/run_passages.command`

Local source: `/Users/joshua/Documents/Codex/2026-09-29/can-x20-2/outputs/passage-experiment/run_passages.command` (source files are not included in this documentation push).

Shell entry point; inspect paths and arguments before running.

**Top-level definitions/type:** Shell

## `outputs/passage-experiment/test_passages.py`

Local source: `/Users/joshua/Documents/Codex/2026-09-29/can-x20-2/outputs/passage-experiment/test_passages.py` (source files are not included in this documentation push).

Python module; see defined symbols and source.

**Top-level definitions/type:** `Tokenizer`, `Ranker`, `Tests`

## `outputs/project-evaluation/evaluate.py`

Local source: `/Users/joshua/Documents/Codex/2026-09-29/can-x20-2/outputs/project-evaluation/evaluate.py` (source files are not included in this documentation push).

Resumable SciFact DEVELOPMENT evaluation. Never reads claims_test.jsonl. Shares actual Phase 2/3 results between verifiers. Does not change deployment, train models, or claim clinical accuracy. See README.md for scope an

**Top-level definitions/type:** `sha`, `save`, `cases_from`, `metrics`, `summarize`, `main`

## `outputs/project-evaluation/run_advanced.command`

Local source: `/Users/joshua/Documents/Codex/2026-09-29/can-x20-2/outputs/project-evaluation/run_advanced.command` (source files are not included in this documentation push).

Shell entry point; inspect paths and arguments before running.

**Top-level definitions/type:** Shell

## `outputs/project-evaluation/run_full.command`

Local source: `/Users/joshua/Documents/Codex/2026-09-29/can-x20-2/outputs/project-evaluation/run_full.command` (source files are not included in this documentation push).

Shell entry point; inspect paths and arguments before running.

**Top-level definitions/type:** Shell

## `outputs/project-evaluation/test_evaluation.py`

Local source: `/Users/joshua/Documents/Codex/2026-09-29/can-x20-2/outputs/project-evaluation/test_evaluation.py` (source files are not included in this documentation push).

Python module; see defined symbols and source.

**Top-level definitions/type:** `EvaluationTests`

## `outputs/project-evaluation/diagnostics/advanced_diagnostics.py`

Local source: `/Users/joshua/Documents/Codex/2026-09-29/can-x20-2/outputs/project-evaluation/diagnostics/advanced_diagnostics.py` (source files are not included in this documentation push).

Offline development diagnostics; never trains or changes deployment.

**Top-level definitions/type:** `gold_records`, `selection_report`, `summarize`, `main`

## `outputs/project-evaluation/diagnostics/analyze_saved.py`

Local source: `/Users/joshua/Documents/Codex/2026-09-29/can-x20-2/outputs/project-evaluation/diagnostics/analyze_saved.py` (source files are not included in this documentation push).

Python module; see defined symbols and source.

**Top-level definitions/type:** No top-level functions/classes.

## `outputs/project-evaluation/diagnostics/test_advanced.py`

Local source: `/Users/joshua/Documents/Codex/2026-09-29/can-x20-2/outputs/project-evaluation/diagnostics/test_advanced.py` (source files are not included in this documentation push).

Python module; see defined symbols and source.

**Top-level definitions/type:** `Tests`

## `outputs/regression-audit/audit.py`

Local source: `/Users/joshua/Documents/Codex/2026-09-29/can-x20-2/outputs/regression-audit/audit.py` (source files are not included in this documentation push).

Read-only, annotation-assisted development error audit. No deployment or fitting.

**Top-level definitions/type:** `read`, `norm`, `coverage`, `argmax`, `main`

## `outputs/regression-audit/run_audit.command`

Local source: `/Users/joshua/Documents/Codex/2026-09-29/can-x20-2/outputs/regression-audit/run_audit.command` (source files are not included in this documentation push).

Shell entry point; inspect paths and arguments before running.

**Top-level definitions/type:** Shell

## `outputs/regression-audit/test_audit.py`

Local source: `/Users/joshua/Documents/Codex/2026-09-29/can-x20-2/outputs/regression-audit/test_audit.py` (source files are not included in this documentation push).

Python module; see defined symbols and source.

**Top-level definitions/type:** `CoverageTests`

## `outputs/relation-adaptation/run.py`

Local source: `/Users/joshua/Documents/Codex/2026-09-29/can-x20-2/outputs/relation-adaptation/run.py` (source files are not included in this documentation push).

Training-only biomedical NLI adaptation; no development-guided model choice.

**Top-level definitions/type:** `save`, `lines`, `main`

## `outputs/retrieval-improvement/phase2_adapter.before.py`

Local source: `/Users/joshua/Documents/Codex/2026-09-29/can-x20-2/outputs/retrieval-improvement/phase2_adapter.before.py` (source files are not included in this documentation push).

Python module; see defined symbols and source.

**Top-level definitions/type:** `_utc_now`, `_iso_utc`, `_sigmoid`, `Phase2ImportBundle`, `_prepare_phase2_modules`, `_restore_phase2_modules`, `Phase2Adapter`

## `outputs/retrieval-improvement/backend/adapters/phase2_adapter.py`

Local source: `/Users/joshua/Documents/Codex/2026-09-29/can-x20-2/outputs/retrieval-improvement/backend/adapters/phase2_adapter.py` (source files are not included in this documentation push).

Python module; see defined symbols and source.

**Top-level definitions/type:** `_utc_now`, `_iso_utc`, `_sigmoid`, `Phase2ImportBundle`, `_prepare_phase2_modules`, `_restore_phase2_modules`, `Phase2Adapter`

## `outputs/retrieval-improvement/tests/test_claim_reranking.py`

Local source: `/Users/joshua/Documents/Codex/2026-09-29/can-x20-2/outputs/retrieval-improvement/tests/test_claim_reranking.py` (source files are not included in this documentation push).

Python module; see defined symbols and source.

**Top-level definitions/type:** `Reranker`, `doc`, `Tests`

## `outputs/selector-integration/run.py`

Local source: `/Users/joshua/Documents/Codex/2026-09-29/can-x20-2/outputs/selector-integration/run.py` (source files are not included in this documentation push).

Python module; see defined symbols and source.

**Top-level definitions/type:** `report`, `main`

## `outputs/selector-integration/run_comparison.command`

Local source: `/Users/joshua/Documents/Codex/2026-09-29/can-x20-2/outputs/selector-integration/run_comparison.command` (source files are not included in this documentation push).

Shell entry point; inspect paths and arguments before running.

**Top-level definitions/type:** Shell

## `outputs/selector-integration/sentences.py`

Local source: `/Users/joshua/Documents/Codex/2026-09-29/can-x20-2/outputs/selector-integration/sentences.py` (source files are not included in this documentation push).

Inference accepts claim/document text only; never benchmark annotations.

**Top-level definitions/type:** `sentence_units`, `choose`

## `outputs/selector-integration/test_sentences.py`

Local source: `/Users/joshua/Documents/Codex/2026-09-29/can-x20-2/outputs/selector-integration/test_sentences.py` (source files are not included in this documentation push).

Python module; see defined symbols and source.

**Top-level definitions/type:** `Tokenizer`, `Ranker`, `Tests`

## `outputs/supervised-selector/audit_passages.py`

Local source: `/Users/joshua/Documents/Codex/2026-09-29/can-x20-2/outputs/supervised-selector/audit_passages.py` (source files are not included in this documentation push).

Python module; see defined symbols and source.

**Top-level definitions/type:** No top-level functions/classes.

## `outputs/supervised-selector/run_training.command`

Local source: `/Users/joshua/Documents/Codex/2026-09-29/can-x20-2/outputs/supervised-selector/run_training.command` (source files are not included in this documentation push).

Shell entry point; inspect paths and arguments before running.

**Top-level definitions/type:** Shell

## `outputs/supervised-selector/test_training.py`

Local source: `/Users/joshua/Documents/Codex/2026-09-29/can-x20-2/outputs/supervised-selector/test_training.py` (source files are not included in this documentation push).

Python module; see defined symbols and source.

**Top-level definitions/type:** `Tests`

## `outputs/supervised-selector/train_selector.py`

Local source: `/Users/joshua/Documents/Codex/2026-09-29/can-x20-2/outputs/supervised-selector/train_selector.py` (source files are not included in this documentation push).

Train a sentence-evidence selector; never read development/test labels. Labels mean annotated evidence relevance, NOT supported/refuted claim verdicts.

**Top-level definitions/type:** `write`, `digest`, `tokens`, `build_data`, `ranking_metrics`, `main`

## `outputs/verifier-adaptation/run.py`

Local source: `/Users/joshua/Documents/Codex/2026-09-29/can-x20-2/outputs/verifier-adaptation/run.py` (source files are not included in this documentation push).

Training-only biomedical NLI adaptation; no development-guided model choice.

**Top-level definitions/type:** `save`, `lines`, `main`

## `work/apply_enhancements.py`

Local source: `/Users/joshua/Documents/Codex/2026-09-29/can-x20-2/work/apply_enhancements.py` (source files are not included in this documentation push).

Python module; see defined symbols and source.

**Top-level definitions/type:** No top-level functions/classes.

## `work/audit_verifiers.py`

Local source: `/Users/joshua/Documents/Codex/2026-09-29/can-x20-2/work/audit_verifiers.py` (source files are not included in this documentation push).

Python module; see defined symbols and source.

**Top-level definitions/type:** No top-level functions/classes.

## `work/build_selector_integration.py`

Local source: `/Users/joshua/Documents/Codex/2026-09-29/can-x20-2/work/build_selector_integration.py` (source files are not included in this documentation push).

Python module; see defined symbols and source.

**Top-level definitions/type:** No top-level functions/classes.

## `work/check_35k.py`

Local source: `/Users/joshua/Documents/Codex/2026-09-29/can-x20-2/work/check_35k.py` (source files are not included in this documentation push).

Python module; see defined symbols and source.

**Top-level definitions/type:** No top-level functions/classes.

## `work/evaluate_dev_pairs.py`

Local source: `/Users/joshua/Documents/Codex/2026-09-29/can-x20-2/work/evaluate_dev_pairs.py` (source files are not included in this documentation push).

Python module; see defined symbols and source.

**Top-level definitions/type:** No top-level functions/classes.

## `work/evaluate_retrieval.py`

Local source: `/Users/joshua/Documents/Codex/2026-09-29/can-x20-2/work/evaluate_retrieval.py` (source files are not included in this documentation push).

Python module; see defined symbols and source.

**Top-level definitions/type:** No top-level functions/classes.

## `work/finalize_lineage.py`

Local source: `/Users/joshua/Documents/Codex/2026-09-29/can-x20-2/work/finalize_lineage.py` (source files are not included in this documentation push).

Python module; see defined symbols and source.

**Top-level definitions/type:** No top-level functions/classes.

## `work/finish_retrieval.py`

Local source: `/Users/joshua/Documents/Codex/2026-09-29/can-x20-2/work/finish_retrieval.py` (source files are not included in this documentation push).

Python module; see defined symbols and source.

**Top-level definitions/type:** No top-level functions/classes.

## `work/fix_long_evidence.py`

Local source: `/Users/joshua/Documents/Codex/2026-09-29/can-x20-2/work/fix_long_evidence.py` (source files are not included in this documentation push).

Python module; see defined symbols and source.

**Top-level definitions/type:** No top-level functions/classes.

## `work/fix_persistence.py`

Local source: `/Users/joshua/Documents/Codex/2026-09-29/can-x20-2/work/fix_persistence.py` (source files are not included in this documentation push).

Python module; see defined symbols and source.

**Top-level definitions/type:** No top-level functions/classes.

## `work/fix_registry.py`

Local source: `/Users/joshua/Documents/Codex/2026-09-29/can-x20-2/work/fix_registry.py` (source files are not included in this documentation push).

Python module; see defined symbols and source.

**Top-level definitions/type:** No top-level functions/classes.

## `work/probe_conclusions.py`

Local source: `/Users/joshua/Documents/Codex/2026-09-29/can-x20-2/work/probe_conclusions.py` (source files are not included in this documentation push).

Python module; see defined symbols and source.

**Top-level definitions/type:** No top-level functions/classes.

## `work/probe_live_pubmed.py`

Local source: `/Users/joshua/Documents/Codex/2026-09-29/can-x20-2/work/probe_live_pubmed.py` (source files are not included in this documentation push).

Python module; see defined symbols and source.

**Top-level definitions/type:** No top-level functions/classes.

## `work/probe_passages.py`

Local source: `/Users/joshua/Documents/Codex/2026-09-29/can-x20-2/work/probe_passages.py` (source files are not included in this documentation push).

Python module; see defined symbols and source.

**Top-level definitions/type:** No top-level functions/classes.

## `work/probe_verifier_evidence.py`

Local source: `/Users/joshua/Documents/Codex/2026-09-29/can-x20-2/work/probe_verifier_evidence.py` (source files are not included in this documentation push).

Python module; see defined symbols and source.

**Top-level definitions/type:** No top-level functions/classes.

## `work/refine_evaluation.py`

Local source: `/Users/joshua/Documents/Codex/2026-09-29/can-x20-2/work/refine_evaluation.py` (source files are not included in this documentation push).

Python module; see defined symbols and source.

**Top-level definitions/type:** No top-level functions/classes.

## `work/replay_reranking.py`

Local source: `/Users/joshua/Documents/Codex/2026-09-29/can-x20-2/work/replay_reranking.py` (source files are not included in this documentation push).

Python module; see defined symbols and source.

**Top-level definitions/type:** No top-level functions/classes.

## `work/run_e2e_cases.py`

Local source: `/Users/joshua/Documents/Codex/2026-09-29/can-x20-2/work/run_e2e_cases.py` (source files are not included in this documentation push).

Python module; see defined symbols and source.

**Top-level definitions/type:** No top-level functions/classes.

## `work/update_evidence_ui.py`

Local source: `/Users/joshua/Documents/Codex/2026-09-29/can-x20-2/work/update_evidence_ui.py` (source files are not included in this documentation push).

Python module; see defined symbols and source.

**Top-level definitions/type:** No top-level functions/classes.

## `work/use_conclusion_passage.py`

Local source: `/Users/joshua/Documents/Codex/2026-09-29/can-x20-2/work/use_conclusion_passage.py` (source files are not included in this documentation push).

Python module; see defined symbols and source.

**Top-level definitions/type:** No top-level functions/classes.

## `work/verify_passage_fix.py`

Local source: `/Users/joshua/Documents/Codex/2026-09-29/can-x20-2/work/verify_passage_fix.py` (source files are not included in this documentation push).

Python module; see defined symbols and source.

**Top-level definitions/type:** No top-level functions/classes.

## `work/wire_nli.py`

Local source: `/Users/joshua/Documents/Codex/2026-09-29/can-x20-2/work/wire_nli.py` (source files are not included in this documentation push).

Python module; see defined symbols and source.

**Top-level definitions/type:** No top-level functions/classes.

## `work/advanced-runtime/backend/__init__.py`

Local source: `/Users/joshua/Documents/Codex/2026-09-29/can-x20-2/work/advanced-runtime/backend/__init__.py` (source files are not included in this documentation push).

Python module; see defined symbols and source.

**Top-level definitions/type:** No top-level functions/classes.

## `work/advanced-runtime/backend/pipeline.py`

Local source: `/Users/joshua/Documents/Codex/2026-09-29/can-x20-2/work/advanced-runtime/backend/pipeline.py` (source files are not included in this documentation push).

Python module; see defined symbols and source.

**Top-level definitions/type:** `_utc_now`, `_enum_value`, `_assert_success`, `_collect_models`, `BiomedicalVerificationPipeline`

## `work/advanced-runtime/backend/pipeline_config.py`

Local source: `/Users/joshua/Documents/Codex/2026-09-29/can-x20-2/work/advanced-runtime/backend/pipeline_config.py` (source files are not included in this documentation push).

Python module; see defined symbols and source.

**Top-level definitions/type:** `_env_path`, `_env_int`, `_env_float`, `Phase1Config`, `Phase2Config`, `Phase3Config`, `Phase4Config`, `Phase5Config`, `RuntimeConfig`, `PipelineConfig`, `load_pipeline_config`, `ensure_runtime_directories`, `validate_static_paths`

## `work/advanced-runtime/backend/schemas.py`

Local source: `/Users/joshua/Documents/Codex/2026-09-29/can-x20-2/work/advanced-runtime/backend/schemas.py` (source files are not included in this documentation push).

Python module; see defined symbols and source.

**Top-level definitions/type:** `Verdict`, `UserFacingVerdict`, `PhaseName`, `PhaseStatus`, `ExplanationStatus`, `AuthorityTier`, `Modality`, `BaseSchema`, `InferenceRequest`, `PhaseError`, `PhaseTiming`, `ModelArtifact`, `Phase1Result`, `EvidenceLineage`, `EvidenceRecord`, `RetrievalTrace`, `Phase2Result`, `Phase3Result`, `ClassProbabilities`, `PairwiseVerification`, `Phase4Result`, `GroundingMetrics`, `Phase5Result`, `PipelineProvenance`, `DecisionPackage`, `verdict_to_user_facing`

## `work/advanced-runtime/backend/adapters/__init__.py`

Local source: `/Users/joshua/Documents/Codex/2026-09-29/can-x20-2/work/advanced-runtime/backend/adapters/__init__.py` (source files are not included in this documentation push).

Python module; see defined symbols and source.

**Top-level definitions/type:** No top-level functions/classes.

## `work/advanced-runtime/backend/adapters/biomedical_nli_adapter.py`

Local source: `/Users/joshua/Documents/Codex/2026-09-29/can-x20-2/work/advanced-runtime/backend/adapters/biomedical_nli_adapter.py` (source files are not included in this documentation push).

Biomedical NLI verifier with explicit label mapping and relevance discounting. This is a separate deployment mode, not the historical Phase 4 checkpoint. Scores are uncalibrated model outputs. The original adapter remain

**Top-level definitions/type:** `relevance_discount`, `evidence_passage`, `BiomedicalNliAdapter`

## `work/advanced-runtime/backend/adapters/phase1_adapter.py`

Local source: `/Users/joshua/Documents/Codex/2026-09-29/can-x20-2/work/advanced-runtime/backend/adapters/phase1_adapter.py` (source files are not included in this documentation push).

Python module; see defined symbols and source.

**Top-level definitions/type:** `Phase1AdapterError`, `_load_module_from_path`, `_choose_device`, `_file_sha256`, `Phase1Adapter`

## `work/advanced-runtime/backend/adapters/phase2_adapter.py`

Local source: `/Users/joshua/Documents/Codex/2026-09-29/can-x20-2/work/advanced-runtime/backend/adapters/phase2_adapter.py` (source files are not included in this documentation push).

Python module; see defined symbols and source.

**Top-level definitions/type:** `_utc_now`, `_iso_utc`, `_sigmoid`, `Phase2ImportBundle`, `_prepare_phase2_modules`, `_restore_phase2_modules`, `Phase2Adapter`

## `work/advanced-runtime/backend/adapters/phase3_adapter.py`

Local source: `/Users/joshua/Documents/Codex/2026-09-29/can-x20-2/work/advanced-runtime/backend/adapters/phase3_adapter.py` (source files are not included in this documentation push).

Python module; see defined symbols and source.

**Top-level definitions/type:** `_utc_now`, `_iso_utc`, `_load_module_from_file`, `Phase3Adapter`

## `work/advanced-runtime/backend/adapters/phase4_adapter.py`

Local source: `/Users/joshua/Documents/Codex/2026-09-29/can-x20-2/work/advanced-runtime/backend/adapters/phase4_adapter.py` (source files are not included in this documentation push).

Python module; see defined symbols and source.

**Top-level definitions/type:** `Phase4AdapterError`, `PubMedBERTVerifier`, `utc_now_string`, `sha256_file`, `choose_device`, `Phase4Adapter`

## `work/advanced-runtime/backend/adapters/phase5_adapter.py`

Local source: `/Users/joshua/Documents/Codex/2026-09-29/can-x20-2/work/advanced-runtime/backend/adapters/phase5_adapter.py` (source files are not included in this documentation push).

Python module; see defined symbols and source.

**Top-level definitions/type:** `_utc_now`, `_sha256_file`, `_enum_value`, `_get_phase5_root`, `_load_phase5_config`, `_prepare_phase5_imports`, `_make_phase5_evidence`, `_extract_grounding_metrics`, `_model_artifact`, `Phase5Adapter`, `run_phase5`

## `work/advanced-runtime/backend/api/__init__.py`

Local source: `/Users/joshua/Documents/Codex/2026-09-29/can-x20-2/work/advanced-runtime/backend/api/__init__.py` (source files are not included in this documentation push).

Python module; see defined symbols and source.

**Top-level definitions/type:** No top-level functions/classes.

## `work/advanced-runtime/backend/api/app.py`

Local source: `/Users/joshua/Documents/Codex/2026-09-29/can-x20-2/work/advanced-runtime/backend/api/app.py` (source files are not included in this documentation push).

Python module; see defined symbols and source.

**Top-level definitions/type:** `lifespan`, `root`

## `work/advanced-runtime/backend/api/dependencies.py`

Local source: `/Users/joshua/Documents/Codex/2026-09-29/can-x20-2/work/advanced-runtime/backend/api/dependencies.py` (source files are not included in this documentation push).

Python module; see defined symbols and source.

**Top-level definitions/type:** `initialize_pipeline`, `get_pipeline`, `shutdown_pipeline`, `get_inference_lock`

## `work/advanced-runtime/backend/api/routes/__init__.py`

Local source: `/Users/joshua/Documents/Codex/2026-09-29/can-x20-2/work/advanced-runtime/backend/api/routes/__init__.py` (source files are not included in this documentation push).

Python module; see defined symbols and source.

**Top-level definitions/type:** No top-level functions/classes.

## `work/advanced-runtime/backend/api/routes/inference.py`

Local source: `/Users/joshua/Documents/Codex/2026-09-29/can-x20-2/work/advanced-runtime/backend/api/routes/inference.py` (source files are not included in this documentation push).

Python module; see defined symbols and source.

**Top-level definitions/type:** `_safe_request_id`, `_save_uploaded_image`, `_load_json_file`, `create_inference`, `get_inference`, `get_audit`

## `work/advanced-runtime/backend/api/routes/system.py`

Local source: `/Users/joshua/Documents/Codex/2026-09-29/can-x20-2/work/advanced-runtime/backend/api/routes/system.py` (source files are not included in this documentation push).

Python module; see defined symbols and source.

**Top-level definitions/type:** `_utc_now_iso`, `health`, `models`

## `work/advanced-runtime/backend/services/__init__.py`

Local source: `/Users/joshua/Documents/Codex/2026-09-29/can-x20-2/work/advanced-runtime/backend/services/__init__.py` (source files are not included in this documentation push).

Python module; see defined symbols and source.

**Top-level definitions/type:** No top-level functions/classes.

## `work/advanced-runtime/backend/services/persistence.py`

Local source: `/Users/joshua/Documents/Codex/2026-09-29/can-x20-2/work/advanced-runtime/backend/services/persistence.py` (source files are not included in this documentation push).

Python module; see defined symbols and source.

**Top-level definitions/type:** `PersistenceError`, `DuplicateRequestError`, `AuditPhaseRecord`, `AuditRecord`, `PersistenceResult`, `_enum_value`, `_sha256_bytes`, `_sha256_text`, `_safe_request_id`, `_canonical_json_bytes`, `_fsync_directory`, `_atomic_write_new`, `_phase_record`, `_extract_checkpoint_sha256`, `_model_artifact_summary`, `_build_invariant_checks`, `DecisionPackagePersistence`

## `work/advanced-runtime/backend/services/pubmed_search.py`

Local source: `/Users/joshua/Documents/Codex/2026-09-29/can-x20-2/work/advanced-runtime/backend/services/pubmed_search.py` (source files are not included in this documentation push).

Bounded PubMed search with explicit provenance and an offline-safe cache. Search terms are transmitted to NCBI only when this client is enabled by the adapter. Never accepts arbitrary URLs. Never assigns a fact-checking 

**Top-level definitions/type:** `search_terms`, `parse_articles`, `PubMedSearch`

## `work/advanced-runtime/backend/utils/__init__.py`

Local source: `/Users/joshua/Documents/Codex/2026-09-29/can-x20-2/work/advanced-runtime/backend/utils/__init__.py` (source files are not included in this documentation push).

Python module; see defined symbols and source.

**Top-level definitions/type:** No top-level functions/classes.

## `work/blue-v1-backup/app.js`

Local source: `/Users/joshua/Documents/Codex/2026-09-29/can-x20-2/work/blue-v1-backup/app.js` (source files are not included in this documentation push).

Frontend/source asset; follow the source link for implementation.

**Top-level definitions/type:** js

## `work/blue-v1-backup/index.html`

Local source: `/Users/joshua/Documents/Codex/2026-09-29/can-x20-2/work/blue-v1-backup/index.html` (source files are not included in this documentation push).

Frontend/source asset; follow the source link for implementation.

**Top-level definitions/type:** html

## `work/blue-v1-backup/styles.css`

Local source: `/Users/joshua/Documents/Codex/2026-09-29/can-x20-2/work/blue-v1-backup/styles.css` (source files are not included in this documentation push).

Frontend/source asset; follow the source link for implementation.

**Top-level definitions/type:** css
