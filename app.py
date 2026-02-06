import streamlit as st
from datetime import date

st.set_page_config(page_title="Just a Small App", layout="centered")

# ---------- DATE LOCK ----------
TODAY = date.today()
UNLOCK_DATE = date(2026, 2, 7)  # adjust year if needed

# ---------- LOAD SAVED MOOD ----------
query_params = st.experimental_get_query_params()
saved_mood = query_params.get("mood", ["Default"])[0]

if "page" not in st.session_state:
    st.session_state.page = 1

if "mood" not in st.session_state:
    st.session_state.mood = saved_mood

# ---------- COLOR PALETTES (FIXED) ----------
palettes = {
    "Default": {"bg": "#f5f1ea", "accent": "#7a6f63"},
    "Calm": {"bg": "#eef3ee", "accent": "#5f7a68"},
    "Soft happy": {"bg": "#f7ecef", "accent": "#9c5f6a"},
    "Nostalgic": {"bg": "#f2e6d8", "accent": "#7a5c45"},
    "Late night": {"bg": "#e9ecf1", "accent": "#4b5563"},  # FIXED (not dark)
}

palette = palettes.get(st.session_state.mood, palettes["Default"])

# ---------- GLOBAL STYLES ----------
st.markdown(
    f"""
    <style>
    html, body, [class*="st-"] {{
        background-color: {palette['bg']} !important;
        color: {palette['accent']} !important;
    }}
    h1, h2, h3 {{
        color: {palette['accent']} !important;
        font-family: 'Georgia', serif;
    }}
    p {{
        color: {palette['accent']} !important;
        font-family: 'Arial', sans-serif;
    }}
    </style>
    """,
    unsafe_allow_html=True
)

# ---------- PAGE 1 ----------
if st.session_state.page == 1:
    st.title("Hey")

    st.write("""
    So this started very randomly.

    I was bored, scrolling through the calendar, pretending to be productive…
    and then I noticed — it’s Valentine’s Week already.

    No big plans. No dramatic reason.
    Just one of those *“huh… why not?”* moments.

    So I decided to build something small.
    Something light.
    Something that fits the week — without making a big deal out of it.

    Anyway… since you’re here now,
    might as well continue 🙂
    """)

    if st.button("Continue →"):
        st.session_state.page = 2
        st.rerun()

# ---------- PAGE 2 ----------
elif st.session_state.page == 2:
    st.title("A quiet Valentine’s week")

    # ---- DATE LOCK ----
    if TODAY < UNLOCK_DATE:
        st.write("Not quite today. Check back when the week begins 🌹")
        st.stop()

    st.write("""
    Valentine’s week has themes for each day.
    I figured I’d reinterpret them… gently.
    """)

    mood = st.radio(
        "Pick a mood for today:",
        ["Calm", "Soft happy", "Nostalgic", "Late night"],
        index=["Calm", "Soft happy", "Nostalgic", "Late night"].index(
            st.session_state.mood
        ) if st.session_state.mood in palettes else 0
    )

    # ---- SAVE MOOD ----
    st.session_state.mood = mood
    st.experimental_set_query_params(mood=mood)

    songs = {
        "Calm": {
            "title": "Coldplay – Sparks",
            "link": "https://open.spotify.com/track/7D0RhFcb3CrfPuTJ0obrod",
            "caption": "Soft. Unrushed. Almost silent."
        },
        "Soft happy": {
            "title": "Rex Orange County – Sunflower",
            "link": "https://open.spotify.com/track/0xY0i9l2E12LHG0L1r5Q3s",
            "caption": "Feels like light through a window."
        },
        "Nostalgic": {
            "title": "Chhu Kar Mere Mann Ko",
            "link": "https://open.spotify.com/track/4oYFq0kYzZpVbJX9WJZxyz",
            "caption": "Some songs remember things for us."
        },
        "Late night": {
            "title": "Arctic Monkeys – 505",
            "link": "https://open.spotify.com/track/2eVYJ2eJv9Fbl9p1h4pY7X",
            "caption": "Best heard when the world slows down."
        },
    }

    # 🌹 ROSE APPEARS ONLY AFTER MOOD PICK
    st.markdown("## 🌹")

    st.markdown(f"### 🎧 {songs[mood]['title']}")
    st.markdown(f"[Open song ↗]({songs[mood]['link']})")
    st.caption(songs[mood]['caption'])

    st.divider()

    st.write("""
    If today quietly feels like a rose kind of day…  
    I’m not hard to find.
    """)

