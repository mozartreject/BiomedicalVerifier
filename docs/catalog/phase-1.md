# phase-1: source file catalog

Source root: `/Users/joshua/Downloads/kaggle_upload`

Generated from local files. Inclusion does not imply a file is active, tested, or production-ready. Backups and historical experiments are included when present. Descriptions are module docstrings or structural summaries, not an audit of correctness.

## `config.yaml`

Local source: `/Users/joshua/Downloads/kaggle_upload/config.yaml` (source files are not included in this documentation push).

Configuration file; values are intentionally not copied into this catalog.

**Top-level definitions/type:** Configuration

## `src/config.py`

Local source: `/Users/joshua/Downloads/kaggle_upload/src/config.py` (source files are not included in this documentation push).

Configuration loader for Phase 1.

**Top-level definitions/type:** `DataConfig`, `ModelConfig`, `TrainingConfig`, `EvalConfig`, `SystemConfig`, `LoggingConfig`, `Config`, `load_config`

## `src/dataset.py`

Local source: `/Users/joshua/Downloads/kaggle_upload/src/dataset.py` (source files are not included in this documentation push).

Dataset classes for Phase 1 multimodal training.

**Top-level definitions/type:** `TripletDataset`, `BinaryMMDataset`, `TextOnlyDataset`, `ImageOnlyDataset`, `collate_fn_contrastive`, `collate_fn_binary`, `collate_fn_text_only`, `collate_fn_image_only`

## `src/losses.py`

Local source: `/Users/joshua/Downloads/kaggle_upload/src/losses.py` (source files are not included in this documentation push).

Loss functions for Phase 1.

**Top-level definitions/type:** `FocalLoss`, `ContrastiveLoss`, `InfoNCELoss`

## `src/models.py`

Local source: `/Users/joshua/Downloads/kaggle_upload/src/models.py` (source files are not included in this documentation push).

Model architectures for Phase 1 Multimodal Encoder.

**Top-level definitions/type:** `CrossAttentionFusion`, `BilinearFusion`, `ContrastiveFusion`, `TextOnlyClassifier`, `ImageOnlyClassifier`

## `src/train.py`

Local source: `/Users/joshua/Downloads/kaggle_upload/src/train.py` (source files are not included in this documentation push).

Phase 1 Training Script - UPDATED FOR MACRO-F1, CM PLOTS, AND RETRIEVAL.

**Top-level definitions/type:** `build_model`, `build_dataloaders`, `train_epoch_contrastive`, `validate_contrastive`, `train_epoch_binary`, `validate_binary`, `test_binary`, `evaluate_contrastive_retrieval`, `main`

## `src/transforms.py`

Local source: `/Users/joshua/Downloads/kaggle_upload/src/transforms.py` (source files are not included in this documentation push).

Image augmentation and preprocessing for Phase 1.

**Top-level definitions/type:** `get_train_transforms`, `get_val_transforms`

## `src/utils.py`

Local source: `/Users/joshua/Downloads/kaggle_upload/src/utils.py` (source files are not included in this documentation push).

Utility functions for Phase 1.

**Top-level definitions/type:** `set_seed`, `count_parameters`, `freeze_backbone`, `unfreeze_top_layers`, `compute_metrics`, `print_metrics`, `save_checkpoint`, `load_checkpoint`, `save_json`, `EarlyStopping`
