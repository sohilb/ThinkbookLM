# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project

ThinkbookLM is a NotebookLM clone built with Streamlit. The UI is a three-panel layout (Sources | Chat | Studio) modelled after Google's NotebookLM.

## Commands

This project uses `uv` for dependency management.

```bash
# Install dependencies
uv sync

# Run the app
uv run streamlit run app.py

# Run with auto-reload (default in dev)
uv run streamlit run app.py --server.runOnSave true

# Add a dependency
uv add <package>
```

## Architecture

All application code lives in `app.py` (single-file Streamlit app). `main.py` is a placeholder entry point not used by the UI.

**Layout** — three bordered columns rendered after a top utility bar:
- `col1` (25%) — Sources panel: file upload via `@st.dialog`, uploaded filenames stored in `st.session_state.sources`
- `col2` (50%) — Chat panel
- `col3` (25%) — Studio panel

**State** — managed entirely through `st.session_state`. Key keys:
- `page` — current page/view
- `sources` — list of uploaded source filenames

**UI conventions:**
- Use only native Streamlit APIs — no `unsafe_allow_html`, no injected CSS/JS
- Dialogs (`@st.dialog`) are preferred over inline conditional widget rendering to keep the main page uncluttered
- `st.rerun()` is called after mutating session state inside dialogs to reflect changes immediately
