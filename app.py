import streamlit as st

st.set_page_config(page_title="Just a Small App", layout="centered")

# ---------- STATE ----------
if "page" not in st.session_state:
    st.session_state.page = 1

if "mood" not in st.session_state:
    st.session_state.mood = "Default"

# ---------- COLOR PALETTES ----------
palettes = {
    "Default": {"bg": "#f5f1ea", "accent": "#7a6f63"},
    "Calm": {"bg": "#eef3ee", "accent": "#5f7a68"},
    "Soft happy": {"bg": "#f7ecef", "accent": "#9c5f6a"},
    "Nostalgic": {"bg": "#f2e6d8", "accent": "#7a5c45"},
    "Late night": {"bg": "#1f2633", "accent": "#c2c6d3"},
}

palette = palettes.get(st.session_state.mood, palettes["Default"])

# ---------- GLOBAL STYLES ----------
st.markdown(
    f"""
    <style>
    body {{
        background-color: {palette['bg']};
    }}
    .stApp {{
        background-color: {palette['bg']};
    }}
    h1, h2, h3 {{
        color: {palette['accent']};
        font-family: 'Georgia', serif;
    }}
    p, label {{
        color: {palette['accent']};
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

    st.write("""
    Valentine’s week has themes for each day.
    I figured I’d reinterpret them… gently.
    """)

    st.subheader("🌹 Feb 7 — Rose Day")

    mood = st.radio(
        "Pick a mood for today:",
        ["Calm", "Soft happy", "Nostalgic", "Late night"],
        index=0
    )

    st.session_state.mood = mood

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
            "link": "https://open.spotify.com/track/1Pz4D6Kx9mVjvGZ0r7dxyz",
            "caption": "Some songs remember things for us."
        },
        "Late night": {
            "title": "Arctic Monkeys – 505",
            "link": "https://open.spotify.com/track/2eVYJ2eJv9Fbl9p1h4pY7X",
            "caption": "Best heard when the world slows down."
        },
    }

    st.markdown(f"### 🎧 {songs[mood]['title']}")
    st.markdown(f"[Open song ↗]({songs[mood]['link']})")
    st.caption(songs[mood]['caption'])

    st.divider()

    st.write("""
    If today happens to feel a little like rose day…  
    I’m just a message away.
    """)

