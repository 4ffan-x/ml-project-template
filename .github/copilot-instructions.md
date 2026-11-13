# Project rules
- Training runs on Colab; the local laptop has no GPU. Never assume
  CUDA locally; use a `device` variable.
- All hyperparameters come from `configs/config.yaml`, never hardcoded.
- Report macro AUROC and micro F1, not just accuracy.
- Use type hints and short docstrings.
- Write a pytest for any new data-loading function.
- Save checkpoints with epoch, model state, and optimizer state.
- Keep Grad-CAM/explainability code in `explain/`, separate from training.
- Never hardcode secrets; read from `.env`.
- Ask before adding a new dependency.
- Read PROJECT.md before large tasks.
