# phase-3: source file catalog

Source root: `/Users/joshua/Downloads/Phase3-main`

Generated from local files. Inclusion does not imply a file is active, tested, or production-ready. Backups and historical experiments are included when present. Descriptions are module docstrings or structural summaries, not an audit of correctness.

## `ablation_study.py`

Local source: `/Users/joshua/Downloads/Phase3-main/ablation_study.py` (source files are not included in this documentation push).

Python module; see defined symbols and source.

**Top-level definitions/type:** `AblationError`, `EvidenceRecord`, `ClaimAudit`, `utc_now`, `normalize_text`, `ensure_finite`, `safe_float`, `sha256_file`, `atomic_json_write`, `atomic_text_write`, `load_json`, `average`, `percentage`, `extract_claim_text`, `load_phase2_claims`, `extract_phase3_claims`, `get_evidence_id`, `get_retrieval_score`, `get_hierarchy_tier`, `get_hierarchy_weight`, `canonicalize_evidence`, `record_to_dict`, `deduplicate_evidence`, `rank_records`, `ranking_map`, `tier_distribution`, `calculate_rank_displacement`, `calculate_topk_overlap`, `compare_top1_quality`, `analyze_claim`, `validate_claim_alignment`, `validate_phase3_evidence`, `deterministic_bootstrap_ci`, `aggregate_results`, `format_distribution`, `build_report`, `run_ablation`, `build_argument_parser`, `main`

## `analyze_phase3_taxonomy.py`

Local source: `/Users/joshua/Downloads/Phase3-main/analyze_phase3_taxonomy.py` (source files are not included in this documentation push).

Phase 3 — Taxonomy V2 Failure Analysis ====================================== Analyzes: 1. No-signal unique documents 2. Ambiguous unique documents 3. Cross-tier conflicts 4. High-confidence overrides 5. Old-tier coverag

**Top-level definitions/type:** `load`, `save`, `pct`, `safe_mean`, `safe_median`, `tokenize`, `useful_tokens`

## `analyze_v3_2_10_evaluator_score_mutation_provenance.py`

Local source: `/Users/joshua/Downloads/Phase3-main/analyze_v3_2_10_evaluator_score_mutation_provenance.py` (source files are not included in this documentation push).

Python module; see defined symbols and source.

**Top-level definitions/type:** `load_json`, `dump_json`, `safe_read`, `safe_unparse`, `node_line`, `node_end_line`, `normalize_number`, `should_skip`, `source_window`, `dotted_name`, `names_in_node`, `constants_in_node`, `contains_interest_field`, `build_parent_map`, `enclosing_function`, `enclosing_class`, `enclosing_conditions`, `candidate_score`, `print_special`

## `analyze_v3_2_5_compositional_candidates.py`

Local source: `/Users/joshua/Downloads/Phase3-main/analyze_v3_2_5_compositional_candidates.py` (source files are not included in this documentation push).

Python module; see defined symbols and source.

**Top-level definitions/type:** `load_json`, `unique_matches`

## `analyze_v3_2_7_rule_provenance_subtractive.py`

Local source: `/Users/joshua/Downloads/Phase3-main/analyze_v3_2_7_rule_provenance_subtractive.py` (source files are not included in this documentation push).

Python module; see defined symbols and source.

**Top-level definitions/type:** `load_json`, `dump_json`, `as_float`, `normalize_scores`, `baseline_state`, `confidence_proxy`, `classify_scores`, `tier_equal`, `first_present`, `normalize_tier`, `numeric_or_none`, `compact_text`, `extract_candidate_contributions`, `deduplicate_contributions`, `scoreful_contributions`, `reconstruct_scores`, `reconstruction_error`, `reconstruction_exact`

## `analyze_v3_2_8_score_accounting_forensics.py`

Local source: `/Users/joshua/Downloads/Phase3-main/analyze_v3_2_8_score_accounting_forensics.py` (source files are not included in this documentation push).

Python module; see defined symbols and source.

**Top-level definitions/type:** `load_json`, `dump_json`, `as_float`, `normalize_scores`, `close`, `safe_repr`, `walk_object`, `numeric_fields`, `extract_matches`, `raw_match_totals`, `candidate_cap`, `candidate_scale`, `candidate_subtraction`, `round_candidates`, `transformation_analysis`, `duplicate_analysis`, `find_numeric_explanations`

## `analyze_v3_2_9_context_transform_attribution.py`

Local source: `/Users/joshua/Downloads/Phase3-main/analyze_v3_2_9_context_transform_attribution.py` (source files are not included in this documentation push).

Python module; see defined symbols and source.

**Top-level definitions/type:** `load_json`, `dump_json`, `as_float`, `close`, `normalize_scores`, `extract_matches`, `raw_totals`, `score_delta`, `is_transformed`, `delta_signature`, `delta_signature_string`, `flatten_context`, `auxiliary_tokens`, `common_tokens`, `common_context_tokens`

## `audit_v3_2_2_recovery.py`

Local source: `/Users/joshua/Downloads/Phase3-main/audit_v3_2_2_recovery.py` (source files are not included in this documentation push).

Python module; see defined symbols and source.

**Top-level definitions/type:** `load_json`, `as_float`, `get_context`, `nearest_sentence`, `any_match`, `classify_scope`, `tier_correct`, `classified_correct`, `classified_wrong`, `risk_state`

## `audit_v3_2_input_integrity.py`

Local source: `/Users/joshua/Downloads/Phase3-main/audit_v3_2_input_integrity.py` (source files are not included in this documentation push).

Python module; see defined symbols and source.

**Top-level definitions/type:** No top-level functions/classes.

## `build_evaluation_set.py`

Local source: `/Users/joshua/Downloads/Phase3-main/build_evaluation_set.py` (source files are not included in this documentation push).

Build Phase 3 Evaluation Set from PubMed Downloads real abstracts with known study types (A/B/C/D).

**Top-level definitions/type:** `search_pmids`, `fetch_abstracts`, `build_evaluation_set`, `load_evaluation_set`

## `config.py`

Local source: `/Users/joshua/Downloads/Phase3-main/config.py` (source files are not included in this documentation push).

Phase 3 Configuration NO TRAINING. Just paths, tiers, and weights.

**Top-level definitions/type:** No top-level functions/classes.

## `counterfactual_recovery_audit_v3_2_2.py`

Local source: `/Users/joshua/Downloads/Phase3-main/counterfactual_recovery_audit_v3_2_2.py` (source files are not included in this documentation push).

Python module; see defined symbols and source.

**Top-level definitions/type:** `load_json`, `as_float`, `normalize_scores`, `exact_baseline_state`, `classify_from_scores`, `tier_equal`, `exact_state_equal`, `classified_correct`, `classified_wrong`, `weak_correct_tier`, `state_quality`, `impact_label`, `high_risk`

## `design_recovery_discovery_v3_2_2.py`

Local source: `/Users/joshua/Downloads/Phase3-main/design_recovery_discovery_v3_2_2.py` (source files are not included in this documentation push).

Python module; see defined symbols and source.

**Top-level definitions/type:** `extract_hits`, `existing_match_families`, `existing_match_concepts`, `already_detected`

## `diagnose_taxonomy_v3.py`

Local source: `/Users/joshua/Downloads/Phase3-main/diagnose_taxonomy_v3.py` (source files are not included in this documentation push).

Python module; see defined symbols and source.

**Top-level definitions/type:** No top-level functions/classes.

## `evaluate_healthfc.py`

Local source: `/Users/joshua/Downloads/Phase3-main/evaluate_healthfc.py` (source files are not included in this documentation push).

Evaluate evidence tier classifier against HealthFC ground truth. Maps T1/T2/T3/T4 citation types to A/B/C/D quality tiers for evaluation.

**Top-level definitions/type:** `download_healthfc`, `citation_to_tier`, `evaluate_classifier`

## `evaluate_phase3.py`

Local source: `/Users/joshua/Downloads/Phase3-main/evaluate_phase3.py` (source files are not included in this documentation push).

Python module; see defined symbols and source.

**Top-level definitions/type:** No top-level functions/classes.

## `evaluate_pubmed.py`

Local source: `/Users/joshua/Downloads/Phase3-main/evaluate_pubmed.py` (source files are not included in this documentation push).

Evaluate Phase 3 classifier on PubMed evaluation set. REAL ground truth: PubMed publication type filters.

**Top-level definitions/type:** `load_evaluation_set`, `evaluate_on_pubmed`, `evaluate_on_pubmed_llm`

## `evaluate_scifact.py`

Local source: `/Users/joshua/Downloads/Phase3-main/evaluate_scifact.py` (source files are not included in this documentation push).

Python module; see defined symbols and source.

**Top-level definitions/type:** `load_json`, `load_jsonl`, `atomic_write_json`, `atomic_write_text`, `sha256_file`, `normalize_doc_id`, `extract_claim_number`, `load_scifact_claims`, `load_phase2_claim_ids`, `load_phase3_claim_ids`, `main`

## `evaluate_taxonomy_v3.py`

Local source: `/Users/joshua/Downloads/Phase3-main/evaluate_taxonomy_v3.py` (source files are not included in this documentation push).

Python module; see defined symbols and source.

**Top-level definitions/type:** `load_json`, `save_json`, `sha256_file`, `pct`, `safe_float`, `claim_id`, `claim_text`, `evidence_list`, `document_identity`, `normalize_tier`, `result_to_dict`, `extract_claims`, `build_documents`, `main`

## `evaluate_taxonomy_v3_2.py`

Local source: `/Users/joshua/Downloads/Phase3-main/evaluate_taxonomy_v3_2.py` (source files are not included in this documentation push).

Python module; see defined symbols and source.

**Top-level definitions/type:** `get_text`

## `evaluate_taxonomy_v3_2_broken_title_only_backup.py`

Local source: `/Users/joshua/Downloads/Phase3-main/evaluate_taxonomy_v3_2_broken_title_only_backup.py` (source files are not included in this documentation push).

Python module; see defined symbols and source.

**Top-level definitions/type:** `get_text`

## `evaluate_v3_2_1_controlled.py`

Local source: `/Users/joshua/Downloads/Phase3-main/evaluate_v3_2_1_controlled.py` (source files are not included in this documentation push).

Python module; see defined symbols and source.

**Top-level definitions/type:** `old_tier`, `high_conf_disagreement`, `serialize_result`

## `evidence_classifier.py`

Local source: `/Users/joshua/Downloads/Phase3-main/evidence_classifier.py` (source files are not included in this documentation push).

Python module; see defined symbols and source.

**Top-level definitions/type:** `EvidenceClassifier`, `get_classifier`

## `evidence_taxonomy_v2.py`

Local source: `/Users/joshua/Downloads/Phase3-main/evidence_taxonomy_v2.py` (source files are not included in this documentation push).

Phase 3 — Evidence Hierarchy Taxonomy V2 ========================================= Research-grade study-design signal taxonomy. IMPORTANT: - This module does NOT replace the production classifier by itself. - It provides

**Top-level definitions/type:** `Match`, `RuleResult`, `normalize_text`, `EvidenceRuleEngine`, `taxonomy_statistics`, `self_test`

## `evidence_taxonomy_v3.py`

Local source: `/Users/joshua/Downloads/Phase3-main/evidence_taxonomy_v3.py` (source files are not included in this documentation push).

Phase 3 — Evidence Hierarchy Taxonomy V3 ========================================= Conservative research-grade study-design classifier. Hierarchy --------- A = Randomized trials / systematic reviews / meta-analyses B = O

**Top-level definitions/type:** `Match`, `RuleResult`, `normalize_text`, `EvidenceRuleEngine`, `taxonomy_statistics`, `self_test`

## `evidence_taxonomy_v3_1_backup.py`

Local source: `/Users/joshua/Downloads/Phase3-main/evidence_taxonomy_v3_1_backup.py` (source files are not included in this documentation push).

Phase 3 — Evidence Hierarchy Taxonomy V3 ========================================= Conservative research-grade study-design classifier. Hierarchy --------- A = Randomized trials / systematic reviews / meta-analyses B = O

**Top-level definitions/type:** `Match`, `RuleResult`, `normalize_text`, `EvidenceRuleEngine`, `taxonomy_statistics`, `self_test`

## `evidence_taxonomy_v3_2.py`

Local source: `/Users/joshua/Downloads/Phase3-main/evidence_taxonomy_v3_2.py` (source files are not included in this documentation push).

Phase 3 — Evidence Hierarchy Taxonomy V3.2 ========================================== Semantic-repair layer over V3.1. Goals: - preserve high-precision study-design signals - stop experimental modality from masquerading 

**Top-level definitions/type:** `canonical_signal`, `infer_family`, `EvidenceRuleEngine`, `self_test`

## `evidence_taxonomy_v3_2_before_3_2_1_fix.py`

Local source: `/Users/joshua/Downloads/Phase3-main/evidence_taxonomy_v3_2_before_3_2_1_fix.py` (source files are not included in this documentation push).

Phase 3 — Evidence Hierarchy Taxonomy V3.2 ========================================== Semantic-repair layer over V3.1. Goals: - preserve high-precision study-design signals - stop experimental modality from masquerading 

**Top-level definitions/type:** `canonical_signal`, `infer_family`, `EvidenceRuleEngine`, `self_test`

## `evidence_taxonomy_v3_2_before_api_fix.py`

Local source: `/Users/joshua/Downloads/Phase3-main/evidence_taxonomy_v3_2_before_api_fix.py` (source files are not included in this documentation push).

Phase 3 — Evidence Hierarchy Taxonomy V3.2 ========================================== Semantic-repair layer over V3.1. Goals: - preserve high-precision study-design signals - stop experimental modality from masquerading 

**Top-level definitions/type:** `canonical_signal`, `infer_family`, `EvidenceRuleEngine`, `self_test`

## `evidence_taxonomy_v3_pretest_backup.py`

Local source: `/Users/joshua/Downloads/Phase3-main/evidence_taxonomy_v3_pretest_backup.py` (source files are not included in this documentation push).

Phase 3 — Evidence Hierarchy Taxonomy V3 ========================================= Conservative research-grade study-design classifier. Hierarchy --------- A = Randomized trials / systematic reviews / meta-analyses B = O

**Top-level definitions/type:** `Match`, `RuleResult`, `normalize_text`, `EvidenceRuleEngine`, `taxonomy_statistics`, `self_test`

## `finalize_phase3.py`

Local source: `/Users/joshua/Downloads/Phase3-main/finalize_phase3.py` (source files are not included in this documentation push).

Phase 3 — Production Final Evidence Hierarchy Consolidation =========================================================== Goals ----- - Normalize Phase-3 JSON schemas safely. - Preserve claim IDs when claims are dict-keyed

**Top-level definitions/type:** `FinalizationConfig`, `utc_now`, `load_json`, `canonical_json_bytes`, `sha256_data`, `sha256_file`, `atomic_save_json`, `pct`, `finite_number`, `safe_float`, `normalize_tier`, `extract_claims`, `evidence_field_name`, `extract_evidence`, `claim_identifier`, `claim_text`, `normalized_document_text`, `evidence_identity`, `strongest_match_by_tier`, `evaluate_v2`, `make_decision`, `main`

## `forensic_audit_v3_2_1.py`

Local source: `/Users/joshua/Downloads/Phase3-main/forensic_audit_v3_2_1.py` (source files are not included in this documentation push).

Python module; see defined symbols and source.

**Top-level definitions/type:** `safe_float`, `normalized_match`, `matches`, `top_matches`, `result_is_decisive`, `high_conf`, `disagrees_reference`, `has_design_signal`, `strongest_design_signal`, `signal_signature`, `family_counter`, `concept_counter`, `tier_score`, `score_delta_by_tier`, `infer_change_reason`, `recovery_priority`

## `hierarchy_weights.py`

Local source: `/Users/joshua/Downloads/Phase3-main/hierarchy_weights.py` (source files are not included in this documentation push).

Python module; see defined symbols and source.

**Top-level definitions/type:** `get_weight`, `get_retrieval_score`, `calculate_weighted_score`, `rank_evidence`, `EvidenceWeighter`

## `llm_classifier.py`

Local source: `/Users/joshua/Downloads/Phase3-main/llm_classifier.py` (source files are not included in this documentation push).

LLM-based Evidence Tier Classifier using Ollama FINAL ATTEMPT: Ultra-strict system prompt + forced JSON output

**Top-level definitions/type:** `OllamaClassifier`, `get_llm_classifier`

## `mine_v3_2_4_recovery_candidates.py`

Local source: `/Users/joshua/Downloads/Phase3-main/mine_v3_2_4_recovery_candidates.py` (source files are not included in this documentation push).

Python module; see defined symbols and source.

**Top-level definitions/type:** `load_json`, `sentence_bounds`, `get_sentence`, `get_context`, `scope_guess`

## `ph.py`

Local source: `/Users/joshua/Downloads/Phase3-main/ph.py` (source files are not included in this documentation push).

Python module; see defined symbols and source.

**Top-level definitions/type:** No top-level functions/classes.

## `phase3_ablation.py`

Local source: `/Users/joshua/Downloads/Phase3-main/phase3_ablation.py` (source files are not included in this documentation push).

Python module; see defined symbols and source.

**Top-level definitions/type:** `normalize_id`, `get_gold_ids`, `get_evidence_id`, `score`, `weighted_score`, `rank`, `main`

## `phase3_build_v22_adjudication.py`

Local source: `/Users/joshua/Downloads/Phase3-main/phase3_build_v22_adjudication.py` (source files are not included in this documentation push).

Python module; see defined symbols and source.

**Top-level definitions/type:** `load`, `norm_id`, `evidence_id`, `truncate`, `signal_names`, `priority`, `reason`, `build_evidence_lookup`, `main`

## `phase3_classifier.py`

Local source: `/Users/joshua/Downloads/Phase3-main/phase3_classifier.py` (source files are not included in this documentation push).

Python module; see defined symbols and source.

**Top-level definitions/type:** `to_float`, `rank_evidence`, `main`

## `phase3_final_freeze.py`

Local source: `/Users/joshua/Downloads/Phase3-main/phase3_final_freeze.py` (source files are not included in this documentation push).

Python module; see defined symbols and source.

**Top-level definitions/type:** `banner`, `section`, `now_iso`, `norm_tier`, `json_safe`, `write_json`, `sha256_file`, `file_metadata`, `find_input`, `score_dict`, `parse_python`, `extract_engine_version`, `extract_constructor_defaults`, `source_audit`, `replay_v32_decision`, `parity_audit`, `confusion_matrix`, `safe_div`, `classification_metrics`, `error_forensics`, `transformation_audit`, `score_distribution_audit`, `zero_delta_proof`, `dataset_integrity`, `evaluate_freeze_gates`, `make_markdown_report`, `main`

## `phase3_healthfc.py`

Local source: `/Users/joshua/Downloads/Phase3-main/phase3_healthfc.py` (source files are not included in this documentation push).

Python module; see defined symbols and source.

**Top-level definitions/type:** `map_healthfc_tier`, `heuristic_source_classification`, `main`

## `phase3_taxonomy_v21_master.py`

Local source: `/Users/joshua/Downloads/Phase3-main/phase3_taxonomy_v21_master.py` (source files are not included in this documentation push).

PHASE 3 — TAXONOMY V2.1 MASTER SHADOW AUDIT =========================================== One-shot diagnostic covering: 1. Production vs V2 comparison 2. Zero-signal handling (UNRESOLVED instead of accidental A) 3. Semanti

**Top-level definitions/type:** `load_json`, `safe_pct`, `mean`, `median`, `evidence_identity`, `normalize_signal`, `deduplicate_matches`, `recompute_scores`, `ranked_scores`, `winner`, `remove_suspicious`, `definitive_tiers`, `signal_tiers`, `heuristic_confidence`, `v21_decision`, `classify_error_bucket`, `csv_value`, `write_csv`, `main`

## `phase3_v221_adjudicator_consistency_audit.py`

Local source: `/Users/joshua/Downloads/Phase3-main/phase3_v221_adjudicator_consistency_audit.py` (source files are not included in this documentation push).

Python module; see defined symbols and source.

**Top-level definitions/type:** `load_json`, `save_json`, `safe_pct`, `norm_text`, `csv_value`, `write_csv`, `map_design_text`, `boolean_expected_tiers`, `audit_internal_logic`, `deterministic_tier`, `review_priority`, `main`

## `phase3_v22_blind_adjudicator.py`

Local source: `/Users/joshua/Downloads/Phase3-main/phase3_v22_blind_adjudicator.py` (source files are not included in this documentation push).

Python module; see defined symbols and source.

**Top-level definitions/type:** `load_json`, `save_json`, `safe_pct`, `normalize_bool`, `extract_json`, `validate_result`, `ollama_generate`, `classify_document`, `csv_value`, `write_csv`, `main`

## `phase3_v231_forensic_error_analysis.py`

Local source: `/Users/joshua/Downloads/Phase3-main/phase3_v231_forensic_error_analysis.py` (source files are not included in this documentation push).

Python module; see defined symbols and source.

**Top-level definitions/type:** `load_json`, `save_json`, `safe_pct`, `csv_value`, `write_csv`, `true_flags`, `changed_flags`, `tier_trigger`, `contradiction_flags`, `main`

## `phase3_v232_evidence_grounding_audit.py`

Local source: `/Users/joshua/Downloads/Phase3-main/phase3_v232_evidence_grounding_audit.py` (source files are not included in this documentation push).

Python module; see defined symbols and source.

**Top-level definitions/type:** `load_json`, `save_json`, `write_csv`, `safe_pct`, `norm`, `tokens`, `exact_phrase_present`, `token_coverage`, `best_fuzzy_ratio`, `evidence_grounded`, `pattern_hits`, `trigger`, `classify_grounding`, `main`

## `phase3_v233_ownership_entailment_audit.py`

Local source: `/Users/joshua/Downloads/Phase3-main/phase3_v233_ownership_entailment_audit.py` (source files are not included in this documentation push).

Python module; see defined symbols and source.

**Top-level definitions/type:** `load_json`, `save_json`, `safe_pct`, `csv_value`, `write_csv`, `extract_json`, `generate`, `call_json`, `normalize_status`, `normalize_field`, `normalize_output`, `norm_text`, `evidence_is_grounded`, `supported`, `owned_signal_map`, `detect_contradictions`, `derive_strict_tier`, `choose_targets`, `run_audit`, `audit_field_evidence`, `review_priority`, `main`

## `phase3_v234_blind_phenotype_reverse_engineering.py`

Local source: `/Users/joshua/Downloads/Phase3-main/phase3_v234_blind_phenotype_reverse_engineering.py` (source files are not included in this documentation push).

Python module; see defined symbols and source.

**Top-level definitions/type:** `load_json`, `save_json`, `csv_value`, `write_csv`, `extract_json`, `generate`, `call_json`, `clamp`, `normalize`, `entropy`, `mutual_information_binary`, `categorical_mutual_information`, `main`

## `phase3_v235_taxonomy_reconstruction_audit.py`

Local source: `/Users/joshua/Downloads/Phase3-main/phase3_v235_taxonomy_reconstruction_audit.py` (source files are not included in this documentation push).

Python module; see defined symbols and source.

**Top-level definitions/type:** `load_json`, `save_json`, `write_csv`, `mean`, `std`, `percentile`, `ci95`, `safe_float`, `prepare_rows`, `make_matrix`, `dicts_to_columns`, `DictFrame`, `to_dataframe`, `make_logistic`, `make_rf`, `metrics`, `majority_baseline`, `stratified_repeated_cv`, `summarize_repeated_cv`, `consensus_predictions`, `leave_one_out`, `permutation_test`, `confusion_rows`, `class_recall`, `feature_stability`, `error_audit`, `main`

## `phase3_v23_dualpass_diagnostic.py`

Local source: `/Users/joshua/Downloads/Phase3-main/phase3_v23_dualpass_diagnostic.py` (source files are not included in this documentation push).

Python module; see defined symbols and source.

**Top-level definitions/type:** `load_json`, `save_json`, `safe_pct`, `normalize_bool`, `extract_json`, `generate`, `call_json`, `normalize_extraction`, `derive_tier`, `choose_diagnostic_sample`, `run_pass1`, `run_pass2`, `main`

## `phase3_v240_taxonomy_label_origin_audit.BACKUP.py`

Local source: `/Users/joshua/Downloads/Phase3-main/phase3_v240_taxonomy_label_origin_audit.BACKUP.py` (source files are not included in this documentation push).

Python module; see defined symbols and source.

**Top-level definitions/type:** `load_json`, `save_json`, `write_csv`, `mean`, `std`, `percentile`, `ci95`, `safe_float`, `metrics`, `class_recall`, `entropy`, `prepare_rows`, `phenotype_signature`, `build_signature_audit`, `label_transition_audit`, `make_preprocessor`, `dataframe`, `phenotype_distance`, `pairwise_distance_audit`, `nearest_neighbor_audit`, `rare_class_autopsy`, `contradiction_audit`, `make_logistic`, `make_tree`, `repeated_oof_predictions`, `shallow_tree_audit`, `loo_logistic_audit`, `matched_permutation_test`, `local_label_consistency`, `decision_gate`, `build_report`, `main`

## `phase3_v240_taxonomy_label_origin_audit.py`

Local source: `/Users/joshua/Downloads/Phase3-main/phase3_v240_taxonomy_label_origin_audit.py` (source files are not included in this documentation push).

Python module; see defined symbols and source.

**Top-level definitions/type:** `load_json`, `save_json`, `write_csv`, `mean`, `std`, `percentile`, `ci95`, `safe_float`, `metrics`, `class_recall`, `entropy`, `prepare_rows`, `phenotype_signature`, `build_signature_audit`, `label_transition_audit`, `make_preprocessor`, `dataframe`, `phenotype_distance`, `pairwise_distance_audit`, `nearest_neighbor_audit`, `rare_class_autopsy`, `contradiction_audit`, `make_logistic`, `make_tree`, `repeated_oof_predictions`, `shallow_tree_audit`, `loo_logistic_audit`, `matched_permutation_test`, `local_label_consistency`, `decision_gate`, `build_report`, `main`

## `phase3_v250_provenance_forensics.py`

Local source: `/Users/joshua/Downloads/Phase3-main/phase3_v250_provenance_forensics.py` (source files are not included in this documentation push).

Python module; see defined symbols and source.

**Top-level definitions/type:** `require`, `entropy`, `conditional_entropy`, `cramers_v`, `bootstrap_mean_ci`, `safe_bool`, `classification_metrics`, `make_encoder`, `provenance_flag`

## `phase3_v251_label_lineage_reconstruction.py`

Local source: `/Users/joshua/Downloads/Phase3-main/phase3_v251_label_lineage_reconstruction.py` (source files are not included in this documentation push).

Python module; see defined symbols and source.

**Top-level definitions/type:** `unique_nonmissing`, `earliest_production`, `same`

## `phase3_v260_production_candidate.py`

Local source: `/Users/joshua/Downloads/Phase3-main/phase3_v260_production_candidate.py` (source files are not included in this documentation push).

Python module; see defined symbols and source.

**Top-level definitions/type:** `load_json`, `save_json`, `evidence_key`, `extract_text`, `get_claims`, `get_retrieval_score`, `parse_json_object`, `ollama_generate`, `call_json`, `check_ollama`, `normalize_bool`, `normalize_list`, `normalize_extraction`, `run_pass1`, `run_pass2`, `map_verified_to_tier`, `load_v260_cache`, `classify_document`, `collect_unique_evidence`, `build_new_classified`, `rank_claim`, `build_weighted_output`, `validate_artifact`, `unique_rows_by_eid`, `distribution`, `transition_matrix`, `top1_map`, `compare_rankings`, `main`

## `phase3_v2611_evidence_grounding.py`

Local source: `/Users/joshua/Downloads/Phase3-main/phase3_v2611_evidence_grounding.py` (source files are not included in this documentation push).

Python module; see defined symbols and source.

**Top-level definitions/type:** `load_json`, `save_json`, `normalize`, `match_patterns`, `context_window`, `contextualize`, `first_sentence_like`, `extract_claims`, `build_registry`, `infer_grounded_signals`, `audit_row`, `risk_score`, `main`

## `phase3_v261_forensic_validation.py`

Local source: `/Users/joshua/Downloads/Phase3-main/phase3_v261_forensic_validation.py` (source files are not included in this documentation push).

Python module; see defined symbols and source.

**Top-level definitions/type:** `load_json`, `save_json`, `get_claims`, `evidence_key`, `normalize_text`, `hits`, `has_any`, `add_flag`, `inspect_document`, `deduplicate_rows`, `risk_sort_key`, `create_annotation_record`, `build_gold_queue`, `main`

## `phase3_v262_blinded_gold_benchmark.py`

Local source: `/Users/joshua/Downloads/Phase3-main/phase3_v262_blinded_gold_benchmark.py` (source files are not included in this documentation push).

PHASE 3 V2.6.2 BLINDED GOLD ANNOTATION + PAIRED LEGACY-vs-V260 BENCHMARK PURPOSE ------- 1. Freeze V260 predictions. 2. Build a blinded annotation dataset from V2611 grounded review queue. 3. Prevent prediction/forensic 

**Top-level definitions/type:** `now_utc`, `load_json`, `save_json`, `normalize`, `sha256_text`, `safe_float`, `safe_int`, `mean`, `percentile`, `ci95`, `first_nonempty`, `extract_registry`, `extract_v260_predictions`, `canonical_prediction`, `determine_stratum`, `build_annotation_packet`, `build_sealed_predictions`, `recursive_key_scan`, `audit_packet_leakage`, `write_annotation_csv`, `normalize_bool`, `annotation_completion`, `validate_gold`, `confusion_matrix`, `class_metrics`, `aggregate_metrics`, `weighted_kappa`, `tier_mae`, `catastrophic_tier_error_rate`, `binomial_coefficient`, `mcnemar_exact`, `bootstrap_paired_accuracy_difference`, `bootstrap_macro_f1_difference`, `benchmark`, `build_error_analysis`, `write_disagreement_csv`, `pct`, `fmt`, `write_codebook_txt`, `benchmark_text`, `build_sampling_manifest`, `load_annotation_packet`, `merge_existing_annotations`, `main`

## `phase3_v270_build_expanded_lexicon.py`

Local source: `/Users/joshua/Downloads/Phase3-main/phase3_v270_build_expanded_lexicon.py` (source files are not included in this documentation push).

PHASE 3 V2.7.0 STRUCTURED ~1000-ENTRY STUDY-DESIGN LEXICON BUILDER PURPOSE ------- 1. Create a large structured lexical-signal inventory for Phase 3. 2. Preserve V260/V261/V2611/V262 completely unchanged. 3. Separate: - 

**Top-level definitions/type:** `now_utc`, `norm`, `slug`, `save_json`, `sha256_obj`, `phrase_variants`, `weight_for`, `signal_type_for`, `build_lexicon`, `audit_lexicon`, `main`

## `phase3_v270_contextual_classifier.py`

Local source: `/Users/joshua/Downloads/Phase3-main/phase3_v270_contextual_classifier.py` (source files are not included in this documentation push).

PHASE 3 V2.7.0 — STAGE 2B CONTEXTUAL LEXICAL STUDY-DESIGN CLASSIFIER READ-ONLY INPUTS ---------------- data/phase3_v2611/v2611_canonical_evidence_registry.json data/phase3_v260/v260_evidence_audit.json data/phase3_v270/v

**Top-level definitions/type:** `now_utc`, `load_json`, `save_json`, `sha256_obj`, `normalize_text`, `compile_term`, `context_window`, `load_v260_unique`, `prepare_lexicon`, `find_matches`, `collapse_matches`, `raw_family_scores`, `get_family_signals`, `contains_source`, `resolve_context`, `rank_scores`, `classify`, `top_signal_summary`, `main`

## `phase3_v3211_all_in_one_score_forensics.py`

Local source: `/Users/joshua/Downloads/Phase3-main/phase3_v3211_all_in_one_score_forensics.py` (source files are not included in this documentation push).

Python module; see defined symbols and source.

**Top-level definitions/type:** `utc_now`, `safe_float`, `sha256_file`, `sha256_text`, `json_dump`, `csv_dump`, `rel`, `print_header`, `normalize_scores`, `score_delta`, `ranked_scores`, `decision_from_scores`, `iter_python_files`, `prioritized_files`, `Mutation`, `Analyzer`, `analyze_source`, `source_window`, `infer_execution_stages`, `transformation_requirements`, `mutation_matches_target`, `rank_mutations_for_targets`, `simulate_add_b`, `counterfactual_grid`, `first_b_recovery`, `discover_guards`, `normalized_code_hash`, `version_drift`, `snapshot`, `compare_snapshots`, `render_target_table`, `render_top_mutations`, `render_execution_order`, `render_target_candidates`, `render_recovery`, `main`

## `phase3_v3212_all_in_one_controlled_intervention.py`

Local source: `/Users/joshua/Downloads/Phase3-main/phase3_v3212_all_in_one_controlled_intervention.py` (source files are not included in this documentation push).

Python module; see defined symbols and source.

**Top-level definitions/type:** `now`, `sha256`, `load_json`, `dump_json`, `objdict`, `normalize_tier`, `score_dict`, `decide`, `load_classifier_module`, `instantiate_engine`, `call_classifier`, `extract_scores`, `extract_prediction`, `confusion_matrix`, `accuracy`, `macro_f1`, `apply_b_delta`, `benchmark_counterfactual`, `main`

## `phase3_v3214_conflict_quarantine_final.py`

Local source: `/Users/joshua/Downloads/Phase3-main/phase3_v3214_conflict_quarantine_final.py` (source files are not included in this documentation push).

Python module; see defined symbols and source.

**Top-level definitions/type:** `banner`, `section`, `now`, `norm`, `score_dict`, `sha256`, `write_json`, `safe_div`, `replay_prediction`, `discover_pmid_conflicts`, `build_quarantine`, `integrity_audit`, `metrics`, `error_ledger`, `quarantine_analysis`, `transformation_check`, `metric_comparison`, `write_error_csv`, `markdown_report`, `main`

## `phase4_readiness_audit.py`

Local source: `/Users/joshua/Downloads/Phase3-main/phase4_readiness_audit.py` (source files are not included in this documentation push).

Python module; see defined symbols and source.

**Top-level definitions/type:** `banner`, `section`, `allowed`, `sha256`, `rel`, `inspect_json`, `inspect_csv`

## `phase4_v001_label_schema_audit.py`

Local source: `/Users/joshua/Downloads/Phase3-main/phase4_v001_label_schema_audit.py` (source files are not included in this documentation push).

Python module; see defined symbols and source.

**Top-level definitions/type:** `banner`, `section`, `sha256`, `load_jsonl`, `load_csv`, `recursive_keys`, `recursive_scalar_values`, `print_counter`, `norm_text`

## `phase4_v002_label_resolution.py`

Local source: `/Users/joshua/Downloads/Phase3-main/phase4_v002_label_resolution.py` (source files are not included in this documentation push).

Python module; see defined symbols and source.

**Top-level definitions/type:** `banner`, `section`, `rel`, `allowed`, `sha256`, `load_jsonl`, `load_csv`, `norm_text`, `unique_nonempty`, `get_scifact_labels`, `scifact_claim_state`, `context_lines`

## `phase4_v003_canonical_builder.py`

Local source: `/Users/joshua/Downloads/Phase3-main/phase4_v003_canonical_builder.py` (source files are not included in this documentation push).

Python module; see defined symbols and source.

**Top-level definitions/type:** `banner`, `section`, `sha256`, `load_jsonl`, `load_csv`, `norm_text`, `text_hash`, `safe_str`, `utc_now`, `write_json`, `write_jsonl`, `write_csv`, `collect_scifact_evidence_labels`, `get_doc_sentences`, `reconstruct_gold_evidence`, `extract_phase2_evidence_texts`, `phase2_key_for_claim`, `make_scifact_row`, `token_proxy`, `percentile`

## `phase4_v004_scifact_nei_candidate_builder.py`

Local source: `/Users/joshua/Downloads/Phase3-main/phase4_v004_scifact_nei_candidate_builder.py` (source files are not included in this documentation push).

Python module; see defined symbols and source.

**Top-level definitions/type:** `banner`, `section`, `utc_now`, `safe_str`, `norm_text`, `sha256`, `text_hash`, `load_jsonl`, `write_json`, `write_jsonl`, `tokenize`, `lexical_set`, `jaccard`, `containment`, `overlap_count`, `percentile`, `bm25_idf`, `retrieve_bm25`, `candidate_similarity`, `mmr_select`, `print_distribution`

## `phase4_v004a_scifact_nei_candidate_builder.py`

Local source: `/Users/joshua/Downloads/Phase3-main/phase4_v004a_scifact_nei_candidate_builder.py` (source files are not included in this documentation push).

Python module; see defined symbols and source.

**Top-level definitions/type:** `banner`, `section`, `utc_now`, `safe_str`, `norm_text`, `sha256`, `text_hash`, `load_jsonl`, `write_json`, `write_jsonl`, `tokenize`, `lexical_set`, `jaccard`, `containment`, `overlap_count`, `percentile`, `bm25_idf`, `retrieve_bm25`, `candidate_similarity`, `mmr_select`, `print_distribution`

## `phase4_v004b_scifact_nei_candidate_builder.py`

Local source: `/Users/joshua/Downloads/Phase3-main/phase4_v004b_scifact_nei_candidate_builder.py` (source files are not included in this documentation push).

Python module; see defined symbols and source.

**Top-level definitions/type:** `banner`, `section`, `utc_now`, `safe_str`, `norm_text`, `sha256`, `text_hash`, `load_jsonl`, `write_json`, `write_jsonl`, `tokenize`, `lexical_set`, `jaccard`, `containment`, `overlap_count`, `percentile`, `bm25_idf`, `retrieve_bm25`, `candidate_similarity`, `mmr_select`, `print_distribution`

## `phase4_v005_nei_semantic_screener.py`

Local source: `/Users/joshua/Downloads/Phase3-main/phase4_v005_nei_semantic_screener.py` (source files are not included in this documentation push).

Python module; see defined symbols and source.

**Top-level definitions/type:** `banner`, `section`, `utc_now`, `safe_str`, `norm_text`, `tokenize`, `lexical_set`, `sha256`, `text_hash`, `load_jsonl`, `write_json`, `write_jsonl`, `jaccard`, `containment`, `percentile`, `polarity_features`, `risk_priority`

## `phase4_v006_nei_adjudication_builder.py`

Local source: `/Users/joshua/Downloads/Phase3-main/phase4_v006_nei_adjudication_builder.py` (source files are not included in this documentation push).

Python module; see defined symbols and source.

**Top-level definitions/type:** `section`, `banner`, `utc_now`, `sha256`, `load_jsonl`, `write_json`, `write_jsonl`, `deterministic_review_id`

## `phase4_v007_semantic_adjudicator_calibration.py`

Local source: `/Users/joshua/Downloads/Phase3-main/phase4_v007_semantic_adjudicator_calibration.py` (source files are not included in this documentation push).

Python module; see defined symbols and source.

**Top-level definitions/type:** `banner`, `section`, `utc_now`, `safe_str`, `norm_text`, `text_hash`, `sha256`, `load_jsonl`, `write_json`, `write_jsonl`, `canonical_label`, `fold_cost`

## `phase4_v007_semantic_adjudicator_calibration_original.py`

Local source: `/Users/joshua/Downloads/Phase3-main/phase4_v007_semantic_adjudicator_calibration_original.py` (source files are not included in this documentation push).

Python module; see defined symbols and source.

**Top-level definitions/type:** `banner`, `section`, `utc_now`, `safe_str`, `norm_text`, `text_hash`, `sha256`, `load_jsonl`, `write_json`, `write_jsonl`, `canonical_label`, `fold_cost`

## `phase4_v007a_semantic_adjudicator_calibration.py`

Local source: `/Users/joshua/Downloads/Phase3-main/phase4_v007a_semantic_adjudicator_calibration.py` (source files are not included in this documentation push).

Python module; see defined symbols and source.

**Top-level definitions/type:** `banner`, `section`, `utc_now`, `safe_str`, `norm_text`, `text_hash`, `sha256`, `load_jsonl`, `write_json`, `write_jsonl`, `canonical_label`, `uf_add`, `uf_find`, `uf_union`, `normalized_squared_error`, `global_assignment_cost`

## `phase4_v008_semantic_adjudicator_cv.py`

Local source: `/Users/joshua/Downloads/Phase3-main/phase4_v008_semantic_adjudicator_cv.py` (source files are not included in this documentation push).

Python module; see defined symbols and source.

**Top-level definitions/type:** `banner`, `section`, `utc_now`, `sha256`, `load_jsonl`, `write_json`, `write_jsonl`, `stable_pair_id`, `softmax_np`, `binary_brier`, `expected_calibration_error`, `metric_bundle`, `bootstrap_ci`, `binary_label_id`, `PairDataset`, `fit_temperature`, `find_class_threshold`, `selective_predictions`

## `phase4_v008_semantic_adjudicator_cv_original.py`

Local source: `/Users/joshua/Downloads/Phase3-main/phase4_v008_semantic_adjudicator_cv_original.py` (source files are not included in this documentation push).

Python module; see defined symbols and source.

**Top-level definitions/type:** `banner`, `section`, `utc_now`, `sha256`, `load_jsonl`, `write_json`, `write_jsonl`, `stable_pair_id`, `softmax_np`, `binary_brier`, `expected_calibration_error`, `metric_bundle`, `bootstrap_ci`, `PairDataset`, `fit_temperature`, `find_class_threshold`, `selective_predictions`

## `phase4_v008_semantic_adjudicator_cv_pre_binary_label_fix.py`

Local source: `/Users/joshua/Downloads/Phase3-main/phase4_v008_semantic_adjudicator_cv_pre_binary_label_fix.py` (source files are not included in this documentation push).

Python module; see defined symbols and source.

**Top-level definitions/type:** `banner`, `section`, `utc_now`, `sha256`, `load_jsonl`, `write_json`, `write_jsonl`, `stable_pair_id`, `softmax_np`, `binary_brier`, `expected_calibration_error`, `metric_bundle`, `bootstrap_ci`, `PairDataset`, `fit_temperature`, `find_class_threshold`, `selective_predictions`

## `phase4_v009_preflight.py`

Local source: `/Users/joshua/Downloads/Phase3-main/phase4_v009_preflight.py` (source files are not included in this documentation push).

Python module; see defined symbols and source.

**Top-level definitions/type:** `banner`, `section`, `sha256`, `load_json`, `load_jsonl`, `write_json`, `fail`

## `phase4_v009_preflight_original.py`

Local source: `/Users/joshua/Downloads/Phase3-main/phase4_v009_preflight_original.py` (source files are not included in this documentation push).

Python module; see defined symbols and source.

**Top-level definitions/type:** `banner`, `section`, `sha256`, `load_json`, `load_jsonl`, `write_json`, `fail`

## `phase4_v009b_threshold_robustness.py`

Local source: `/Users/joshua/Downloads/Phase3-main/phase4_v009b_threshold_robustness.py` (source files are not included in this documentation push).

Python module; see defined symbols and source.

**Top-level definitions/type:** `banner`, `section`, `sha256`, `load_json`, `load_jsonl`, `write_json`, `write_jsonl`, `fail`, `class_stats`, `percentile_interval`, `bootstrap_precision`, `find_lowest_threshold`, `fold_safe_frontier`

## `phase4_v009c_fold_diagnostics.py`

Local source: `/Users/joshua/Downloads/Phase3-main/phase4_v009c_fold_diagnostics.py` (source files are not included in this documentation push).

Python module; see defined symbols and source.

**Top-level definitions/type:** `banner`, `section`, `load_json`, `load_jsonl`, `write_json`, `sha256`, `percentile_summary`, `accuracy`, `binary_metrics`

## `phase4_v009d_raw_score_audit.py`

Local source: `/Users/joshua/Downloads/Phase3-main/phase4_v009d_raw_score_audit.py` (source files are not included in this documentation push).

Python module; see defined symbols and source.

**Top-level definitions/type:** `banner`, `section`, `load_json`, `load_jsonl`, `write_json`, `sha256`, `summary`, `softmax_binary`, `balanced_accuracy`, `collect_temperature`

## `phase4_v009e_split_training_audit.py`

Local source: `/Users/joshua/Downloads/Phase3-main/phase4_v009e_split_training_audit.py` (source files are not included in this documentation push).

Python module; see defined symbols and source.

**Top-level definitions/type:** `banner`, `section`, `load_json`, `load_jsonl`, `write_json`, `sha256`, `numeric_summary`, `safe_len_text`, `find_first`, `normalize_json`

## `phase4_v009f_fold3_seed_sensitivity.py`

Local source: `/Users/joshua/Downloads/Phase3-main/phase4_v009f_fold3_seed_sensitivity.py` (source files are not included in this documentation push).

Python module; see defined symbols and source.

**Top-level definitions/type:** `banner`, `section`, `load_json`, `load_jsonl`, `write_json`, `sha256`, `softmax_np`, `numeric_summary`, `binary_label_id`, `PairDataset`

## `phase4_v009g_fold3_prediction_stability.py`

Local source: `/Users/joshua/Downloads/Phase3-main/phase4_v009g_fold3_prediction_stability.py` (source files are not included in this documentation push).

Python module; see defined symbols and source.

**Top-level definitions/type:** `banner`, `section`, `load_json`, `load_jsonl`, `write_json`, `write_jsonl`, `sha256`, `numeric_summary`, `prediction_entropy`, `stability_category`, `stable_identifier`

## `phase4_v009h_contradict_semantic_phenotypes.py`

Local source: `/Users/joshua/Downloads/Phase3-main/phase4_v009h_contradict_semantic_phenotypes.py` (source files are not included in this documentation push).

Python module; see defined symbols and source.

**Top-level definitions/type:** `banner`, `section`, `load_json`, `load_jsonl`, `write_json`, `write_jsonl`, `sha256`, `numeric_summary`, `safe_divide`, `tokenize`, `lexical_overlap`, `jaccard_overlap`, `detect_phenotypes`, `cohort_name`, `phenotype_presence`

## `phase4_v009i_contradict_margin_audit.py`

Local source: `/Users/joshua/Downloads/Phase3-main/phase4_v009i_contradict_margin_audit.py` (source files are not included in this documentation push).

Python module; see defined symbols and source.

**Top-level definitions/type:** `banner`, `section`, `load_json`, `load_jsonl`, `write_json`, `write_jsonl`, `sha256`, `safe_divide`, `numeric_summary`, `signed_margin`, `phenotype_present`, `mean_or_none`

## `phase4_v009j_training_dynamics_audit.py`

Local source: `/Users/joshua/Downloads/Phase3-main/phase4_v009j_training_dynamics_audit.py` (source files are not included in this documentation push).

Python module; see defined symbols and source.

**Top-level definitions/type:** `banner`, `section`, `load_json`, `write_json`, `sha256`, `summary`, `pct_change`

## `rebuild_v3_2_corpus.py`

Local source: `/Users/joshua/Downloads/Phase3-main/rebuild_v3_2_corpus.py` (source files are not included in this documentation push).

Python module; see defined symbols and source.

**Top-level definitions/type:** `norm_id`, `first_string`, `sha256_text`, `recursively_find_strings`, `recursively_find_ids`

## `run_phase3.py`

Local source: `/Users/joshua/Downloads/Phase3-main/run_phase3.py` (source files are not included in this documentation push).

Python module; see defined symbols and source.

**Top-level definitions/type:** `load_json`, `save_json`, `load_phase2_evidence`, `get_evidence_key`, `collect_unique_evidence`, `run_classification`, `build_classified_claims`, `create_classified_output`, `get_retrieval_score`, `get_hierarchy_weight`, `rank_evidence`, `create_ranking_outputs`, `validate_results`, `main`

## `simulate_v3_2_2_recovery.py`

Local source: `/Users/joshua/Downloads/Phase3-main/simulate_v3_2_2_recovery.py` (source files are not included in this documentation push).

Python module; see defined symbols and source.

**Top-level definitions/type:** `f`, `find_rule_matches`, `existing_concepts`, `semantically_already_present`, `confidence_from_margin`, `shadow_classify`, `disagreement`, `high_risk_shadow`

## `simulate_v3_2_3_guarded_recovery.py`

Local source: `/Users/joshua/Downloads/Phase3-main/simulate_v3_2_3_guarded_recovery.py` (source files are not included in this documentation push).

Python module; see defined symbols and source.

**Top-level definitions/type:** `load_json`, `as_float`, `normalize_scores`, `baseline_state`, `tier_equal`, `classified_correct`, `classified_wrong`, `weak_correct`, `state_quality`, `confidence_proxy`, `classify_scores`, `high_risk`

## `simulate_v3_2_6_compositional_counterfactual.py`

Local source: `/Users/joshua/Downloads/Phase3-main/simulate_v3_2_6_compositional_counterfactual.py` (source files are not included in this documentation push).

Python module; see defined symbols and source.

**Top-level definitions/type:** `load_json`, `as_float`, `normalize_scores`, `baseline_state`, `tier_equal`, `confidence_proxy`, `classify_scores`, `classified_correct`, `classified_wrong`, `weak_correct`, `state_quality`, `high_risk`

## `test_llm.py`

Local source: `/Users/joshua/Downloads/Phase3-main/test_llm.py` (source files are not included in this documentation push).

Balanced test: 12-13 samples from each tier (A/B/C/D) = ~50 total This gives a FAIR F1 score.

**Top-level definitions/type:** `test_llm_balanced`

## `test_taxonomy_v2.py`

Local source: `/Users/joshua/Downloads/Phase3-main/test_taxonomy_v2.py` (source files are not included in this documentation push).

Standalone diagnostic for Phase 3 Evidence Taxonomy V2. Does NOT modify existing Phase 3 outputs.

**Top-level definitions/type:** `find_input`, `extract_claims`, `extract_evidence`, `main`

## `test_taxonomy_v2_real.py`

Local source: `/Users/joshua/Downloads/Phase3-main/test_taxonomy_v2_real.py` (source files are not included in this documentation push).

Phase 3 — Taxonomy V2 Real-Data Shadow Evaluation ================================================== READ-ONLY diagnostic. Does NOT: - modify hierarchy_classified.json - modify config.py - modify evidence_classifier.py -

**Top-level definitions/type:** `load_json`, `pct`, `get_claims`, `evidence_identity`, `strongest_match_by_tier`, `semantic_signature`, `main`
