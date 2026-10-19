# phase-4: source file catalog

Source root: `/Users/joshua/Downloads/Phase4-main`

Generated from local files. Inclusion does not imply a file is active, tested, or production-ready. Backups and historical experiments are included when present. Descriptions are module docstrings or structural summaries, not an audit of correctness.

## `ablation_eval.py`

Local source: `/Users/joshua/Downloads/Phase4-main/ablation_eval.py` (source files are not included in this documentation push).

Python module; see defined symbols and source.

**Top-level definitions/type:** `AblationDataset`, `evaluate_condition`, `main`

## `advanced_phase4_causal_audit.py`

Local source: `/Users/joshua/Downloads/Phase4-main/advanced_phase4_causal_audit.py` (source files are not included in this documentation push).

Python module; see defined symbols and source.

**Top-level definitions/type:** `load_jsonl`, `atomic_json`, `atomic_jsonl`, `sha256`, `normalize_space`, `safe_title`, `vector_metrics`, `aggregate_condition`

## `analyze_label_conflicts.py`

Local source: `/Users/joshua/Downloads/Phase4-main/analyze_label_conflicts.py` (source files are not included in this documentation push).

Python module; see defined symbols and source.

**Top-level definitions/type:** `normalize_text`, `atomic_write_text`, `write_json`, `load_conflicts`, `get_label`, `main`

## `audit_evidence_text_conflicts.py`

Local source: `/Users/joshua/Downloads/Phase4-main/audit_evidence_text_conflicts.py` (source files are not included in this documentation push).

Python module; see defined symbols and source.

**Top-level definitions/type:** `read_jsonl`, `normalize`, `normalize_aggressive`, `tokens`, `token_jaccard`, `containment`, `sequence_similarity`, `prefix_relationship`, `duplicate_title_prefix`, `classify_pair`

## `build_leakage_safe_splits.py`

Local source: `/Users/joshua/Downloads/Phase4-main/build_leakage_safe_splits.py` (source files are not included in this documentation push).

Python module; see defined symbols and source.

**Top-level definitions/type:** `normalize_text`, `normalize_claim`, `claim_hash`, `evidence_normalized`, `load_jsonl`, `atomic_write_text`, `write_json`, `write_jsonl`, `load_data`, `repair_claim_hashes`, `remove_exact_duplicates`, `build_claim_groups`, `choose_target_split`, `assign_claim_groups`, `audit_conflicting_claims`, `unique_claims`, `audit_leakage`, `audit_exact_duplicates`, `audit_hashes`, `statistics`, `calculate_class_weights`, `write_csv`, `main`

## `build_scifact_e2_benchmark.py`

Local source: `/Users/joshua/Downloads/Phase4-main/build_scifact_e2_benchmark.py` (source files are not included in this documentation push).

Python module; see defined symbols and source.

**Top-level definitions/type:** `BenchmarkError`, `normalize_text`, `sha256_text`, `sha256_file`, `atomic_write_text`, `atomic_write_json`, `atomic_write_jsonl`, `read_jsonl`, `validate_phase4_row`, `load_scifact_rows`, `load_phase2_corpus_ids`, `build_claim_records`, `shingles`, `jaccard`, `UnionFind`, `find_near_duplicate_groups`, `proportional_targets`, `class_vector`, `score_assignment`, `assign_groups`, `group_assignment_split`, `move_group`, `split_counts_from_assignments`, `exact_size_rebalance`, `create_split_rows`, `distribution`, `verify_split_integrity`, `gold_summary`, `build_readme`, `main`

## `closed_world_diagnostic.py`

Local source: `/Users/joshua/Downloads/Phase4-main/closed_world_diagnostic.py` (source files are not included in this documentation push).

closed_world_diagnostic.py PURPOSE ------- Diagnostic and provenance analysis ONLY. This script trains nothing, evaluates no model, and loads no verifier checkpoint. It answers, empirically: A. What exactly are the docum

**Top-level definitions/type:** `DiagnosticError`, `fail`, `atomic_text`, `atomic_json`, `atomic_jsonl`, `sha256_file`, `sha256_text`, `load_jsonl`, `cache_path`, `cache_load`, `cache_store`, `normalize_basic`, `normalize_strict`, `token_shingles`, `jaccard`, `containment`, `preview`, `extract_pmid`, `_shingle_hashes`, `build_minhash_matrix`, `lsh_buckets`, `lsh_candidate_pairs`, `lsh_query_index`, `lsh_query`, `project_import_path`, `clear_modules`, `discover_corpus_files`, `probe_phase2_api`, `_format_candidates`, `load_corpus`, `analyze_corpus`, `parse_label`, `detect_field`, `analyze_split_schema`, `build_corpus_index`, `match_one_row`, `grounding_of`, `run_gold_matching`, `aggregate_claims`, `row_level_summary`, `retrieval_support_by_dataset`, `run_leakage_analysis`, `evidence_document_overlap`, `render_report`, `main`

## `config.yaml`

Local source: `/Users/joshua/Downloads/Phase4-main/config.yaml` (source files are not included in this documentation push).

Configuration file; values are intentionally not copied into this catalog.

**Top-level definitions/type:** Configuration

## `create_demo_data.py`

Local source: `/Users/joshua/Downloads/Phase4-main/create_demo_data.py` (source files are not included in this documentation push).

create_demo_data.py Creates a demo CSV for multimodal inference from your Phase 1 FakeHealth data. Run this ONCE to generate data/pipeline/fakehealth_for_demo.csv

**Top-level definitions/type:** `create_fakehealth_demo_csv`

## `diagnose_end_to_end_failure.py`

Local source: `/Users/joshua/Downloads/Phase4-main/diagnose_end_to_end_failure.py` (source files are not included in this documentation push).

Python module; see defined symbols and source.

**Top-level definitions/type:** `set_seed`, `get_device`, `safe_float`, `atomic_text`, `atomic_json`, `atomic_jsonl`, `load_jsonl`, `select_input_file`, `evidence_text`, `evidence_identity`, `short_title`, `validate_results`, `initialize_model3`, `predict_pair`, `get_saved_pair_probs`, `aggregate_probs`, `calculate_metrics`, `overlap_count`, `top1_same`, `mean_field`, `max_field`, `main`

## `diagnose_phase4_input_dependence.py`

Local source: `/Users/joshua/Downloads/Phase4-main/diagnose_phase4_input_dependence.py` (source files are not included in this documentation push).

Python module; see defined symbols and source.

**Top-level definitions/type:** `read_jsonl`, `write_jsonl`, `entropy`, `js_divergence`, `l1_distance`, `stable_hash`, `mean_or_nan`, `median_or_nan`, `pct`, `try_construct_from_module`, `extract_logits`, `predict_pair`, `choose_random_evidence`, `get_evidence_text`

## `discover_scifact_gold_mapping.py`

Local source: `/Users/joshua/Downloads/Phase4-main/discover_scifact_gold_mapping.py` (source files are not included in this documentation push).

Python module; see defined symbols and source.

**Top-level definitions/type:** `load_jsonl`, `norm_text`, `flatten_keys`, `inspect_json`, `inspect_jsonl`, `inspect_delimited`, `score_candidate`

## `evaluate.py`

Local source: `/Users/joshua/Downloads/Phase4-main/evaluate.py` (source files are not included in this documentation push).

Python module; see defined symbols and source.

**Top-level definitions/type:** `main`

## `evaluate_end_to_end_balanced.py`

Local source: `/Users/joshua/Downloads/Phase4-main/evaluate_end_to_end_balanced.py` (source files are not included in this documentation push).

Python module; see defined symbols and source.

**Top-level definitions/type:** `project_import_path`, `clear_modules`, `clear_package_prefix`, `set_seed`, `get_device`, `sha256_file`, `atomic_text`, `atomic_json`, `atomic_jsonl`, `append_jsonl`, `load_jsonl`, `first_nonempty`, `extract_claim`, `extract_label`, `normalized_claim`, `safe_float`, `sigmoid`, `validate_subset`, `initialize_phase2`, `retrieve_evidence`, `initialize_phase3`, `classify_and_rank`, `initialize_phase4`, `evidence_text`, `predict_pair`, `aggregate_probabilities`, `run_one_claim`, `load_progress`, `calculate_metrics`, `save_confusion_matrix`, `save_predictions_csv`, `initialize_phase5`, `make_phase5_record`, `summarize_phase5`, `main`

## `evaluate_hard_negative_e2e_validation.py`

Local source: `/Users/joshua/Downloads/Phase4-main/evaluate_hard_negative_e2e_validation.py` (source files are not included in this documentation push).

Python module; see defined symbols and source.

**Top-level definitions/type:** `PipelineError`, `seed_everything`, `choose_device`, `find_existing`, `read_jsonl`, `atomic_write_json`, `atomic_write_jsonl`, `write_csv`, `extract_claim_text`, `extract_claim_hash`, `extract_label`, `extract_ranked_evidence`, `extract_evidence_text`, `extract_hierarchy_weight`, `extract_retrieval_score`, `PubMedBERTVerifier`, `load_checkpoint_model`, `build_cache_map`, `align_validation`, `softmax_numpy`, `score_claim_evidence`, `compute_or_load_epoch_probabilities`, `calculate_metrics`, `normalized_retrieval_scores`, `evidence_weights`, `aggregate_weighted_mean`, `aggregate_max_probability`, `aggregate_margin_competition`, `aggregate_log_odds`, `aggregate_temperature_mean`, `evaluate_predictions`, `is_better`, `flatten_result`, `search_epoch`, `print_best`, `main`

## `evaluate_model3_final_test.py`

Local source: `/Users/joshua/Downloads/Phase4-main/evaluate_model3_final_test.py` (source files are not included in this documentation push).

Python module; see defined symbols and source.

**Top-level definitions/type:** `set_seed`, `get_device`, `atomic_json_save`, `Example`, `first_nonempty`, `normalize_label`, `evidence_to_text`, `parse_record`, `load_jsonl`, `PairDataset`, `make_collator`, `PubMedBERTVerifier`, `calculate_metrics`, `evaluate`, `write_predictions_csv`, `write_predictions_jsonl`, `print_class_metrics`, `print_confusion_matrix`, `main`

## `evaluate_relation_aware_v2.py`

Local source: `/Users/joshua/Downloads/Phase4-main/evaluate_relation_aware_v2.py` (source files are not included in this documentation push).

Python module; see defined symbols and source.

**Top-level definitions/type:** `set_seed`, `get_device`, `atomic_text`, `atomic_json`, `atomic_jsonl`, `load_jsonl`, `safe_float`, `evidence_text`, `evidence_identity`, `get_tier`, `get_hierarchy_weight`, `get_retrieval_score`, `merge_candidate_sets`, `initialize_phase4`, `phase4_predict`, `initialize_nli`, `nli_predict`, `evidence_quality`, `relation_aware_scores`, `calculate_metrics`, `main`

## `evaluate_relation_aware_v3.py`

Local source: `/Users/joshua/Downloads/Phase4-main/evaluate_relation_aware_v3.py` (source files are not included in this documentation push).

Python module; see defined symbols and source.

**Top-level definitions/type:** `set_seed`, `get_device`, `atomic_text`, `atomic_json`, `atomic_jsonl`, `load_jsonl`, `safe_float`, `normalize_vector`, `evidence_text`, `evidence_identity`, `get_tier`, `get_hierarchy_weight`, `get_retrieval_score`, `merge_candidates`, `initialize_phase4`, `phase4_predict`, `initialize_biomedical_nli`, `biomedical_nli_predict`, `evidence_quality`, `fuse_single_evidence`, `aggregate_claim`, `calculate_metrics`, `validate_input`, `main`

## `evaluate_scifact_e2_full_pipeline.py`

Local source: `/Users/joshua/Downloads/Phase4-main/evaluate_scifact_e2_full_pipeline.py` (source files are not included in this documentation push).

Python module; see defined symbols and source.

**Top-level definitions/type:** `PipelineEvaluationError`, `seed_everything`, `read_jsonl`, `atomic_write_text`, `atomic_write_json`, `atomic_write_jsonl`, `sha256_file`, `choose_device`, `normalize_score`, `sigmoid`, `validate_validation_rows`, `load_phase2`, `bm25_search`, `rerank_documents`, `load_phase3`, `extract_doc_id`, `extract_reranker_raw_score`, `prepare_phase3_evidence`, `classify_evidence`, `rank_phase3`, `load_cache`, `save_cache`, `PubMedBERTVerifier`, `load_checkpoint`, `phase4_probabilities`, `evidence_aggregation_weight`, `aggregate_claim`, `calculate_metrics`, `build_retrieval_phase3_cache`, `evaluate_epoch_topk`, `main`

## `evaluate_scifact_e2_retrieval.py`

Local source: `/Users/joshua/Downloads/Phase4-main/evaluate_scifact_e2_retrieval.py` (source files are not included in this documentation push).

Python module; see defined symbols and source.

**Top-level definitions/type:** `RetrievalEvaluationError`, `read_jsonl`, `atomic_write_text`, `atomic_write_json`, `atomic_write_jsonl`, `validate_claim`, `load_phase2_components`, `verify_component_interfaces`, `document_id`, `run_bm25_search`, `run_reranker`, `first_gold_rank`, `metrics_from_ranks`, `main`

## `export_phase5_predictions.py`

Local source: `/Users/joshua/Downloads/Phase4-main/export_phase5_predictions.py` (source files are not included in this documentation push).

Python module; see defined symbols and source.

**Top-level definitions/type:** `choose_device`, `normalize_text`, `first_present`, `safe_float`, `load_json`, `atomic_write_json`, `atomic_write_jsonl`, `PubMedBERTCrossEncoder`, `find_state_dict`, `remove_wrapper_prefixes`, `remap_encoder_names`, `inspect_checkpoint`, `load_phase4_model`, `validate_phase3_root`, `extract_evidence_text`, `extract_evidence_id`, `extract_hierarchy`, `extract_hierarchy_weight`, `extract_retrieval_score`, `extract_weighted_score`, `predict_claim_evidence_pair`, `aggregate_evidence_predictions`, `write_predictions_csv`, `main`

## `final_test_crossencoder.py`

Local source: `/Users/joshua/Downloads/Phase4-main/final_test_crossencoder.py` (source files are not included in this documentation push).

Python module; see defined symbols and source.

**Top-level definitions/type:** `save_json`, `save_csv`, `load_raw_rows`, `calculate_metrics`, `calculate_per_dataset_metrics`, `validate_checkpoint`, `main`

## `inference_pipeline.py`

Local source: `/Users/joshua/Downloads/Phase4-main/inference_pipeline.py` (source files are not included in this documentation push).

End-to-end inference: Claim -> Retrieve Evidence (mock) -> Weight -> Verify

**Top-level definitions/type:** `predict_claim`, `main`

## `inspect_phase1_checkpoint.py`

Local source: `/Users/joshua/Downloads/Phase4-main/inspect_phase1_checkpoint.py` (source files are not included in this documentation push).

Python module; see defined symbols and source.

**Top-level definitions/type:** `atomic_write_text`, `write_json`, `human_bytes`, `safe_value`, `load_checkpoint`, `looks_like_state_dict`, `find_state_dict`, `tensor_statistics`, `analyze_state_dict`, `architecture_key_groups`, `identify_linear_candidates`, `extract_metadata`, `build_text_report`, `print_summary`, `main`

## `inspect_phase1_critical.py`

Local source: `/Users/joshua/Downloads/Phase4-main/inspect_phase1_critical.py` (source files are not included in this documentation push).

Python module; see defined symbols and source.

**Top-level definitions/type:** `load_checkpoint`, `print_tensor`, `find_key`, `infer_bert_dimensions`, `infer_vit_dimensions`, `print_critical_layers`, `print_checkpoint_metadata`, `main`

## `multimodal_demo.py`

Local source: `/Users/joshua/Downloads/Phase4-main/multimodal_demo.py` (source files are not included in this documentation push).

multimodal_demo.py Demonstrates end-to-end multimodal inference on Phase 1 datasets. This proves the architecture can process images, even though benchmark training was text-only.

**Top-level definitions/type:** `MultimodalDemoDataset`, `collate_fn`, `evaluate_multimodal`, `main`

## `notepad inspect_scifact.py`

Local source: `/Users/joshua/Downloads/Phase4-main/notepad%20inspect_scifact.py` (source files are not included in this documentation push).

Python module; see defined symbols and source.

**Top-level definitions/type:** No top-level functions/classes.

## `optimize_scifact_e2_aggregation.py`

Local source: `/Users/joshua/Downloads/Phase4-main/optimize_scifact_e2_aggregation.py` (source files are not included in this documentation push).

Python module; see defined symbols and source.

**Top-level definitions/type:** `EvaluationError`, `seed_everything`, `read_jsonl`, `atomic_write_json`, `atomic_write_jsonl`, `choose_device`, `validate_data`, `PubMedBERTVerifier`, `load_checkpoint`, `pair_cache_path`, `calculate_epoch_pair_probabilities`, `hierarchy_quality`, `retrieval_quality`, `quality_multiplier`, `rank_multiplier`, `relation_scores`, `predict_claim`, `calculate_metrics`, `threshold_values`, `class_margin_values`, `evaluate_configuration`, `main`

## `phase4_claim_provenance_resolver.py`

Local source: `/Users/joshua/Downloads/Phase4-main/phase4_claim_provenance_resolver.py` (source files are not included in this documentation push).

Python module; see defined symbols and source.

**Top-level definitions/type:** `load_jsonl`, `write_jsonl`, `norm_id`, `normalize_claim`, `compact_claim`, `sha256`, `extract_claim`, `extract_raw_scifact_gold`, `extract_processed_gold`, `get_source_id`

## `phase4_counterfactual_robustness_audit.py`

Local source: `/Users/joshua/Downloads/Phase4-main/phase4_counterfactual_robustness_audit.py` (source files are not included in this documentation push).

Python module; see defined symbols and source.

**Top-level definitions/type:** `load_jsonl`, `normalize_space`, `normalize_eid`, `sha256`, `metrics`, `predict`, `aggregate`

## `phase4_crossencoder.py`

Local source: `/Users/joshua/Downloads/Phase4-main/phase4_crossencoder.py` (source files are not included in this documentation push).

Python module; see defined symbols and source.

**Top-level definitions/type:** `set_seed`, `get_device`, `save_json`, `load_class_weights`, `ClaimEvidenceDataset`, `PubMedBERTVerifier`, `move_batch`, `calculate_metrics`, `evaluate`, `save_checkpoint`, `main`

## `phase4_exact_evidence_anatomy.py`

Local source: `/Users/joshua/Downloads/Phase4-main/phase4_exact_evidence_anatomy.py` (source files are not included in this documentation push).

Python module; see defined symbols and source.

**Top-level definitions/type:** `load_jsonl`, `norm`, `norm_id`

## `phase4_gold_alignment_audit.py`

Local source: `/Users/joshua/Downloads/Phase4-main/phase4_gold_alignment_audit.py` (source files are not included in this documentation push).

Python module; see defined symbols and source.

**Top-level definitions/type:** `load_jsonl`, `write_jsonl`, `sha256`, `norm_id`, `normalize_claim`, `compact_claim`, `candidate_ids_from_dev`

## `phase4_representation_decomposition_audit.py`

Local source: `/Users/joshua/Downloads/Phase4-main/phase4_representation_decomposition_audit.py` (source files are not included in this documentation push).

Python module; see defined symbols and source.

**Top-level definitions/type:** `load_jsonl`, `norm`, `eid`, `predict`, `metric`, `token_ids`, `longest_common_prefix`, `longest_common_suffix`, `count_subsequence`, `remove_one_title_copy`, `strip_repeated_prefix`

## `phase4_semantic_evidence_hierarchy_audit.py`

Local source: `/Users/joshua/Downloads/Phase4-main/phase4_semantic_evidence_hierarchy_audit.py` (source files are not included in this documentation push).

Python module; see defined symbols and source.

**Top-level definitions/type:** `load_jsonl`, `write_jsonl`, `norm`, `norm_id`, `sha256`, `predict`, `entropy`, `confidence`, `margin`, `l1`, `kl`, `bootstrap_mean_ci`, `bootstrap_rate_ci`, `canonical_text`, `historical_text`, `get_gold_ids`, `find_gold_ids_recursive`, `add_job`

## `phase4_token_level_evidence_forensics.py`

Local source: `/Users/joshua/Downloads/Phase4-main/phase4_token_level_evidence_forensics.py` (source files are not included in this documentation push).

Python module; see defined symbols and source.

**Top-level definitions/type:** `load_jsonl`, `normalize_space`, `normalize_eid`, `sha256`, `predict`, `l1`, `first_difference`, `common_prefix_length`, `common_suffix_length`, `jaccard_tokens`, `safe_percentile`, `write_jsonl`, `group_stats`

## `prepare_phase4_e2_training_data.py`

Local source: `/Users/joshua/Downloads/Phase4-main/prepare_phase4_e2_training_data.py` (source files are not included in this documentation push).

Python module; see defined symbols and source.

**Top-level definitions/type:** `DataPreparationError`, `normalize_text`, `sha256_file`, `atomic_write_text`, `atomic_write_json`, `atomic_write_jsonl`, `read_jsonl`, `load_claim_hashes`, `validate_source_row`, `dataset_distribution`, `label_distribution`, `claim_label_audit`, `exact_pair_conflict_audit`, `assert_no_exact_pair_conflicts`, `main`

## `preprocess.py`

Local source: `/Users/joshua/Downloads/Phase4-main/preprocess.py` (source files are not included in this documentation push).

Python module; see defined symbols and source.

**Top-level definitions/type:** `Example`, `normalize_whitespace`, `normalize_label`, `normalize_claim_for_hash`, `sha256_text`, `claim_hash`, `build_sample_id`, `atomic_write_text`, `write_json`, `write_jsonl`, `map_label`, `resolve_column`, `dataframe_to_examples`, `load_scifact_corpus`, `scifact_evidence_text`, `load_scifact`, `load_pubhealth`, `load_clinifact`, `read_healthfc_csv`, `load_healthfc_raw`, `stable_hash_fraction`, `split_unsplit_examples`, `remove_exact_duplicates`, `validate_examples`, `check_split_leakage`, `compute_statistics`, `print_statistics`, `examples_to_dataframe`, `write_csv_atomic`, `write_outputs`, `merge_dataset_splits`, `main`

## `resolve_dev90_evidence_sources.py`

Local source: `/Users/joshua/Downloads/Phase4-main/resolve_dev90_evidence_sources.py` (source files are not included in this documentation push).

Python module; see defined symbols and source.

**Top-level definitions/type:** `read_jsonl`, `normalize_id`, `normalize_text`, `sha`, `scalar_id_candidates`, `text_candidates`, `title_candidates`, `walk_object`, `choose_best_text`

## `select_balanced_subset.py`

Local source: `/Users/joshua/Downloads/Phase4-main/select_balanced_subset.py` (source files are not included in this documentation push).

Python module; see defined symbols and source.

**Top-level definitions/type:** `normalize_text`, `atomic_write_text`, `get_first`, `get_claim`, `get_dataset`, `get_label`, `load_jsonl`, `sha256_text`, `main`

## `smoke_test.py`

Local source: `/Users/joshua/Downloads/Phase4-main/smoke_test.py` (source files are not included in this documentation push).

Python module; see defined symbols and source.

**Top-level definitions/type:** `resolve_path`, `load_class_weights`, `print_trainability`, `gradient_abs_sum`, `module_gradient_report`, `print_gradient_audit`, `assert_no_gradients`, `assert_nonzero_gradient`, `main`

## `train.py`

Local source: `/Users/joshua/Downloads/Phase4-main/train.py` (source files are not included in this documentation push).

Python module; see defined symbols and source.

**Top-level definitions/type:** `resolve_path`, `atomic_write_text`, `atomic_json_dump`, `load_class_weights`, `batch_to_device`, `calculate_metrics`, `evaluate_validation`, `save_checkpoint`, `main`

## `train_and_evaluate_e2e_final.py`

Local source: `/Users/joshua/Downloads/Phase4-main/train_and_evaluate_e2e_final.py` (source files are not included in this documentation push).

Python module; see defined symbols and source.

**Top-level definitions/type:** `seed_everything`, `device`, `cleanup_torch`, `normalize_claim`, `sigmoid`, `safe_float`, `atomic_text`, `atomic_json`, `atomic_jsonl`, `load_jsonl`, `sha256_file`, `discover_split_file`, `read_table`, `first_present`, `parse_label`, `canonical_row`, `canonicalize_rows`, `load_model3_class`, `load_model3_checkpoint`, `load_biomedical_nli`, `nli_batch`, `generate_hard_negatives`, `PairDataset`, `collate_function`, `metrics`, `evaluate_model`, `train_retrieval_conditioned_model`, `create_fresh_final_subset`, `project_import_path`, `clear_modules`, `build_fresh_retrieval_cache`, `evidence_text`, `evidence_id`, `merged_candidates_from_dev`, `phase4_batch_predict`, `build_feature_cache`, `normalize_probabilities`, `fuse_claim`, `select_fusion_config`, `evaluate_final`, `main`

## `train_balanced_retrieval_curriculum.py`

Local source: `/Users/joshua/Downloads/Phase4-main/train_balanced_retrieval_curriculum.py` (source files are not included in this documentation push).

Python module; see defined symbols and source.

**Top-level definitions/type:** `PipelineError`, `seed_everything`, `choose_device`, `read_jsonl`, `atomic_write_jsonl`, `atomic_write_json`, `normalize_text`, `pair_hash`, `normalize_label`, `extract_label`, `extract_claim_text`, `extract_claim_key`, `get_gold_ids`, `canonical_evidence_text`, `canonicalize_existing_training_row`, `load_phase2`, `bm25_search`, `rerank`, `find_phase2_documents`, `PubMedBERTVerifier`, `load_checkpoint_model`, `initialize_from_clean_checkpoint`, `score_pairs`, `make_training_row`, `mine_retrieval_conditioned_rows`, `deduplicate_rows`, `sample_replay_rows`, `balance_retrieval_rows`, `build_curriculum`, `PairDataset`, `calculate_metrics`, `evaluate_pair_loader`, `extract_ranked_evidence`, `align_e2e_validation`, `doc_hierarchy_weight`, `doc_retrieval_score`, `score_e2e_claim`, `compute_or_load_e2e_pairs`, `feature_vector`, `build_feature_matrix`, `heuristic_predictions`, `cross_validated_stacker`, `make_oracle_loader`, `train_curriculum`, `main`

## `train_claim_level_e2e_classifier.py`

Local source: `/Users/joshua/Downloads/Phase4-main/train_claim_level_e2e_classifier.py` (source files are not included in this documentation push).

Python module; see defined symbols and source.

**Top-level definitions/type:** `PipelineError`, `seed_everything`, `choose_device`, `read_jsonl`, `atomic_write_jsonl`, `atomic_write_json`, `normalize_text`, `text_hash`, `extract_claim_text`, `extract_claim_key`, `normalize_label`, `extract_label`, `canonical_evidence_text`, `load_phase2`, `bm25_search`, `rerank_docs`, `PubMedBERTVerifier`, `load_verifier`, `score_documents`, `build_or_load_train_features`, `extract_ranked_evidence`, `build_or_load_val_features`, `_safe_stats`, `feature_vector`, `build_xy`, `calculate_metrics`, `print_metrics`, `model_candidates`, `cross_validate_train_models`, `main`

## `train_model3_improved.py`

Local source: `/Users/joshua/Downloads/Phase4-main/train_model3_improved.py` (source files are not included in this documentation push).

Python module; see defined symbols and source.

**Top-level definitions/type:** `set_seed`, `get_device`, `atomic_json_save`, `atomic_torch_save`, `Example`, `first_nonempty`, `normalize_label`, `evidence_to_text`, `parse_record`, `load_jsonl`, `PairDataset`, `make_collator`, `PubMedBERTVerifier`, `calculate_class_weights`, `calculate_metrics`, `validate`, `load_phase3_claims`, `phase3_evidence_text`, `phase3_weight`, `predict_pair`, `export_phase5_predictions`, `main`

## `train_pipeline_aligned_claim_classifier.py`

Local source: `/Users/joshua/Downloads/Phase4-main/train_pipeline_aligned_claim_classifier.py` (source files are not included in this documentation push).

Python module; see defined symbols and source.

**Top-level definitions/type:** `PipelineError`, `seed_everything`, `choose_device`, `read_jsonl`, `atomic_write_jsonl`, `atomic_write_json`, `normalize_text`, `text_hash`, `extract_claim_text`, `extract_claim_key`, `normalize_label`, `extract_label`, `canonical_evidence_text`, `load_phase2_and_phase3`, `bm25_search`, `rerank_docs`, `PubMedBERTVerifier`, `load_verifier`, `score_documents`, `phase3_classify_document`, `phase3_rank_documents`, `build_or_load_train_phase3_cache`, `build_or_load_train_features`, `extract_ranked_evidence`, `build_or_load_val_features`, `_safe_stats`, `feature_vector`, `build_xy`, `calculate_metrics`, `print_metrics`, `cross_validate_train_models`, `fit_final_combined_model`, `main`

## `train_pipeline_aligned_claim_classifier_fixed.py`

Local source: `/Users/joshua/Downloads/Phase4-main/train_pipeline_aligned_claim_classifier_fixed.py` (source files are not included in this documentation push).

Python module; see defined symbols and source.

**Top-level definitions/type:** `PipelineError`, `seed_everything`, `choose_device`, `read_jsonl`, `atomic_write_jsonl`, `atomic_write_json`, `normalize_text`, `text_hash`, `extract_claim_text`, `extract_claim_key`, `normalize_label`, `extract_label`, `canonical_evidence_text`, `load_phase2_and_phase3`, `bm25_search`, `rerank_docs`, `PubMedBERTVerifier`, `load_verifier`, `score_documents`, `phase3_classify_document`, `phase3_rank_documents`, `build_or_load_train_phase3_cache`, `build_or_load_train_features`, `extract_ranked_evidence`, `build_or_load_val_features`, `_safe_stats`, `feature_vector`, `build_xy`, `calculate_metrics`, `print_metrics`, `cross_validate_train_models`, `fit_final_combined_model`, `main`

## `train_retrieval_hard_negative_verifier.py`

Local source: `/Users/joshua/Downloads/Phase4-main/train_retrieval_hard_negative_verifier.py` (source files are not included in this documentation push).

Python module; see defined symbols and source.

**Top-level definitions/type:** `PipelineError`, `seed_everything`, `choose_device`, `read_jsonl`, `atomic_write_jsonl`, `atomic_write_json`, `normalize_text`, `pair_hash`, `load_phase2`, `bm25_search`, `rerank`, `PubMedBERTVerifier`, `load_source_model`, `score_pairs`, `get_gold_ids`, `mine_hard_negatives`, `validate_no_final_leakage`, `build_augmented_training_data`, `PairDataset`, `calculate_metrics`, `calculate_softened_weights`, `evaluate`, `train_model`, `main`

## `train_scifact_e2_verifier.py`

Local source: `/Users/joshua/Downloads/Phase4-main/train_scifact_e2_verifier.py` (source files are not included in this documentation push).

Python module; see defined symbols and source.

**Top-level definitions/type:** `TrainingError`, `seed_everything`, `read_jsonl`, `validate_rows`, `choose_device`, `ClaimEvidenceDataset`, `PubMedBERTVerifier`, `calculate_class_weights`, `evaluate`, `save_checkpoint`, `atomic_json`, `main`

## `validate_data.py`

Local source: `/Users/joshua/Downloads/Phase4-main/validate_data.py` (source files are not included in this documentation push).

Python module; see defined symbols and source.

**Top-level definitions/type:** `normalize_text`, `normalize_claim`, `sha256_text`, `normalized_claim_hash`, `atomic_write_text`, `write_json`, `load_jsonl`, `load_all_splits`, `validate_schema`, `validate_labels`, `audit_sample_ids`, `validate_claim_hashes`, `audit_empty_text`, `audit_exact_duplicates`, `audit_claim_label_conflicts`, `build_claim_index`, `audit_cross_split_leakage`, `audit_dataset_distributions`, `calculate_class_weights`, `audit_text_lengths`, `percentile`, `describe_numbers`, `audit_image_policy`, `build_leakage_recommendation`, `print_report`, `main`

## `validate_phase4_canonical_replay.py`

Local source: `/Users/joshua/Downloads/Phase4-main/validate_phase4_canonical_replay.py` (source files are not included in this documentation push).

Python module; see defined symbols and source.

**Top-level definitions/type:** `read_jsonl`, `normalize_id`, `normalize_ws`, `max_abs_error`, `mean_abs_error`, `l1_error`, `kl_divergence`, `construct_variants`, `predict`

## `results/checkpoint_replay_audit/run_exact_replay.py`

Local source: `/Users/joshua/Downloads/Phase4-main/results/checkpoint_replay_audit/run_exact_replay.py` (source files are not included in this documentation push).

Python module; see defined symbols and source.

**Top-level definitions/type:** `banner`, `read_jsonl`, `normalize_id`, `normalize_text`, `extract_possible_evidence_id`, `extract_possible_text`, `recursively_extract_records`, `inspect_json_file`, `safe_argmax`, `entropy`, `top2_margin`, `l1_distance`, `max_abs_difference`, `js_divergence`, `predict`

## `src/__init__.py`

Local source: `/Users/joshua/Downloads/Phase4-main/src/__init__.py` (source files are not included in this documentation push).

Python module; see defined symbols and source.

**Top-level definitions/type:** No top-level functions/classes.

## `src/checkpoint.py`

Local source: `/Users/joshua/Downloads/Phase4-main/src/checkpoint.py` (source files are not included in this documentation push).

Python module; see defined symbols and source.

**Top-level definitions/type:** `load_torch_checkpoint`, `get_model_state_dict`, `extract_prefixed_state_dict`, `validate_phase1_checkpoint`, `checkpoint_summary`

## `src/dataset.py`

Local source: `/Users/joshua/Downloads/Phase4-main/src/dataset.py` (source files are not included in this documentation push).

Python module; see defined symbols and source.

**Top-level definitions/type:** `Phase4Dataset`, `build_tokenizer`

## `src/model.py`

Local source: `/Users/joshua/Downloads/Phase4-main/src/model.py` (source files are not included in this documentation push).

Python module; see defined symbols and source.

**Top-level definitions/type:** `Phase4Verifier`

## `src/pipeline_loader.py`

Local source: `/Users/joshua/Downloads/Phase4-main/src/pipeline_loader.py` (source files are not included in this documentation push).

Python module; see defined symbols and source.

**Top-level definitions/type:** `load_phase3_for_ablation`

## `src/trainer.py`

Local source: `/Users/joshua/Downloads/Phase4-main/src/trainer.py` (source files are not included in this documentation push).

Python module; see defined symbols and source.

**Top-level definitions/type:** `VerifierTrainer`

## `src/utils.py`

Local source: `/Users/joshua/Downloads/Phase4-main/src/utils.py` (source files are not included in this documentation push).

Python module; see defined symbols and source.

**Top-level definitions/type:** `set_seed`, `get_device`, `load_yaml`, `atomic_json_dump`, `count_parameters`
