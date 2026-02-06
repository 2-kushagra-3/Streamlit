import streamlit as st
from datetime import date

# --------------------------------------------------
# CONFIG
# --------------------------------------------------
st.set_page_config(page_title="Just a Small App", layout="centered")

TODAY = date.today()
UNLOCK_DATE = date(TODAY.year, 2, 7)

# --------------------------------------------------
# STATE INIT
# --------------------------------------------------
if "page" not in st.session_state:
    st.session_state.page = 1

saved_mood = st.query_params.get("mood", None)

if "mood" not in st.session_state:
    st.session_state.mood = saved_mood

# --------------------------------------------------
# COLOR PALETTES (NO TRUE DARK MODE)
# --------------------------------------------------
PALETTES = {
    None: {"bg": "#f5f1ea", "accent": "#7a6f63"},        # default beige
    "Calm": {"bg": "#eef3ee", "accent": "#5f7a68"},
    "Soft happy": {"bg": "#f7ecef", "accent": "#9c5f6a"},
    "Nostalgic": {"bg": "#f2e6d8", "accent": "#7a5c45"},
    "Late night": {"bg": "#e9ecf1", "accent": "#4b5563"},  # muted, NOT dark
}

palette = PALETTES.get(st.session_state.mood, PALETTES[None])

# --------------------------------------------------
# GLOBAL STYLES
# --------------------------------------------------
st.markdown(
    f"""
    <style>
    html, body, .stApp {{
        background-color: {palette['bg']} !important;
    }}
    h1, h2, h3 {{
        color: {palette['accent']} !important;
        font-family: Georgia, serif;
    }}
    p, label {{
        color: {palette['accent']} !important;
        font-family: Arial, sans-serif;
        font-size: 16px;
    }}
    </style>
    """,
    unsafe_allow_html=True
)

# --------------------------------------------------
# PAGE 1 — STORY
# --------------------------------------------------
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

# --------------------------------------------------
# PAGE 2 — EXPERIENCE
# --------------------------------------------------
elif st.session_state.page == 2:

    # -------- DATE LOCK --------
    if TODAY < UNLOCK_DATE:
        st.title("Almost")
        st.write("Not quite today. This opens with the week 🌹")
        st.stop()

    st.title("A quiet Valentine’s week")

    st.write("""
    Valentine’s week has themes for each day.
    I figured I’d reinterpret them… gently.
    """)

    # -------- MOOD PICKER --------
    mood = st.selectbox(
        "Pick a mood for today:",
        ["", "Calm", "Soft happy", "Nostalgic", "Late night"],
        index=0
    )

    if mood:
        st.session_state.mood = mood
        st.query_params["mood"] = mood

        SONGS = {
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
                "link": "https://open.spotify.com/track/1ZyudLFv35SRvY5tq7Lz4k",
                "caption": "Some songs remember things for us."
            },
            "Late night": {
                "title": "Arctic Monkeys – 505",
                "link": "https://open.spotify.com/track/2eVYJ2eJv9Fbl9p1h4pY7X",
                "caption": "Best heard when the world slows down."
            },
        }

        song = SONGS[mood]

        # -------- ROSE (ONLY AFTER MOOD) --------
        st.markdown("## 🌹")

        st.markdown(f"### 🎧 {song['title']}")
        st.markdown(f"[Open song ↗]({song['link']})")
        st.caption(song["caption"])

        st.divider()

        # -------- FINAL MESSAGE --------
        st.write("""
        If today quietly feels like a rose kind of day…  
        I’m not hard to find.
        """)

