# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project

ThinkbookLM is a full-stack NotebookLM clone. The frontend is Streamlit; the backend (in progress) will be FastAPI. The UI has a three-panel layout (Sources | Chat | Studio).

## Commands

This project uses `uv` for dependency management.

```bash
# Install dependencies
uv sync

# Run the frontend (landing page entry point)
uv run streamlit run frontend/app.py

# Run with auto-reload
uv run streamlit run frontend/app.py --server.runOnSave true

# Run the backend (once implemented)
uv run uvicorn backend.main:app --reload

# Add a dependency
uv add <package>
```

## Structure

```
frontend/
  app.py              # Landing page (Streamlit entry point)
  pages/
    notebook.py       # Notebook UI — Sources | Chat | Studio
  components/         # Reusable Streamlit widgets

backend/
  main.py             # FastAPI app
  api/routes/         # sources.py, chat.py, studio.py
  services/
    ingestion/        # parser → chunker → embedder pipeline
    retrieval/        # vector_store.py — query interface
    generation/       # chat.py, audio.py, structured.py, document.py
    llm/              # client.py — shared Claude API client
  models/             # Pydantic schemas: notebook, source, generation

shared/               # Types shared between frontend and backend
```

## Frontend conventions

- Use only native Streamlit APIs — no `unsafe_allow_html`, no injected CSS/JS
- `@st.dialog` for modal workflows (e.g. Add Sources) to keep page uncluttered
- `st.rerun()` after mutating session state inside dialogs
- `@st.fragment(run_every=...)` for panels that need to reflect state changes independently

## Key session state keys (notebook page)

- `sources` — list of uploaded source filenames
- `sources_selected` — count of checked sources (derived via `sum()` after checkbox render)
- `last_message` — most recent chat input
