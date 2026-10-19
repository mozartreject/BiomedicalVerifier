# phase-2: source file catalog

Source root: `/Users/joshua/Downloads/phase2`

Generated from local files. Inclusion does not imply a file is active, tested, or production-ready. Backups and historical experiments are included when present. Descriptions are module docstrings or structural summaries, not an audit of correctness.

## `analyze_current_classification.py`

Local source: `/Users/joshua/Downloads/phase2/analyze_current_classification.py` (source files are not included in this documentation push).

Python module; see defined symbols and source.

**Top-level definitions/type:** `normalize_prediction_label`, `load_scifact_ground_truth`, `load_predictions`, `load_retrieved_evidence`, `get_retrieved_documents`, `get_gold_rank`, `main`

## `analyze_failure_map.py`

Local source: `/Users/joshua/Downloads/phase2/analyze_failure_map.py` (source files are not included in this documentation push).

Python module; see defined symbols and source.

**Top-level definitions/type:** `load`

## `audit_30k_corpus.py`

Local source: `/Users/joshua/Downloads/phase2/audit_30k_corpus.py` (source files are not included in this documentation push).

Python module; see defined symbols and source.

**Top-level definitions/type:** `load_jsonl`, `norm_id`, `extract_gold_doc_ids`, `inspect_metadata`, `metadata_ids`, `corpus_ids`, `report`, `claim_hit_rate`

## `audit_35k_dense_displacement.py`

Local source: `/Users/joshua/Downloads/phase2/audit_35k_dense_displacement.py` (source files are not included in this documentation push).

Python module; see defined symbols and source.

**Top-level definitions/type:** `load_jsonl`, `normalize_id`, `extract_gold_docs`, `first_gold_rank`, `first_gold_position`, `short`

## `audit_gold_and_metadata.py`

Local source: `/Users/joshua/Downloads/phase2/audit_gold_and_metadata.py` (source files are not included in this documentation push).

Python module; see defined symbols and source.

**Top-level definitions/type:** `load_jsonl`, `load_json`, `load_meta_ids`

## `build_35k_index.py`

Local source: `/Users/joshua/Downloads/phase2/build_35k_index.py` (source files are not included in this documentation push).

Python module; see defined symbols and source.

**Top-level definitions/type:** `load_jsonl`, `clean_space`, `build_scifact_record`, `build_pubmed_record`

## `build_faiss_index.py`

Local source: `/Users/joshua/Downloads/phase2/build_faiss_index.py` (source files are not included in this documentation push).

Build FAISS index from abstracts. Uses BioBERT with mean pooling + L2 normalization for cosine similarity.

**Top-level definitions/type:** `BioBERTEncoder`, `build_faiss_index`, `load_faiss_index`

## `classification_error_analysis.py`

Local source: `/Users/joshua/Downloads/phase2/classification_error_analysis.py` (source files are not included in this documentation push).

Python module; see defined symbols and source.

**Top-level definitions/type:** `load_ground_truth`, `main`

## `classify_claims.py`

Local source: `/Users/joshua/Downloads/phase2/classify_claims.py` (source files are not included in this documentation push).

Python module; see defined symbols and source.

**Top-level definitions/type:** `load_input`, `load_checkpoint`, `save_json`, `check_ollama`, `prepare_evidence`, `normalize_text`, `claim_fingerprint`, `detect_relationship_anchors`, `build_system_prompt`, `build_prompt`, `extract_json`, `normalize_label`, `normalize_result`, `current_claim_sanity_check`, `validate_result`, `apply_explicit_relationship_guard`, `classify_with_qwen`, `main`

## `classify_claims_backup.py`

Local source: `/Users/joshua/Downloads/phase2/classify_claims_backup.py` (source files are not included in this documentation push).

Python module; see defined symbols and source.

**Top-level definitions/type:** `load_input`, `load_checkpoint`, `save_json`, `check_ollama`, `prepare_evidence`, `build_prompt`, `extract_json`, `normalize_label`, `normalize_result`, `validate_result`, `classify_with_qwen`, `main`

## `classify_claims_v6.py`

Local source: `/Users/joshua/Downloads/phase2/classify_claims_v6.py` (source files are not included in this documentation push).

============================================================ PHASE 2 — V6 CLAIM CLASSIFIER ============================================================ Controlled experiment against V5. V6 changes: 1. Strict evidence adm

**Top-level definitions/type:** `load_json`, `save_json`, `claim_fingerprint`, `load_phase2_evidence`, `load_error_claim_ids`, `prepare_evidence`, `detect_relationship_anchors`, `build_prompt`, `extract_json`, `normalize_result`, `current_claim_sanity_check`, `call_ollama`, `classify_with_qwen`, `save_checkpoint`, `load_checkpoint`, `save_final_output`, `compare_v5_v6`, `main`

## `classify_claims_v7.py`

Local source: `/Users/joshua/Downloads/phase2/classify_claims_v7.py` (source files are not included in this documentation push).

====================================================================== PHASE 2 — V7 CLAIM CLASSIFIER ====================================================================== Controlled scientific fact-verification experime

**Top-level definitions/type:** `load_json`, `save_json`, `claim_fingerprint`, `load_phase2_evidence`, `load_error_claim_ids`, `prepare_evidence`, `detect_relationship_anchors`, `build_prompt`, `extract_json`, `normalize_result`, `current_claim_sanity_check`, `call_ollama`, `classify_with_qwen`, `save_checkpoint`, `load_checkpoint`, `save_final_output`, `compare_v5_v7`, `print_comparison`, `main`

## `classify_claims_v7_backup.py`

Local source: `/Users/joshua/Downloads/phase2/classify_claims_v7_backup.py` (source files are not included in this documentation push).

============================================================ PHASE 2 — V6 CLAIM CLASSIFIER ============================================================ Controlled experiment against V5. V6 changes: 1. Strict evidence adm

**Top-level definitions/type:** `load_json`, `save_json`, `claim_fingerprint`, `load_phase2_evidence`, `load_error_claim_ids`, `prepare_evidence`, `detect_relationship_anchors`, `build_prompt`, `extract_json`, `normalize_result`, `current_claim_sanity_check`, `call_ollama`, `classify_with_qwen`, `save_checkpoint`, `load_checkpoint`, `save_final_output`, `compare_v5_v6`, `main`

## `classify_claims_v7_broken.py`

Local source: `/Users/joshua/Downloads/phase2/classify_claims_v7_broken.py` (source files are not included in this documentation push).

============================================================ PHASE 2 — V6 CLAIM CLASSIFIER ============================================================ Controlled experiment against V5. V6 changes: 1. Strict evidence adm

**Top-level definitions/type:** `load_json`, `save_json`, `claim_fingerprint`, `load_phase2_evidence`, `load_error_claim_ids`, `prepare_evidence`, `detect_relationship_anchors`, `build_prompt`, `extract_json`, `normalize_result`, `current_claim_sanity_check`, `call_ollama`, `classify_with_qwen`, `save_checkpoint`, `load_checkpoint`, `save_final_output`, `compare_v5_v6`, `main`

## `classify_claims_v8.py`

Local source: `/Users/joshua/Downloads/phase2/classify_claims_v8.py` (source files are not included in this documentation push).

====================================================================== PHASE 2 — V8 SCIENTIFIC CLAIM CLASSIFIER ====================================================================== FINAL CONTROLLED CLASSIFIER Pipeline:

**Top-level definitions/type:** `load_json`, `save_json`, `load_ground_truth`, `load_v5_predictions`, `select_v5_errors`, `load_phase2_evidence`, `prepare_evidence`, `claim_fingerprint`, `relationship_guidance`, `build_prompt`, `extract_json`, `normalize_quote_text`, `quote_is_grounded`, `validate_quote`, `normalize_status`, `normalize_component`, `normalize_result`, `sanity_check`, `call_ollama`, `classify_with_qwen`, `load_checkpoint`, `save_checkpoint`, `save_final`, `compare_v5_v8`, `print_comparison`, `main`

## `classify_claims_v9.py`

Local source: `/Users/joshua/Downloads/phase2/classify_claims_v9.py` (source files are not included in this documentation push).

PHASE 2 V9.1 — STRICT SCIENTIFIC CLAIM CLASSIFIER Architecture: Phase 2 retrieved evidence ↓ Qwen 2.5 7B ↓ SUPPORTS / REFUTES / NEI ↓ Python validation ↓ Checkpointed output V9.1 FIXES ---------- 1. Structured Ollama JSO

**Top-level definitions/type:** `clean_text`, `normalize_label`, `normalize_confidence`, `token_set`, `contains_number`, `extract_numbers`, `prepare_evidence`, `build_user_prompt`, `extract_json`, `validate_prediction`, `evidence_usage_guard`, `anti_inference_guard`, `numerical_guard`, `directionality_guard`, `causality_guard`, `compound_claim_guard`, `evidence_quality_guard`, `check_ollama`, `call_qwen`, `classify_claim`, `load_phase2_output`, `load_checkpoint`, `save_checkpoint`, `save_failures`, `save_final_output`, `select_claims`, `main`

## `classify_claims_v92.py`

Local source: `/Users/joshua/Downloads/phase2/classify_claims_v92.py` (source files are not included in this documentation push).

Python module; see defined symbols and source.

**Top-level definitions/type:** `load_phase2_evidence`, `normalize_text`, `extract_numbers`, `claim_requires_numeric_evidence`, `numeric_guard`, `directionality_guard`, `negation_guard`, `compound_claim_guard`, `validate_evidence_ids`, `validate_result`, `build_prompt`, `call_ollama`, `extract_json`, `classify_claim`, `load_checkpoint`, `save_checkpoint`, `save_output`, `main`

## `classify_claims_v93.py`

Local source: `/Users/joshua/Downloads/phase2/classify_claims_v93.py` (source files are not included in this documentation push).

Python module; see defined symbols and source.

**Top-level definitions/type:** `load_phase2_evidence`, `normalize_text`, `extract_numbers`, `claim_requires_numeric_evidence`, `numeric_guard`, `directionality_guard`, `negation_guard`, `compound_claim_guard`, `validate_evidence_ids`, `validate_result`, `build_prompt`, `call_ollama`, `extract_json`, `classify_claim`, `load_checkpoint`, `save_checkpoint`, `save_output`, `main`

## `compare_5k_35k_retrieval.py`

Local source: `/Users/joshua/Downloads/phase2/compare_5k_35k_retrieval.py` (source files are not included in this documentation push).

Python module; see defined symbols and source.

**Top-level definitions/type:** `load_jsonl`, `normalize_id`, `tokenize`, `extract_gold_docs`, `hit_at_k`, `first_gold_rank`

## `config.py`

Local source: `/Users/joshua/Downloads/phase2/config.py` (source files are not included in this documentation push).

Phase 2 Configuration NO TRAINING. Just paths and constants.

**Top-level definitions/type:** No top-level functions/classes.

## `debug_qwen.py`

Local source: `/Users/joshua/Downloads/phase2/debug_qwen.py` (source files are not included in this documentation push).

Python module; see defined symbols and source.

**Top-level definitions/type:** No top-level functions/classes.

## `diagnose_candidate_corpus_mismatch.py`

Local source: `/Users/joshua/Downloads/phase2/diagnose_candidate_corpus_mismatch.py` (source files are not included in this documentation push).

Python module; see defined symbols and source.

**Top-level definitions/type:** `load_json`, `load_jsonl`, `extract_id`, `inspect_metadata`, `ids_from_rows`

## `diagnose_retrieval_ceiling.py`

Local source: `/Users/joshua/Downloads/phase2/diagnose_retrieval_ceiling.py` (source files are not included in this documentation push).

Python module; see defined symbols and source.

**Top-level definitions/type:** `load_jsonl`, `load_json`, `norm`, `gold_docs`, `tokens`, `recurse`

## `download_pubmed.py`

Local source: `/Users/joshua/Downloads/phase2/download_pubmed.py` (source files are not included in this documentation push).

Download SciFact corpus + claims, and load abstracts for FAISS indexing. Uses the official S3 tarball (GitHub raw links are dead). Primary source: SciFact corpus.jsonl Optional: Additional PubMed abstracts from data/pubm

**Top-level definitions/type:** `download_file`, `download_scifact`, `download_scifact_alternative`, `verify_scifact_files`, `load_scifact_abstracts`, `load_all_abstracts`

## `evaluate_bm25_extended.py`

Local source: `/Users/joshua/Downloads/phase2/evaluate_bm25_extended.py` (source files are not included in this documentation push).

Python module; see defined symbols and source.

**Top-level definitions/type:** `load_claims`, `evaluate`, `main`

## `evaluate_classification.py`

Local source: `/Users/joshua/Downloads/phase2/evaluate_classification.py` (source files are not included in this documentation push).

Python module; see defined symbols and source.

**Top-level definitions/type:** `load_scifact_ground_truth`, `main`

## `evaluate_hybrid.py`

Local source: `/Users/joshua/Downloads/phase2/evaluate_hybrid.py` (source files are not included in this documentation push).

Evaluate Hybrid BM25 + BioBERT retrieval. Uses Reciprocal Rank Fusion (RRF). Compares: BM25 BioBERT + FAISS Hybrid RRF Metrics: Recall@1 Recall@5 Recall@10 MRR

**Top-level definitions/type:** `normalize_id`, `load_claims`, `evaluate`, `print_results`, `main`

## `evaluate_react.py`

Local source: `/Users/joshua/Downloads/phase2/evaluate_react.py` (source files are not included in this documentation push).

Evaluate ReAct agent vs direct retrieval baseline. Measures: gold hit rate, avg hops, evidence quality.

**Top-level definitions/type:** `load_scifact_claims`, `evaluate_react`, `main`

## `evaluate_reranker.py`

Local source: `/Users/joshua/Downloads/phase2/evaluate_reranker.py` (source files are not included in this documentation push).

Python module; see defined symbols and source.

**Top-level definitions/type:** `load_claims`, `evaluate_reranker`, `main`

## `evaluate_retrieval.py`

Local source: `/Users/joshua/Downloads/phase2/evaluate_retrieval.py` (source files are not included in this documentation push).

Evaluate pure retrieval against SciFact gold evidence. Metrics: Recall@1 Recall@5 Recall@10 MRR Only evidence-bearing claims are included in retrieval metrics. Claims without evidence (NEI) are reported separately. This 

**Top-level definitions/type:** `normalize_id`, `load_scifact_claims`, `evaluate_retriever`, `print_metrics`, `main`

## `evidence_alignment_analysis.py`

Local source: `/Users/joshua/Downloads/phase2/evidence_alignment_analysis.py` (source files are not included in this documentation push).

Python module; see defined symbols and source.

**Top-level definitions/type:** `load_json`, `load_scifact`, `get_gold_doc_ids`, `main`

## `evidence_validator.py`

Local source: `/Users/joshua/Downloads/phase2/evidence_validator.py` (source files are not included in this documentation push).

Semantic Evidence Validator =========================== Separates retrieval ranking from evidence validity. The CrossEncoder answers approximately: "How well does this document rank for this query?" This validator answer

**Top-level definitions/type:** `SemanticEvidenceValidator`

## `freeze_union_candidates.py`

Local source: `/Users/joshua/Downloads/phase2/freeze_union_candidates.py` (source files are not included in this documentation push).

Python module; see defined symbols and source.

**Top-level definitions/type:** `load_jsonl`, `load_json`, `get_doc_id`, `get_claim_id`, `get_gold_ids`, `first_gold_rank`

## `freeze_validated_candidate_pool.py`

Local source: `/Users/joshua/Downloads/phase2/freeze_validated_candidate_pool.py` (source files are not included in this documentation push).

Python module; see defined symbols and source.

**Top-level definitions/type:** `load_jsonl`, `load_json`, `atomic_json_dump`, `sha256_file`, `result_ids`, `first_gold_rank`, `make_union`

## `phase2_final_bottleneck.py`

Local source: `/Users/joshua/Downloads/phase2/phase2_final_bottleneck.py` (source files are not included in this documentation push).

Python module; see defined symbols and source.

**Top-level definitions/type:** `norm_id`, `sint`, `sfloat`, `load_json`, `load_csv`, `first`, `flatten_records`, `extract_diagnostics`, `classify`, `p`

## `phase2_final_experiment.py`

Local source: `/Users/joshua/Downloads/phase2/phase2_final_experiment.py` (source files are not included in this documentation push).

Python module; see defined symbols and source.

**Top-level definitions/type:** `norm_id`, `sint`, `sfloat`, `load_json`, `load_csv`, `first`, `flatten_records`, `hit`, `rr10`, `exact_mcnemar_p`, `bootstrap_delta`, `extract_claim_evidence`, `baseline_policy`, `ce_only_policy`, `global_policy`, `learned_policy`, `ce_top1_rescue`, `ce_top2_rescue`, `ce_top3_rescue`, `best_of_ce_and_fixed`, `best_available_existing`, `evaluate_policy`, `bottleneck`, `p`

## `phase2_master_analysis.py`

Local source: `/Users/joshua/Downloads/phase2/phase2_master_analysis.py` (source files are not included in this documentation push).

Python module; see defined symbols and source.

**Top-level definitions/type:** `load_json`, `load_csv`, `first_existing`, `safe_float`, `safe_int`, `get_any`, `normalize_claim_id`, `reciprocal_rank`, `hit`, `bootstrap_mean_ci`, `paired_bootstrap_delta`, `exact_mcnemar_p`, `rank_bin`, `classify_failure`, `report`

## `polarity_checker.py`

Local source: `/Users/joshua/Downloads/phase2/polarity_checker.py` (source files are not included in this documentation push).

Python module; see defined symbols and source.

**Top-level definitions/type:** `normalize`, `detect_polarity`, `contains_negation`, `compare_polarity`

## `react_agent.py`

Local source: `/Users/joshua/Downloads/phase2/react_agent.py` (source files are not included in this documentation push).

================================================================================ PHASE 2 REACT AGENT: Local FAISS ONLY. No live API during evaluation. OLLAMA VERSION — Singleton retriever, deduplication, robust parsing. 

**Top-level definitions/type:** `AgentState`, `OllamaLLM`, `ReActAgent`, `save_phase2_output`

## `reranker.py`

Local source: `/Users/joshua/Downloads/phase2/reranker.py` (source files are not included in this documentation push).

Python module; see defined symbols and source.

**Top-level definitions/type:** `CrossEncoderReranker`

## `retriever.py`

Local source: `/Users/joshua/Downloads/phase2/retriever.py` (source files are not included in this documentation push).

Advanced retrieval module for SciFact. Retrievers: 1. BM25 2. BioBERT + FAISS 3. Hybrid BM25 + BioBERT using Reciprocal Rank Fusion (RRF) Designed for scientific claim -> evidence retrieval.

**Top-level definitions/type:** `tokenize_scientific_text`, `BM25Retriever`, `BioBERTRetriever`, `HybridRetriever`

## `retriever_backup.py`

Local source: `/Users/joshua/Downloads/phase2/retriever_backup.py` (source files are not included in this documentation push).

Pure retrieval classes. No LLM. No ReAct. These are your scientific baselines.

**Top-level definitions/type:** `BioBERTRetriever`, `BM25Retriever`

## `run_phase2.py`

Local source: `/Users/joshua/Downloads/phase2/run_phase2.py` (source files are not included in this documentation push).

MAIN PHASE 2 PIPELINE Validated retrieval architecture: Claim ↓ ReAct Agent / Qwen 2.5 7B ↓ Retrieval Query ↓ SciFact BM25 @20 + BioBERT Dense @20 over 35K corpus ↓ Candidate Union ↓ Cross-Encoder ↓ Locked V3.1 Fusion ↓ 

**Top-level definitions/type:** `load_scifact_claims`, `main`

## `test_35k_bm25_dense_rrf.py`

Local source: `/Users/joshua/Downloads/phase2/test_35k_bm25_dense_rrf.py` (source files are not included in this documentation push).

Python module; see defined symbols and source.

**Top-level definitions/type:** `load_jsonl`, `norm_id`, `gold_docs`, `tokenize`, `first_gold_rank`, `hit_at`

## `test_adaptive_fusion_master_v5.py`

Local source: `/Users/joshua/Downloads/phase2/test_adaptive_fusion_master_v5.py` (source files are not included in this documentation push).

Python module; see defined symbols and source.

**Top-level definitions/type:** `load_jsonl`, `tokenize`, `norm_id`, `gold_docs`, `get_doc_text`, `top_positions`, `minmax`, `first_gold_rank`, `hit`, `rr10`, `entropy_from_scores`, `rank_map`, `topk_overlap`, `spearman_on_common`, `exact_mcnemar`, `bootstrap_delta`, `metrics_from_ranks`, `objective`, `source_type`, `make_pool`, `rank_for_g`, `gate_g`, `jsonable`

## `test_advanced_ce_bottleneck.py`

Local source: `/Users/joshua/Downloads/phase2/test_advanced_ce_bottleneck.py` (source files are not included in this documentation push).

Python module; see defined symbols and source.

**Top-level definitions/type:** `load_jsonl`, `tokenize`, `norm_id`, `gold_docs`, `top_positions`, `first_gold_rank`, `reciprocal_rank`, `unique_preserve_order`, `get_doc_text`, `pool_for_config`, `rank_pool_by_ce`

## `test_ce_bottleneck_v2_locked.py`

Local source: `/Users/joshua/Downloads/phase2/test_ce_bottleneck_v2_locked.py` (source files are not included in this documentation push).

Python module; see defined symbols and source.

**Top-level definitions/type:** `load_jsonl`, `tokenize`, `norm_id`, `gold_docs`, `get_doc_text`, `top_positions`, `first_gold_rank`, `hit_at`, `reciprocal_rank`, `unique_preserve_order`, `make_pool`, `rank_by_ce`, `pct`

## `test_classification_cases.py`

Local source: `/Users/joshua/Downloads/phase2/test_classification_cases.py` (source files are not included in this documentation push).

Python module; see defined symbols and source.

**Top-level definitions/type:** No top-level functions/classes.

## `test_fusion_forensics_v4.py`

Local source: `/Users/joshua/Downloads/phase2/test_fusion_forensics_v4.py` (source files are not included in this documentation push).

Python module; see defined symbols and source.

**Top-level definitions/type:** `load_jsonl`, `tokenize`, `norm_id`, `gold_docs`, `get_doc_text`, `top_positions`, `minmax`, `first_gold_rank`, `lexical_overlap`, `unique_pool`, `source_type`, `classify_mechanism`

## `test_fusion_robustness_v32.py`

Local source: `/Users/joshua/Downloads/phase2/test_fusion_robustness_v32.py` (source files are not included in this documentation push).

Python module; see defined symbols and source.

**Top-level definitions/type:** `hit`, `rr10`, `exact_mcnemar`, `bootstrap_delta`, `objective`, `jackknife_stats`

## `test_fusion_significance_v31.py`

Local source: `/Users/joshua/Downloads/phase2/test_fusion_significance_v31.py` (source files are not included in this documentation push).

Python module; see defined symbols and source.

**Top-level definitions/type:** `load_jsonl`, `tokenize`, `norm_id`, `gold_docs`, `get_doc_text`, `top_positions`, `minmax`, `first_gold_rank`, `hit`, `rr10`, `unique_pool`, `bootstrap_delta`, `exact_mcnemar`, `safe_exact_mcnemar`, `rank_category`, `top_non_gold`, `best_gold_doc`

## `test_learned_router_v6.py`

Local source: `/Users/joshua/Downloads/phase2/test_learned_router_v6.py` (source files are not included in this documentation push).

Python module; see defined symbols and source.

**Top-level definitions/type:** `hit`, `rr10`, `first_gold_rank`, `rank_for_g`, `metrics_from_ranks`, `objective_from_rank`, `bootstrap_delta`, `exact_mcnemar`, `jsonable`, `extract_features`, `policy_ranks`, `metric_objective`

## `test_oracle_candidate_pool.py`

Local source: `/Users/joshua/Downloads/phase2/test_oracle_candidate_pool.py` (source files are not included in this documentation push).

Python module; see defined symbols and source.

**Top-level definitions/type:** `load_jsonl`, `tokenize`, `norm_id`, `gold_docs`, `first_gold_rank`, `has_gold`, `top_positions`

## `test_reranker.py`

Local source: `/Users/joshua/Downloads/phase2/test_reranker.py` (source files are not included in this documentation push).

Python module; see defined symbols and source.

**Top-level definitions/type:** `main`

## `test_reranker_ablation_v3.py`

Local source: `/Users/joshua/Downloads/phase2/test_reranker_ablation_v3.py` (source files are not included in this documentation push).

Python module; see defined symbols and source.

**Top-level definitions/type:** `load_jsonl`, `tokenize`, `norm_id`, `gold_docs`, `get_doc_text`, `top_positions`, `first_gold_rank`, `reciprocal_rank`, `hit_at`, `zscore`, `minmax`, `reciprocal_rank_score`, `unique_pool`, `evaluate_ranked_ids`, `pct`, `rank_method`, `evaluate_method`, `rank_distribution`

## `test_retrieval.py`

Local source: `/Users/joshua/Downloads/phase2/test_retrieval.py` (source files are not included in this documentation push).

Test retrieval without LLM (fast, for debugging FAISS).

**Top-level definitions/type:** `test_basic_retrieval`

## `test_source_aware_bm25_advanced.py`

Local source: `/Users/joshua/Downloads/phase2/test_source_aware_bm25_advanced.py` (source files are not included in this documentation push).

Python module; see defined symbols and source.

**Top-level definitions/type:** `load_jsonl`, `norm_id`, `gold_docs`, `tokenize`, `rank_top_k`, `first_gold_rank`, `hit_at`, `reciprocal_rank`, `median_or_none`, `evaluate_rankings`

## `test_source_balanced_dense.py`

Local source: `/Users/joshua/Downloads/phase2/test_source_balanced_dense.py` (source files are not included in this documentation push).

Python module; see defined symbols and source.

**Top-level definitions/type:** `load_jsonl`, `norm_id`, `gold_docs`, `hit`

## `test_two_cases.py`

Local source: `/Users/joshua/Downloads/phase2/test_two_cases.py` (source files are not included in this documentation push).

Python module; see defined symbols and source.

**Top-level definitions/type:** No top-level functions/classes.

## `test_validated_retriever_full_regression.py`

Local source: `/Users/joshua/Downloads/phase2/test_validated_retriever_full_regression.py` (source files are not included in this documentation push).

FULL V3.1 -> RUNTIME REPRODUCTION REGRESSION Purpose ------- Verify that ValidatedHybridRetriever reproduces the stored locked V3.1 fusion ranks for every claim represented in: results/fusion_significance_v31_claim_rows.

**Top-level definitions/type:** `save_json`, `first_gold_rank`

## `test_validated_retriever_reproduction.py`

Local source: `/Users/joshua/Downloads/phase2/test_validated_retriever_reproduction.py` (source files are not included in this documentation push).

Python module; see defined symbols and source.

**Top-level definitions/type:** `add_first`

## `test_weighted_rrf_sweep.py`

Local source: `/Users/joshua/Downloads/phase2/test_weighted_rrf_sweep.py` (source files are not included in this documentation push).

Python module; see defined symbols and source.

**Top-level definitions/type:** `load_jsonl`, `norm_id`, `gold_docs`, `tokenize`, `hit_at`, `first_gold_rank`

## `validated_retriever.py`

Local source: `/Users/joshua/Downloads/phase2/validated_retriever.py` (source files are not included in this documentation push).

Validated Phase 2 retrieval pipeline. Locked architecture: SciFact BM25@20 + BioBERT Dense@20 over 35K corpus | v Candidate Union | v Cross-Encoder | v Min-Max Fusion Fusion score: CE_mm + 0.50 * BM25_mm + 0.25 * Dense_m

**Top-level definitions/type:** `tokenize`, `norm_id`, `get_doc_text`, `top_positions`, `minmax`, `ValidatedHybridRetriever`

## `verify_baseline_construction.py`

Local source: `/Users/joshua/Downloads/phase2/verify_baseline_construction.py` (source files are not included in this documentation push).

Python module; see defined symbols and source.

**Top-level definitions/type:** `load_jsonl`, `load_json`

## `verify_biobert_baseline.py`

Local source: `/Users/joshua/Downloads/phase2/verify_biobert_baseline.py` (source files are not included in this documentation push).

Python module; see defined symbols and source.

**Top-level definitions/type:** `load_jsonl`, `load_json`

## `backups/pre_phase2_integration/config.py`

Local source: `/Users/joshua/Downloads/phase2/backups/pre_phase2_integration/config.py` (source files are not included in this documentation push).

Phase 2 Configuration NO TRAINING. Just paths and constants.

**Top-level definitions/type:** No top-level functions/classes.

## `backups/pre_phase2_integration/react_agent.py`

Local source: `/Users/joshua/Downloads/phase2/backups/pre_phase2_integration/react_agent.py` (source files are not included in this documentation push).

================================================================================ PHASE 2 REACT AGENT: Local FAISS ONLY. No live API during evaluation. OLLAMA VERSION — Singleton retriever, deduplication, robust parsing. 

**Top-level definitions/type:** `AgentState`, `OllamaLLM`, `ReActAgent`, `save_phase2_output`

## `backups/pre_phase2_integration/reranker.py`

Local source: `/Users/joshua/Downloads/phase2/backups/pre_phase2_integration/reranker.py` (source files are not included in this documentation push).

Python module; see defined symbols and source.

**Top-level definitions/type:** `CrossEncoderReranker`

## `backups/pre_phase2_integration/retriever.py`

Local source: `/Users/joshua/Downloads/phase2/backups/pre_phase2_integration/retriever.py` (source files are not included in this documentation push).

Advanced retrieval module for SciFact. Retrievers: 1. BM25 2. BioBERT + FAISS 3. Hybrid BM25 + BioBERT using Reciprocal Rank Fusion (RRF) Designed for scientific claim -> evidence retrieval.

**Top-level definitions/type:** `tokenize_scientific_text`, `BM25Retriever`, `BioBERTRetriever`, `HybridRetriever`

## `backups/pre_phase2_integration/run_phase2.py`

Local source: `/Users/joshua/Downloads/phase2/backups/pre_phase2_integration/run_phase2.py` (source files are not included in this documentation push).

MAIN PHASE 2 PIPELINE Pipeline: Claim ↓ BM25 Top-50 ↓ Cross-Encoder Reranker ↓ Top-k evidence ↓ ReAct Agent ↓ Qwen 2.5 7B This is the main script used to generate Phase 2 output.

**Top-level definitions/type:** `load_scifact_claims`, `main`
