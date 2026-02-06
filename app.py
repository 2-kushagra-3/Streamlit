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
    and realised it’s Valentine’s week already.

    No big reason.
    No grand plan.

    Just one of those moments where you build something
    because you can.

    Anyway,
    since you’ve made it this far —
    might as well keep going.
    """)

    if st.button("Continue →"):
        st.session_state.page = 2
        st.rerun()

# ---------- PAGE 2 ----------
elif st.session_state.page == 2:
    apply_theme(st.session_state.mood)

    st.title("A quieter take on the week")

    st.write("""
    Valentine’s week usually comes with a lot of labels.
    I thought I’d reinterpret it — gently.
    """)

    mood = st.selectbox(
        "What kind of mood fits today?",
        ["", "Calm", "Soft happy", "Nostalgic", "Late night"],
        index=0
    )

    if mood:
        # ✅ commit mood FIRST
        st.session_state.mood = mood

        # ✅ re-apply theme AFTER commit
        apply_theme(st.session_state.mood)

        song = SONGS[mood]

        st.markdown("### 🌹")
        st.markdown(f"**🎧 {song['title']}**")
        st.markdown(f"[Open song ↗]({song['link']})")
        st.caption(song["caption"])

        st.markdown(
            f"<div class='soft'><p>{FINAL_MESSAGES[mood]}</p></div>",
            unsafe_allow_html=True
        )
