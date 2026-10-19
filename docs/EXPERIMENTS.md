# Experiments and supporting code

[Workspace catalog](catalog/workspace.md) lists source/configuration files and Python definitions throughout the workspace, including historical experiments.

## Main integration components

- `outputs/evidence-combiner`: candidate classifier, feature extraction, evaluation/training scripts, backend wrapper, tests and launchers.
- `outputs/clean-selector`: recorded selector integration report and model artifacts; model binaries are excluded from this catalog.
- `outputs/supervised-selector`: supervised sentence-selector training code.
- `outputs/selector-integration`: sentence extraction/selection helpers and experiments.
- `outputs/biomedical-verifier-blue`: current dashboard.
- `start_project.command`: combined local launcher entry point.

## Research alternatives

Folders include project-evaluation, corpus-connection, retrieval-improvement, passage-experiment, aggregation-experiment, advanced-evidence, deberta-verifier, verifier-adaptation, relation-adaptation, healthver-adaptation, multipassage, regression-audit and multivers-probe. Folder presence is not evidence of successful training, completed downloads or deployment. Inspect each run's report and artifact provenance before comparing it with the integrated classifier.

The medical-vision experiment folder is historical; the dedicated X-ray option is not part of the requested current dashboard. Third-party vendor code is excluded from this documentation catalog.

## Using the file catalogs

Every included file gets a source link and a structural summary. Python entries expose top-level function/class names parsed without importing or executing the module. A parsing warning identifies files the documentation interpreter could not parse. Notebook contents and outputs are deliberately not duplicated.

Catalog generation is reproducible with `documentation/build_catalog.py`. It is a documentation tool, not a test runner, dependency resolver or deployment script.
