# BiomedicalVerifier project documentation

Local documentation snapshot — 19 October 2026.

BiomedicalVerifier is a research capstone for classifying a biomedical claim as **REFUTED**, **NEI** (not enough evidence), or **SUPPORTED**, accompanied by retrieved evidence and a verdict-constrained explanation.

## Read in this order

1. [Architecture and execution modes](ARCHITECTURE.md)
2. [Phase 1 — representation](PHASE_1.md)
3. [Phase 2 — retrieval](PHASE_2.md)
4. [Phase 3 — evidence hierarchy](PHASE_3.md)
5. [Phase 4 — verification](PHASE_4.md)
6. [Phase 5 — explanation](PHASE_5.md)
7. [Backend and API](BACKEND.md)
8. [Dashboards](FRONTEND.md)
9. [Local startup and troubleshooting](RUNBOOK.md)
10. [Evaluation and research status](EVALUATION.md)
11. [Experiments and supporting scripts](EXPERIMENTS.md)
12. [Every cataloged source file](FILE_INDEX.md)

The file catalogs cover 477 source/configuration files across seven roots at generation time. They include historical experiments and backups, with extracted Python definitions where available. They are not assertions that every file is part of the serving path.

These Markdown files do not alter the application or publish a GitHub repository. Local source links require the existing folders on this machine. Dataset/model files remain external; this documentation is not a standalone software distribution.
