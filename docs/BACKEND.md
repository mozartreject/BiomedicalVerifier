# Backend and API

Source: `~/Downloads/BiomedicalVerifier/backend`.

| File/module | Responsibility |
|---|---|
| `pipeline.py` | Five-stage lifecycle, invariants and persistence |
| `pipeline_config.py` | Typed configuration, environment paths and validation |
| `schemas.py` | Request, evidence, phase result and decision-package contracts |
| `adapters/` | Bridges to each phase and alternative verifier |
| `api/app.py` | FastAPI application |
| `api/dependencies.py` | Pipeline initialization and shared dependencies |
| `api/routes/inference.py` | Claim inference request handling |
| `api/routes/system.py` | System/health information |
| `services/persistence.py` | Decision package and audit persistence |
| `services/pubmed_search.py` | Optional live PubMed retrieval |

[Full application catalog](catalog/application.md) includes tests and diagnostic scripts.

The improved wrapper lives separately in `outputs/evidence-combiner/dashboard_backend.py`; it reuses the original pipeline with custom retrieval/verification adapters. Its health metadata identifies the passage-combiner mode. `test_dashboard.py` and `test_prediction_cache.py` cover important wrapper/cache behavior; documentation generation does not rerun these tests or start the server.

Primary routes used by the UI are `/api/v1/system/health` and `/api/v1/inferences`. Use the launcher's health check to confirm which backend is actually running. Two servers cannot bind the same localhost port simultaneously.
