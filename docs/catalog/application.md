# application: source file catalog

Source root: `/Users/joshua/Downloads/BiomedicalVerifier`

Generated from local files. Inclusion does not imply a file is active, tested, or production-ready. Backups and historical experiments are included when present. Descriptions are module docstrings or structural summaries, not an audit of correctness.

## `backend/__init__.py`

Local source: `/Users/joshua/Downloads/BiomedicalVerifier/backend/__init__.py` (source files are not included in this documentation push).

Python module; see defined symbols and source.

**Top-level definitions/type:** No top-level functions/classes.

## `backend/pipeline.py`

Local source: `/Users/joshua/Downloads/BiomedicalVerifier/backend/pipeline.py` (source files are not included in this documentation push).

Python module; see defined symbols and source.

**Top-level definitions/type:** `_utc_now`, `_enum_value`, `_assert_success`, `_collect_models`, `BiomedicalVerificationPipeline`

## `backend/pipeline_config.py`

Local source: `/Users/joshua/Downloads/BiomedicalVerifier/backend/pipeline_config.py` (source files are not included in this documentation push).

Python module; see defined symbols and source.

**Top-level definitions/type:** `_env_path`, `_env_int`, `_env_float`, `Phase1Config`, `Phase2Config`, `Phase3Config`, `Phase4Config`, `Phase5Config`, `RuntimeConfig`, `PipelineConfig`, `load_pipeline_config`, `ensure_runtime_directories`, `validate_static_paths`

## `backend/schemas.py`

Local source: `/Users/joshua/Downloads/BiomedicalVerifier/backend/schemas.py` (source files are not included in this documentation push).

Python module; see defined symbols and source.

**Top-level definitions/type:** `Verdict`, `UserFacingVerdict`, `PhaseName`, `PhaseStatus`, `ExplanationStatus`, `AuthorityTier`, `Modality`, `BaseSchema`, `InferenceRequest`, `PhaseError`, `PhaseTiming`, `ModelArtifact`, `Phase1Result`, `EvidenceLineage`, `EvidenceRecord`, `RetrievalTrace`, `Phase2Result`, `Phase3Result`, `ClassProbabilities`, `PairwiseVerification`, `Phase4Result`, `GroundingMetrics`, `Phase5Result`, `PipelineProvenance`, `DecisionPackage`, `verdict_to_user_facing`

## `backend/adapters/__init__.py`

Local source: `/Users/joshua/Downloads/BiomedicalVerifier/backend/adapters/__init__.py` (source files are not included in this documentation push).

Python module; see defined symbols and source.

**Top-level definitions/type:** No top-level functions/classes.

## `backend/adapters/biomedical_nli_adapter.py`

Local source: `/Users/joshua/Downloads/BiomedicalVerifier/backend/adapters/biomedical_nli_adapter.py` (source files are not included in this documentation push).

Biomedical NLI verifier with explicit label mapping and relevance discounting. This is a separate deployment mode, not the historical Phase 4 checkpoint. Scores are uncalibrated model outputs. The original adapter remain

**Top-level definitions/type:** `relevance_discount`, `evidence_passage`, `BiomedicalNliAdapter`

## `backend/adapters/phase1_adapter.py`

Local source: `/Users/joshua/Downloads/BiomedicalVerifier/backend/adapters/phase1_adapter.py` (source files are not included in this documentation push).

Python module; see defined symbols and source.

**Top-level definitions/type:** `Phase1AdapterError`, `_load_module_from_path`, `_choose_device`, `_file_sha256`, `Phase1Adapter`

## `backend/adapters/phase2_adapter.py`

Local source: `/Users/joshua/Downloads/BiomedicalVerifier/backend/adapters/phase2_adapter.py` (source files are not included in this documentation push).

Python module; see defined symbols and source.

**Top-level definitions/type:** `_utc_now`, `_iso_utc`, `_sigmoid`, `Phase2ImportBundle`, `_prepare_phase2_modules`, `_restore_phase2_modules`, `Phase2Adapter`

## `backend/adapters/phase3_adapter.py`

Local source: `/Users/joshua/Downloads/BiomedicalVerifier/backend/adapters/phase3_adapter.py` (source files are not included in this documentation push).

Python module; see defined symbols and source.

**Top-level definitions/type:** `_utc_now`, `_iso_utc`, `_load_module_from_file`, `Phase3Adapter`

## `backend/adapters/phase4_adapter.py`

Local source: `/Users/joshua/Downloads/BiomedicalVerifier/backend/adapters/phase4_adapter.py` (source files are not included in this documentation push).

Python module; see defined symbols and source.

**Top-level definitions/type:** `Phase4AdapterError`, `PubMedBERTVerifier`, `utc_now_string`, `sha256_file`, `choose_device`, `Phase4Adapter`

## `backend/adapters/phase5_adapter.py`

Local source: `/Users/joshua/Downloads/BiomedicalVerifier/backend/adapters/phase5_adapter.py` (source files are not included in this documentation push).

Python module; see defined symbols and source.

**Top-level definitions/type:** `_utc_now`, `_sha256_file`, `_enum_value`, `_get_phase5_root`, `_load_phase5_config`, `_prepare_phase5_imports`, `_make_phase5_evidence`, `_extract_grounding_metrics`, `_model_artifact`, `Phase5Adapter`, `run_phase5`

## `backend/api/__init__.py`

Local source: `/Users/joshua/Downloads/BiomedicalVerifier/backend/api/__init__.py` (source files are not included in this documentation push).

Python module; see defined symbols and source.

**Top-level definitions/type:** No top-level functions/classes.

## `backend/api/app.py`

Local source: `/Users/joshua/Downloads/BiomedicalVerifier/backend/api/app.py` (source files are not included in this documentation push).

Python module; see defined symbols and source.

**Top-level definitions/type:** `lifespan`, `root`

## `backend/api/dependencies.py`

Local source: `/Users/joshua/Downloads/BiomedicalVerifier/backend/api/dependencies.py` (source files are not included in this documentation push).

Python module; see defined symbols and source.

**Top-level definitions/type:** `initialize_pipeline`, `get_pipeline`, `shutdown_pipeline`, `get_inference_lock`

## `backend/api/routes/__init__.py`

Local source: `/Users/joshua/Downloads/BiomedicalVerifier/backend/api/routes/__init__.py` (source files are not included in this documentation push).

Python module; see defined symbols and source.

**Top-level definitions/type:** No top-level functions/classes.

## `backend/api/routes/inference.py`

Local source: `/Users/joshua/Downloads/BiomedicalVerifier/backend/api/routes/inference.py` (source files are not included in this documentation push).

Python module; see defined symbols and source.

**Top-level definitions/type:** `_safe_request_id`, `_save_uploaded_image`, `_load_json_file`, `create_inference`, `get_inference`, `get_audit`

## `backend/api/routes/system.py`

Local source: `/Users/joshua/Downloads/BiomedicalVerifier/backend/api/routes/system.py` (source files are not included in this documentation push).

Python module; see defined symbols and source.

**Top-level definitions/type:** `_utc_now_iso`, `health`, `models`

## `backend/services/__init__.py`

Local source: `/Users/joshua/Downloads/BiomedicalVerifier/backend/services/__init__.py` (source files are not included in this documentation push).

Python module; see defined symbols and source.

**Top-level definitions/type:** No top-level functions/classes.

## `backend/services/persistence.py`

Local source: `/Users/joshua/Downloads/BiomedicalVerifier/backend/services/persistence.py` (source files are not included in this documentation push).

Python module; see defined symbols and source.

**Top-level definitions/type:** `PersistenceError`, `DuplicateRequestError`, `AuditPhaseRecord`, `AuditRecord`, `PersistenceResult`, `_enum_value`, `_sha256_bytes`, `_sha256_text`, `_safe_request_id`, `_canonical_json_bytes`, `_fsync_directory`, `_atomic_write_new`, `_phase_record`, `_extract_checkpoint_sha256`, `_model_artifact_summary`, `_build_invariant_checks`, `DecisionPackagePersistence`

## `backend/services/pubmed_search.py`

Local source: `/Users/joshua/Downloads/BiomedicalVerifier/backend/services/pubmed_search.py` (source files are not included in this documentation push).

Bounded PubMed search with explicit provenance and an offline-safe cache. Search terms are transmitted to NCBI only when this client is enabled by the adapter. Never accepts arbitrary URLs. Never assigns a fact-checking 

**Top-level definitions/type:** `search_terms`, `parse_articles`, `PubMedSearch`

## `backend/utils/__init__.py`

Local source: `/Users/joshua/Downloads/BiomedicalVerifier/backend/utils/__init__.py` (source files are not included in this documentation push).

Python module; see defined symbols and source.

**Top-level definitions/type:** No top-level functions/classes.

## `diagnostics/api_contract_test.py`

Local source: `/Users/joshua/Downloads/BiomedicalVerifier/diagnostics/api_contract_test.py` (source files are not included in this documentation push).

Python module; see defined symbols and source.

**Top-level definitions/type:** `find_evidence`

## `diagnostics/compare_phase4_checkpoints_semantics.py`

Local source: `/Users/joshua/Downloads/BiomedicalVerifier/diagnostics/compare_phase4_checkpoints_semantics.py` (source files are not included in this documentation push).

Python module; see defined symbols and source.

**Top-level definitions/type:** `device`, `discover_checkpoints`, `load_checkpoint`, `get_tokenizer`, `score`

## `diagnostics/deep_pipeline_audit.py`

Local source: `/Users/joshua/Downloads/BiomedicalVerifier/diagnostics/deep_pipeline_audit.py` (source files are not included in this documentation push).

Python module; see defined symbols and source.

**Top-level definitions/type:** `banner`, `section`, `get_nested`, `pct`, `rank`, `shorten`, `find_evidence_lists`

## `diagnostics/phase4_fixed_evidence_probe.py`

Local source: `/Users/joshua/Downloads/BiomedicalVerifier/diagnostics/phase4_fixed_evidence_probe.py` (source files are not included in this documentation push).

Python module; see defined symbols and source.

**Top-level definitions/type:** `get_device`, `find_checkpoint`, `score_pair`, `show_delta`

## `diagnostics/phase4_semantic_probe.py`

Local source: `/Users/joshua/Downloads/BiomedicalVerifier/diagnostics/phase4_semantic_probe.py` (source files are not included in this documentation push).

Python module; see defined symbols and source.

**Top-level definitions/type:** `create_inference`, `fmt_prob`

## `frontend/eslint.config.mjs`

Local source: `/Users/joshua/Downloads/BiomedicalVerifier/frontend/eslint.config.mjs` (source files are not included in this documentation push).

Frontend/source asset; follow the source link for implementation.

**Top-level definitions/type:** mjs

## `frontend/next-env.d.ts`

Local source: `/Users/joshua/Downloads/BiomedicalVerifier/frontend/next-env.d.ts` (source files are not included in this documentation push).

Frontend/source asset; follow the source link for implementation.

**Top-level definitions/type:** ts

## `frontend/next.config.ts`

Local source: `/Users/joshua/Downloads/BiomedicalVerifier/frontend/next.config.ts` (source files are not included in this documentation push).

Frontend/source asset; follow the source link for implementation.

**Top-level definitions/type:** ts

## `frontend/postcss.config.mjs`

Local source: `/Users/joshua/Downloads/BiomedicalVerifier/frontend/postcss.config.mjs` (source files are not included in this documentation push).

Frontend/source asset; follow the source link for implementation.

**Top-level definitions/type:** mjs

## `frontend/src/app/globals.css`

Local source: `/Users/joshua/Downloads/BiomedicalVerifier/frontend/src/app/globals.css` (source files are not included in this documentation push).

Frontend/source asset; follow the source link for implementation.

**Top-level definitions/type:** css

## `frontend/src/app/layout.tsx`

Local source: `/Users/joshua/Downloads/BiomedicalVerifier/frontend/src/app/layout.tsx` (source files are not included in this documentation push).

Frontend/source asset; follow the source link for implementation.

**Top-level definitions/type:** tsx

## `frontend/src/app/page.tsx`

Local source: `/Users/joshua/Downloads/BiomedicalVerifier/frontend/src/app/page.tsx` (source files are not included in this documentation push).

Frontend/source asset; follow the source link for implementation.

**Top-level definitions/type:** tsx

## `frontend/src/components/EvidenceCard.tsx`

Local source: `/Users/joshua/Downloads/BiomedicalVerifier/frontend/src/components/EvidenceCard.tsx` (source files are not included in this documentation push).

Frontend/source asset; follow the source link for implementation.

**Top-level definitions/type:** tsx

## `frontend/src/components/PipelineTrace.tsx`

Local source: `/Users/joshua/Downloads/BiomedicalVerifier/frontend/src/components/PipelineTrace.tsx` (source files are not included in this documentation push).

Frontend/source asset; follow the source link for implementation.

**Top-level definitions/type:** tsx

## `frontend/src/components/ProbabilityPanel.tsx`

Local source: `/Users/joshua/Downloads/BiomedicalVerifier/frontend/src/components/ProbabilityPanel.tsx` (source files are not included in this documentation push).

Frontend/source asset; follow the source link for implementation.

**Top-level definitions/type:** tsx

## `frontend/src/components/ResultAccordion.tsx`

Local source: `/Users/joshua/Downloads/BiomedicalVerifier/frontend/src/components/ResultAccordion.tsx` (source files are not included in this documentation push).

Frontend/source asset; follow the source link for implementation.

**Top-level definitions/type:** tsx

## `frontend/src/components/VerificationPanel.tsx`

Local source: `/Users/joshua/Downloads/BiomedicalVerifier/frontend/src/components/VerificationPanel.tsx` (source files are not included in this documentation push).

Frontend/source asset; follow the source link for implementation.

**Top-level definitions/type:** tsx

## `frontend/src/lib/api.ts`

Local source: `/Users/joshua/Downloads/BiomedicalVerifier/frontend/src/lib/api.ts` (source files are not included in this documentation push).

Frontend/source asset; follow the source link for implementation.

**Top-level definitions/type:** ts

## `frontend/src/lib/format.ts`

Local source: `/Users/joshua/Downloads/BiomedicalVerifier/frontend/src/lib/format.ts` (source files are not included in this documentation push).

Frontend/source asset; follow the source link for implementation.

**Top-level definitions/type:** ts

## `frontend/src/lib/types.ts`

Local source: `/Users/joshua/Downloads/BiomedicalVerifier/frontend/src/lib/types.ts` (source files are not included in this documentation push).

Frontend/source asset; follow the source link for implementation.

**Top-level definitions/type:** ts

## `tests/__init__.py`

Local source: `/Users/joshua/Downloads/BiomedicalVerifier/tests/__init__.py` (source files are not included in this documentation push).

Python module; see defined symbols and source.

**Top-level definitions/type:** No top-level functions/classes.

## `tests/test_persistence.py`

Local source: `/Users/joshua/Downloads/BiomedicalVerifier/tests/test_persistence.py` (source files are not included in this documentation push).

Python module; see defined symbols and source.

**Top-level definitions/type:** `main`

## `tests/test_phase1_adapter.py`

Local source: `/Users/joshua/Downloads/BiomedicalVerifier/tests/test_phase1_adapter.py` (source files are not included in this documentation push).

Python module; see defined symbols and source.

**Top-level definitions/type:** `main`

## `tests/test_phase2_adapter.py`

Local source: `/Users/joshua/Downloads/BiomedicalVerifier/tests/test_phase2_adapter.py` (source files are not included in this documentation push).

Python module; see defined symbols and source.

**Top-level definitions/type:** `main`

## `tests/test_phase3_adapter.py`

Local source: `/Users/joshua/Downloads/BiomedicalVerifier/tests/test_phase3_adapter.py` (source files are not included in this documentation push).

Python module; see defined symbols and source.

**Top-level definitions/type:** `main`

## `tests/test_phase4_adapter.py`

Local source: `/Users/joshua/Downloads/BiomedicalVerifier/tests/test_phase4_adapter.py` (source files are not included in this documentation push).

Python module; see defined symbols and source.

**Top-level definitions/type:** `assert_close`, `main`

## `tests/test_phase5_adapter.py`

Local source: `/Users/joshua/Downloads/BiomedicalVerifier/tests/test_phase5_adapter.py` (source files are not included in this documentation push).

Python module; see defined symbols and source.

**Top-level definitions/type:** `enum_value`, `main`

## `tests/test_pipeline.py`

Local source: `/Users/joshua/Downloads/BiomedicalVerifier/tests/test_pipeline.py` (source files are not included in this documentation push).

Python module; see defined symbols and source.

**Top-level definitions/type:** `enum_value`, `main`

## `tests/test_schemas.py`

Local source: `/Users/joshua/Downloads/BiomedicalVerifier/tests/test_schemas.py` (source files are not included in this documentation push).

Python module; see defined symbols and source.

**Top-level definitions/type:** `main`

## `tools/convert_phase1_checkpoint.py`

Local source: `/Users/joshua/Downloads/BiomedicalVerifier/tools/convert_phase1_checkpoint.py` (source files are not included in this documentation push).

Python module; see defined symbols and source.

**Top-level definitions/type:** `load_module_from_path`, `map_vit_key`, `main`

## `ui_backup_hci_20260928_123436/globals.css`

Local source: `/Users/joshua/Downloads/BiomedicalVerifier/ui_backup_hci_20260928_123436/globals.css` (source files are not included in this documentation push).

Frontend/source asset; follow the source link for implementation.

**Top-level definitions/type:** css

## `ui_backup_hci_20260928_123436/page.tsx`

Local source: `/Users/joshua/Downloads/BiomedicalVerifier/ui_backup_hci_20260928_123436/page.tsx` (source files are not included in this documentation push).

Frontend/source asset; follow the source link for implementation.

**Top-level definitions/type:** tsx

## `ui_backup_pre_hci/EvidenceCard.tsx`

Local source: `/Users/joshua/Downloads/BiomedicalVerifier/ui_backup_pre_hci/EvidenceCard.tsx` (source files are not included in this documentation push).

Frontend/source asset; follow the source link for implementation.

**Top-level definitions/type:** tsx

## `ui_backup_pre_hci/PipelineTrace.tsx`

Local source: `/Users/joshua/Downloads/BiomedicalVerifier/ui_backup_pre_hci/PipelineTrace.tsx` (source files are not included in this documentation push).

Frontend/source asset; follow the source link for implementation.

**Top-level definitions/type:** tsx

## `ui_backup_pre_hci/ProbabilityPanel.tsx`

Local source: `/Users/joshua/Downloads/BiomedicalVerifier/ui_backup_pre_hci/ProbabilityPanel.tsx` (source files are not included in this documentation push).

Frontend/source asset; follow the source link for implementation.

**Top-level definitions/type:** tsx

## `ui_backup_pre_hci/VerificationPanel.tsx`

Local source: `/Users/joshua/Downloads/BiomedicalVerifier/ui_backup_pre_hci/VerificationPanel.tsx` (source files are not included in this documentation push).

Frontend/source asset; follow the source link for implementation.

**Top-level definitions/type:** tsx

## `ui_backup_pre_hci/globals.css`

Local source: `/Users/joshua/Downloads/BiomedicalVerifier/ui_backup_pre_hci/globals.css` (source files are not included in this documentation push).

Frontend/source asset; follow the source link for implementation.

**Top-level definitions/type:** css

## `ui_backup_pre_hci/page.tsx`

Local source: `/Users/joshua/Downloads/BiomedicalVerifier/ui_backup_pre_hci/page.tsx` (source files are not included in this documentation push).

Frontend/source asset; follow the source link for implementation.

**Top-level definitions/type:** tsx
