import streamlit as st
from styles import apply_theme
from content import SONGS, FINAL_MESSAGES

st.set_page_config(page_title="Just a Small App", layout="centered")

# ---------- STATE ----------
if "page" not in st.session_state:
    st.session_state.page = 1

if "mood" not in st.session_state:
    st.session_state.mood = None

# ---------- PAGE 1 ----------
if st.session_state.page == 1:
    apply_theme(None)

    st.title("Hey")

    st.write("""
    This started pretty randomly.

    I was bored, pretending to be productive,
    glanced at the calendar —
    and noticed it’s Chocolate Day.

    No big idea behind it.
    Just felt like one of those days
    where you lean into small comforts.

    So I made this.
    """)

    if st.button("Continue →"):
        st.session_state.page = 2
        st.rerun()

# ---------- PAGE 2 ----------
elif st.session_state.page == 2:
    apply_theme(st.session_state.mood)

    st.title("Something for today")

    st.write("""
    Chocolate Day feels less about gestures
    and more about quiet indulgences.
    I thought I’d keep it that way.
    """)

    mood = st.selectbox(
        "What feels right today?",
        ["", "Calm", "Soft happy", "Nostalgic", "Late night"],
        index=0
    )

    if mood:
        st.session_state.mood = mood
        apply_theme(st.session_state.mood)

        song = SONGS[mood]

        st.markdown("### 🍫")
        st.markdown(f"**🎧 {song['title']}**")
        st.markdown(f"[Open song ↗]({song['link']})")
        st.caption(song["caption"])

        st.markdown(
            f"<div class='soft'><p>{FINAL_MESSAGES[mood]}</p></div>",
            unsafe_allow_html=True
        )
