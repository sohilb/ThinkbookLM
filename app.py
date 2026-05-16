import streamlit as st


st.set_page_config(
    page_title="ThinkbookLM",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        "Get Help": "https://github.com/streamlit/streamlit/issues",
        "Report a bug": "https://github.com/streamlit/streamlit/issues"
    },
)

if "page" not in st.session_state:
    st.session_state.page = "home"
if "sources" not in st.session_state:
    st.session_state.sources = []
if "sources_selected" not in st.session_state:
    st.session_state.sources_selected = 0

@st.dialog("Add Sources")
def add_sources_dialog():
    uploaded_file = st.file_uploader("Choose a file", label_visibility="collapsed", width="stretch", key="dialog_file_uploader")
    if uploaded_file:
        sources = st.session_state.get("sources", [])
        sources.append(uploaded_file.name)
        st.session_state.sources = sources
        st.rerun()
    elif st.button("Websites", icon=":material/insert_link:", width="stretch", key="dialog_websites_btn"):
        pass

# Top utility bar
with st.container(horizontal=True):
    st.text_input("Notebook title", value="Untitled notebook", max_chars=30, key="notebook_title", label_visibility="collapsed", icon=":material/edit:")
    st.space("stretch")
    st.button("Create notebook", key="create_notebook_btn", help="Create notebook", icon=":material/add:", type="secondary" )
    st.button("👤", key="profile_btn", help="Profile")


st.divider()

# Main content area with three columns
col1, col2, col3 = st.columns([0.25, 0.50, 0.25], border=True)
with col1:
    st.subheader("Sources", text_alignment="left", divider="gray")
    if st.button("Add Sources", key="add_sources_btn", width="stretch", icon=":material/add:"):
        add_sources_dialog()
    for source in st.session_state.get("sources", []):
        st.checkbox(str(source), key=f"source_{source}", value=True)

    st.session_state.sources_selected = sum(
        st.session_state.get(f"source_{source}", True)
        for source in st.session_state.get("sources", [])
    )
    
with col2:
    st.subheader("Chat", text_alignment="left", divider="gray")
    with st.container(border=False, height="stretch"):
        st.info("Chat interface coming soon!", icon=":material/add:")
    st.text(f"{st.session_state.get('sources_selected', 0)} sources selected", text_alignment="right", width="stretch")
    if prompt := st.chat_input("Type your message here...", key="chat_input"):
        st.session_state.last_message = prompt
        st.rerun()
with col3:
    st.subheader("Studio", text_alignment="left", divider="gray")
    feat_col_1, feat_col_2 = st.columns(2)
    with feat_col_1:
        st.button("Audio Overview", key="audio_overview_btn", width="stretch", icon=":material/audiotrack:")
        st.button("Video Overview", key="video_overview_btn", width="stretch", icon=":material/videocam:")
        st.button("Reports", key="reports_btn", width="stretch", icon=":material/bar_chart:")
        st.button("Quiz", key="quiz_btn", width="stretch", icon=":material/quiz:")
        st.button("Data Table", key="data_table_btn", width="stretch", icon=":material/table_view:")
    with feat_col_2:
        st.button("Slide Deck", key="slide_deck_btn", width="stretch", icon=":material/slideshow:")
        st.button("Mind map", key="mind_map_btn", width="stretch", icon=":material/insert_chart:")
        st.button("Flashcards", key="flashcards_btn", width="stretch", icon=":material/flash_on:")
        st.button("Infographics", key="infographics_btn", width="stretch", icon=":material/image:")
    
    



@st.fragment(run_every="1s")
def studio_panel():
    st.write(dict(st.session_state))

studio_panel()
