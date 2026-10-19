# Evaluation and honest project status

Source of these recorded results: `outputs/clean-selector/REPORT.md`, inspected while writing this documentation. These are historical results, not a new evaluation run.

| Measurement | Earlier comparator | Supervised selector integration |
|---|---:|---:|
| Correct / 300 development claims | 197 | 201 |
| Accuracy | 65.7% | 67.0% |
| Macro-F1 | 0.6428 | 0.6503 |
| Annotated sentence recovered / 188 evidence-bearing claims | 110 | 120 |
| Complete annotated rationale / 188 | 104 | 113 |

Corpus: 35,183 documents. The reported split preparation excludes training document-connected groups that overlap development documents/text; the retained classifier training pool contains 531 claims. The development set has nevertheless been repeatedly reused to compare approaches.

The new confusion matrix uses true rows and predicted columns in REFUTED, NEI, SUPPORTED order:

```text
35 19 10
15 80 17
16 22 86
```

A four-case net improvement does not establish statistical significance. Refuted recall decreased in this comparison even though overall accuracy improved. Report per-class behavior rather than only the headline score.

## What this does not establish

- Independent held-out 75% or 80% accuracy.
- Reliable classification of every arbitrary biomedical claim.
- Medical-image interpretation quality or explanation factuality.
- Clinical calibration of displayed scores.

Expanded PubMed evidence can also make original SciFact NEI annotations incomplete. Evaluation should distinguish corpus coverage, retrieval, passage selection, verification and explanation failures. Preserve a genuinely untouched final test set, with independent review of any expanded-corpus labeling changes.
