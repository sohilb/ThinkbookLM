import streamlit as st

pages = st.navigation(
    [
        st.Page("pages/notebook.py", title="Notebook"),
    ],
    position="hidden",
)

st.set_page_config(
    page_title="ThinkbookLM",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="collapsed",
    menu_items={
        "Get help": None,
        "Report a bug": None,
        "About": None,
    },
)

# Landing page — to be implemented


if 'page' not in st.session_state:
    st.session_state.page = 'home'
if 'display_mode' not in st.session_state:
    st.session_state.display_mode = 'grid'

# Top utility bar
with st.container(horizontal=True, vertical_alignment="center", border=True):
    st.image(image="frontend/assets/logo.jpg", width=50)
    st.subheader("ThinkbookLM")
    st.space("stretch")
    st.button("👤", key="profile_btn", help="Profile")


with st.container(horizontal=True, vertical_alignment="center", width="stretch"):
    with st.container(horizontal=True):
        filer_options = ["All", "My notebooks", " notebooks"]
        st.pills("filters", options=filer_options, key="filter_selection_1", default="All", selection_mode="single", label_visibility="collapsed")
    with st.container(horizontal=True, horizontal_alignment="right", vertical_alignment="center"):
        st.button("", icon=":material/search:", key="search_btn", help="Search for a notebook")
        _is_grid = st.session_state.display_mode == 'grid'
        _grid_opt = ":material/grid_view: :material/check:" if _is_grid else ":material/grid_view:"
        _list_opt = ":material/reorder: :material/check:" if not _is_grid else ":material/reorder:"
        _selected = st.segmented_control("Display mode", options=[_grid_opt, _list_opt], label_visibility="collapsed", default=_grid_opt if _is_grid else _list_opt)
        if _selected and ":material/grid_view:" in _selected and not _is_grid:
            st.session_state.display_mode = 'grid'
            st.rerun()
        elif _selected and ":material/reorder:" in _selected and _is_grid:
            st.session_state.display_mode = 'list'
            st.rerun()
        st.selectbox("Sort selection", options=["Most recent", "Title"], key="sort_selection", label_visibility="collapsed")
        st.button("Create new", icon=":material/add:", key="create_notebook_btn_1")