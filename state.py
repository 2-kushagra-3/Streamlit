import streamlit as st

def init_state():
    if "page" not in st.session_state:
        st.session_state.page = 1

    if "mood" not in st.session_state:
        st.session_state.mood = st.query_params.get("mood", None)


def set_mood(mood: str):
    st.session_state.mood = mood
    st.query_params["mood"] = mood
