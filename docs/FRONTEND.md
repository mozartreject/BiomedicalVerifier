# Dashboards

## Current blue dashboard

Source: `outputs/biomedical-verifier-blue` in the workspace. A static HTML/CSS/JavaScript frontend, served locally on port 3001.

| File | Purpose |
|---|---|
| `index.html` | Claim form and results interface |
| `styles.css` | Responsive layout and visual theme |
| `app.js` | Input handling, backend requests and result rendering |
| `insights.js` | Evidence/probability/timing visualizations |
| `serve.py` | Local static server and API bridge |
| `netlify.toml` | Static hosting configuration |

The dedicated chest-X-ray feature was removed. Generic image attachment does not make the final verdict image-grounded. Result scores describe model output, not clinical certainty.

Use the combined launcher documented in [the runbook](RUNBOOK.md). The older frontend README's simple `http.server` preview does not provide the custom API bridge from `serve.py`.

## Original dashboard

`~/Downloads/BiomedicalVerifier/frontend` retains the original frontend project. UI backup directories also exist in the application root. They are historical alternatives; this documentation does not replace or delete them. Their source assets appear in the application catalog when within the catalog's scope.

## Hosting

The Netlify configuration concerns the static frontend. The Python models, local artifacts and Ollama require a separate backend environment. Presence of hosting configuration is not proof of deployment. Never display sample results as live model results.
