# Local runbook

## Start the improved local application

Run in a terminal, including VS Code's terminal:

```zsh
zsh /Users/joshua/Documents/Codex/2026-09-29/can-x20-2/start_project.command
```

This existing launcher references the Python environment at `~/Downloads/BiomedicalVerifier/.venv`. It is machine-specific, not a portable installation command.

## Check without starting

```zsh
zsh /Users/joshua/Documents/Codex/2026-09-29/can-x20-2/start_project.command --check
```

Frontend: `http://127.0.0.1:3001/`. Backend: `http://127.0.0.1:8000/`. Ollama normally uses port 11434.

## Required local resources

- All five phase source folders and the BiomedicalVerifier application.
- Existing Python environment and model dependencies.
- The 35,183-document metadata artifact in Phase 2.
- Cached MiniLM and PubMedBERT model/tokenizer files.
- The trained clean selector and its trained combiner artifacts.
- Phase 1 diagnostic checkpoint and phase configuration files required by pipeline validation.
- Ollama with the configured `qwen2.5:7b` model.

The candidate requests offline Hugging Face loading; missing models will cause an error instead of silently downloading. Do not load unknown pickle/joblib/checkpoint files.

## Troubleshooting

For `address already in use`, inspect `lsof -nP -iTCP:8000 -sTCP:LISTEN` and determine whether the desired backend is already active. Stop only the intended server. Use Ctrl+C in its own terminal when possible.

For pasted `^[[200~` characters, clear the command line with Ctrl+C and paste/type the clean command again.

Inspect `outputs/evidence-combiner/dashboard-runtime/launcher-logs` for launcher output. Do not infer a healthy backend from a visible frontend page alone. This documentation task has not restarted or revalidated the running application.
