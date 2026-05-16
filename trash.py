import streamlit as st
from datetime import datetime

st.set_page_config(
    page_title="ThinkbookLM",
    page_icon="📓",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown("""
<style>
    /* Global dark theme */
    .stApp {
        background-color: #1a1b1e;
        color: #e0e0e0;
    }

    /* Hide default streamlit elements */
    #MainMenu, footer, header { visibility: hidden; }
    .block-container { padding: 0 !important; max-width: 100% !important; }

    /* Top navbar */
    .navbar {
        display: flex;
        align-items: center;
        justify-content: space-between;
        padding: 14px 32px;
        background-color: #1a1b1e;
        border-bottom: 1px solid #2e2f33;
        position: sticky;
        top: 0;
        z-index: 100;
    }
    .navbar-brand {
        display: flex;
        align-items: center;
        gap: 10px;
        font-size: 20px;
        font-weight: 600;
        color: #e0e0e0;
        text-decoration: none;
    }
    .navbar-icon {
        width: 32px;
        height: 32px;
        background: linear-gradient(135deg, #6b8afd, #a78bfa);
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 16px;
    }
    .navbar-right {
        display: flex;
        align-items: center;
        gap: 12px;
    }
    .btn-settings {
        display: flex;
        align-items: center;
        gap: 6px;
        background: transparent;
        border: 1px solid #3e3f44;
        border-radius: 20px;
        color: #b0b3ba;
        padding: 7px 16px;
        font-size: 14px;
        cursor: pointer;
    }
    .avatar {
        width: 32px;
        height: 32px;
        background: linear-gradient(135deg, #f97316, #ec4899);
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 14px;
        font-weight: 600;
        color: white;
    }

    /* Tabs row */
    .tabs-row {
        display: flex;
        align-items: center;
        justify-content: space-between;
        padding: 16px 32px 0 32px;
        gap: 12px;
    }
    .tabs-left {
        display: flex;
        align-items: center;
        gap: 4px;
    }
    .tab-btn {
        padding: 7px 18px;
        border-radius: 20px;
        border: none;
        font-size: 14px;
        cursor: pointer;
        background: transparent;
        color: #9ca3af;
    }
    .tab-btn.active {
        background-color: #3b3d45;
        color: #e0e0e0;
        font-weight: 500;
    }
    .tabs-right {
        display: flex;
        align-items: center;
        gap: 8px;
    }
    .icon-btn {
        width: 36px;
        height: 36px;
        border-radius: 50%;
        border: none;
        background: transparent;
        color: #9ca3af;
        font-size: 16px;
        cursor: pointer;
        display: flex;
        align-items: center;
        justify-content: center;
    }
    .icon-btn.active {
        background-color: #3b3d45;
        color: #e0e0e0;
    }
    .sort-btn {
        display: flex;
        align-items: center;
        gap: 6px;
        padding: 7px 14px;
        border-radius: 20px;
        border: 1px solid #3e3f44;
        background: transparent;
        color: #b0b3ba;
        font-size: 14px;
        cursor: pointer;
    }
    .create-btn {
        display: flex;
        align-items: center;
        gap: 6px;
        padding: 8px 18px;
        border-radius: 24px;
        border: 2px solid #e0e0e0;
        background: transparent;
        color: #e0e0e0;
        font-size: 14px;
        font-weight: 500;
        cursor: pointer;
    }

    /* Section headings */
    .section-title {
        font-size: 22px;
        font-weight: 500;
        color: #e0e0e0;
        padding: 28px 32px 16px 32px;
    }

    /* Featured cards */
    .featured-card {
        border-radius: 14px;
        overflow: hidden;
        background: #23252b;
        position: relative;
        min-height: 200px;
        cursor: pointer;
        transition: transform 0.15s ease, box-shadow 0.15s ease;
    }
    .featured-card:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 24px rgba(0,0,0,0.4);
    }
    .featured-card-image {
        width: 100%;
        height: 200px;
        object-fit: cover;
        display: block;
    }
    .featured-card-overlay {
        position: absolute;
        bottom: 0;
        left: 0;
        right: 0;
        padding: 16px;
        background: linear-gradient(transparent, rgba(0,0,0,0.85));
    }
    .featured-card-plain {
        padding: 20px;
        min-height: 200px;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
    }
    .card-source-badge {
        display: flex;
        align-items: center;
        gap: 8px;
        margin-bottom: 8px;
        font-size: 12px;
        color: #b0b3ba;
    }
    .source-icon {
        width: 22px;
        height: 22px;
        border-radius: 50%;
        background: #e63946;
        display: inline-flex;
        align-items: center;
        justify-content: center;
        font-size: 10px;
        font-weight: 700;
        color: white;
    }
    .card-title {
        font-size: 18px;
        font-weight: 600;
        color: #e0e0e0;
        margin-bottom: 10px;
        line-height: 1.3;
    }
    .card-meta {
        font-size: 12px;
        color: #9ca3af;
        display: flex;
        align-items: center;
        gap: 6px;
    }

    /* Recent notebook cards */
    .notebook-card {
        border-radius: 14px;
        background: #23252b;
        padding: 20px;
        min-height: 170px;
        cursor: pointer;
        position: relative;
        transition: transform 0.15s ease, box-shadow 0.15s ease;
    }
    .notebook-card:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 24px rgba(0,0,0,0.4);
    }
    .notebook-emoji {
        font-size: 40px;
        margin-bottom: 10px;
        display: block;
    }
    .notebook-title {
        font-size: 16px;
        font-weight: 500;
        color: #e0e0e0;
        margin-bottom: 6px;
    }
    .notebook-meta {
        font-size: 12px;
        color: #6b7280;
    }
    .notebook-menu {
        position: absolute;
        top: 14px;
        right: 14px;
        color: #6b7280;
        font-size: 16px;
        cursor: pointer;
    }
    .create-notebook-card {
        border-radius: 14px;
        background: #1e1f24;
        border: 2px dashed #3b3d45;
        min-height: 170px;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        cursor: pointer;
        transition: border-color 0.15s ease;
    }
    .create-notebook-card:hover {
        border-color: #6b8afd;
    }
    .create-circle {
        width: 52px;
        height: 52px;
        border-radius: 50%;
        background: #3b3d45;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 26px;
        color: #b0b3ba;
        margin-bottom: 12px;
    }
    .create-label {
        font-size: 15px;
        color: #b0b3ba;
        font-weight: 400;
    }

    /* See all */
    .see-all-row {
        display: flex;
        justify-content: flex-end;
        padding: 8px 32px;
    }
    .see-all-btn {
        display: flex;
        align-items: center;
        gap: 6px;
        color: #9ca3af;
        font-size: 14px;
        cursor: pointer;
        background: transparent;
        border: none;
        padding: 6px 12px;
        border-radius: 8px;
    }
    .see-all-btn:hover { color: #e0e0e0; }

    /* Main content padding */
    .main-content {
        padding: 0 32px 48px 32px;
    }

    /* Modal overlay */
    .modal-overlay {
        position: fixed;
        top: 0; left: 0; right: 0; bottom: 0;
        background: rgba(0,0,0,0.7);
        z-index: 999;
        display: flex;
        align-items: center;
        justify-content: center;
    }
    .modal-box {
        background: #23252b;
        border-radius: 18px;
        padding: 36px;
        width: 480px;
        box-shadow: 0 20px 60px rgba(0,0,0,0.6);
    }
    .modal-title {
        font-size: 22px;
        font-weight: 600;
        color: #e0e0e0;
        margin-bottom: 24px;
    }
    .modal-input {
        width: 100%;
        background: #1a1b1e;
        border: 1px solid #3b3d45;
        border-radius: 10px;
        padding: 12px 16px;
        color: #e0e0e0;
        font-size: 15px;
        margin-bottom: 16px;
    }
    .modal-actions {
        display: flex;
        gap: 10px;
        justify-content: flex-end;
        margin-top: 20px;
    }
    .modal-cancel {
        padding: 9px 20px;
        border-radius: 20px;
        border: 1px solid #3b3d45;
        background: transparent;
        color: #b0b3ba;
        font-size: 14px;
        cursor: pointer;
    }
    .modal-create {
        padding: 9px 20px;
        border-radius: 20px;
        border: none;
        background: #6b8afd;
        color: white;
        font-size: 14px;
        font-weight: 500;
        cursor: pointer;
    }
</style>
""", unsafe_allow_html=True)

# ---------- Session state ----------
if "notebooks" not in st.session_state:
    st.session_state.notebooks = [
        {"id": 1, "title": "Designing a Spotify Artist...", "emoji": "🎵", "date": "Aug 5, 2025", "sources": 1},
        {"id": 2, "title": "Untitled notebook", "emoji": "📒", "date": "Apr 24, 2025", "sources": 0},
        {"id": 3, "title": "Untitled notebook", "emoji": "🤯", "date": "Oct 4, 2024", "sources": 1},
    ]
if "show_create_modal" not in st.session_state:
    st.session_state.show_create_modal = False
if "active_tab" not in st.session_state:
    st.session_state.active_tab = "All"

FEATURED = [
    {
        "source": "The Atlantic",
        "source_icon": "A",
        "source_color": "#e63946",
        "title": "Stories on Progress, from The Atlantic",
        "date": "Apr 11, 2026",
        "sources": 71,
        "image": None,
    },
    {
        "source": "Our World in Data",
        "source_icon": "📊",
        "source_color": "#2563eb",
        "title": "Trends in Health, Wealth and...",
        "date": "Apr 15, 2025",
        "sources": 24,
        "image": None,
    },
    {
        "source": "Google Research",
        "source_icon": "🔬",
        "source_color": "#4285f4",
        "title": "Can a computer simulate a brain?",
        "date": "Jul 29, 2025",
        "sources": 17,
        "image": "https://images.unsplash.com/photo-1507413245164-6160d8298b31?w=400&q=80",
    },
    {
        "source": "ThinkbookLM",
        "source_icon": "📓",
        "source_color": "#7c3aed",
        "title": "Introduction to ThinkbookLM",
        "date": "Dec 6, 2023",
        "sources": 27,
        "image": "https://images.unsplash.com/photo-1544716278-ca5e3f4abd8c?w=400&q=80",
    },
]

# ---------- Navbar ----------
st.markdown("""
<div class="navbar">
  <div class="navbar-brand">
    <div class="navbar-icon">📓</div>
    ThinkbookLM
  </div>
  <div class="navbar-right">
    <button class="btn-settings">⚙️ Settings</button>
    <span style="background:#374151;color:#9ca3af;font-size:11px;padding:3px 8px;border-radius:4px;font-weight:600;">PRO</span>
    <div class="avatar">S</div>
  </div>
</div>
""", unsafe_allow_html=True)

# ---------- Tab bar ----------
tabs = ["All", "My notebooks", "Featured notebooks"]
col_tabs, col_right = st.columns([3, 2])

with col_tabs:
    selected_tab = st.radio(
        "tabs",
        tabs,
        index=tabs.index(st.session_state.active_tab),
        horizontal=True,
        label_visibility="collapsed",
    )
    if selected_tab != st.session_state.active_tab:
        st.session_state.active_tab = selected_tab
        st.rerun()

with col_right:
    btn_cols = st.columns([1, 1, 1, 2, 2])
    with btn_cols[3]:
        st.button("Most recent ▾", use_container_width=True)
    with btn_cols[4]:
        if st.button("＋ Create new", type="primary", use_container_width=True):
            st.session_state.show_create_modal = True

st.markdown("<div style='height:8px'></div>", unsafe_allow_html=True)

# ---------- Create notebook modal ----------
if st.session_state.show_create_modal:
    with st.container():
        st.markdown("""
        <div style="background:#23252b;border:1px solid #3b3d45;border-radius:18px;padding:32px;max-width:460px;margin:0 auto;">
          <div class="modal-title">Create new notebook</div>
        </div>
        """, unsafe_allow_html=True)
        new_title = st.text_input("Notebook title", placeholder="Untitled notebook", key="new_notebook_title")
        new_emoji = st.text_input("Emoji icon", value="📓", key="new_notebook_emoji")
        c1, c2 = st.columns(2)
        with c1:
            if st.button("Cancel", use_container_width=True):
                st.session_state.show_create_modal = False
                st.rerun()
        with c2:
            if st.button("Create", type="primary", use_container_width=True):
                title = new_title.strip() or "Untitled notebook"
                emoji = new_emoji.strip() or "📓"
                new_id = max((n["id"] for n in st.session_state.notebooks), default=0) + 1
                st.session_state.notebooks.insert(0, {
                    "id": new_id,
                    "title": title,
                    "emoji": emoji,
                    "date": datetime.now().strftime("%b %-d, %Y"),
                    "sources": 0,
                })
                st.session_state.show_create_modal = False
                st.rerun()

# ---------- Featured notebooks ----------
if st.session_state.active_tab in ("All", "Featured notebooks"):
    st.markdown('<div class="section-title">Featured notebooks</div>', unsafe_allow_html=True)

    cols = st.columns(4)
    for i, nb in enumerate(FEATURED):
        with cols[i]:
            if nb["image"]:
                st.markdown(f"""
                <div class="featured-card" style="position:relative;min-height:200px;overflow:hidden;">
                  <img src="{nb['image']}" class="featured-card-image"/>
                  <div class="featured-card-overlay">
                    <div class="card-source-badge">
                      <span style="font-size:14px">{nb['source_icon']}</span>
                      <span>{nb['source']}</span>
                    </div>
                    <div class="card-title" style="font-size:16px">{nb['title']}</div>
                    <div class="card-meta">{nb['date']} · {nb['sources']} sources 🌐</div>
                  </div>
                </div>
                """, unsafe_allow_html=True)
            else:
                st.markdown(f"""
                <div class="featured-card featured-card-plain">
                  <div>
                    <div class="card-source-badge">
                      <span style="background:{nb['source_color']};width:22px;height:22px;border-radius:50%;display:inline-flex;align-items:center;justify-content:center;font-size:11px;font-weight:700;color:white;">{nb['source_icon']}</span>
                      <span>{nb['source']}</span>
                    </div>
                    <div class="card-title">{nb['title']}</div>
                  </div>
                  <div class="card-meta">{nb['date']} · {nb['sources']} sources 🌐</div>
                </div>
                """, unsafe_allow_html=True)

    st.markdown("""
    <div class="see-all-row">
      <button class="see-all-btn">See all &nbsp;›</button>
    </div>
    """, unsafe_allow_html=True)

# ---------- Recent notebooks ----------
if st.session_state.active_tab in ("All", "My notebooks"):
    st.markdown('<div class="section-title">Recent notebooks</div>', unsafe_allow_html=True)

    notebooks = st.session_state.notebooks
    # Show create card + up to 7 notebooks = 8 slots total, 4 per row
    slots = [None] + notebooks  # None = create card
    cols_per_row = 4
    rows = [slots[i:i+cols_per_row] for i in range(0, len(slots), cols_per_row)]

    for row in rows:
        cols = st.columns(cols_per_row)
        for j, item in enumerate(row):
            with cols[j]:
                if item is None:
                    # Create new card
                    if st.button(
                        "＋\n\nCreate new notebook",
                        key="create_new_main",
                        use_container_width=True,
                        help="Create a new notebook",
                    ):
                        st.session_state.show_create_modal = True
                        st.rerun()
                    st.markdown("""
                    <style>
                    div[data-testid="stButton"] button[kind="secondary"] {
                        border: 2px dashed #3b3d45 !important;
                        background: #1e1f24 !important;
                        color: #b0b3ba !important;
                        border-radius: 14px !important;
                        min-height: 170px !important;
                        font-size: 14px !important;
                    }
                    </style>
                    """, unsafe_allow_html=True)
                else:
                    sources_txt = f"{item['sources']} source{'s' if item['sources'] != 1 else ''}"
                    st.markdown(f"""
                    <div class="notebook-card">
                      <div class="notebook-menu">⋮</div>
                      <span class="notebook-emoji">{item['emoji']}</span>
                      <div class="notebook-title">{item['title']}</div>
                      <div class="notebook-meta">{item['date']} · {sources_txt}</div>
                    </div>
                    """, unsafe_allow_html=True)
        # Pad remaining columns if row is not full
        if len(row) < cols_per_row:
            for _ in range(cols_per_row - len(row)):
                pass

    st.markdown("<div style='height:32px'></div>", unsafe_allow_html=True)
