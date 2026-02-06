import streamlit as st

# --------------------------------------------------
# CONFIG
# --------------------------------------------------
st.set_page_config(page_title="Just a Small App", layout="centered")

# --------------------------------------------------
# STATE INIT
# --------------------------------------------------
if "page" not in st.session_state:
    st.session_state.page = 1

saved_mood = st.query_params.get("mood", None)

if "mood" not in st.session_state:
    st.session_state.mood = saved_mood

# --------------------------------------------------
# COLOR PALETTES
# --------------------------------------------------
PALETTES = {
    None: {"bg": "#f5f1ea", "accent": "#7a6f63"},
    "Calm": {"bg": "#eef3ee", "accent": "#5f7a68"},
    "Soft happy": {"bg": "#f7ecef", "accent": "#9c5f6a"},
    "Nostalgic": {"bg": "#f2e6d8", "accent": "#7a5c45"},
    "Late night": {"bg": "#e9ecf1", "accent": "#4b5563"},
}

palette = PALETTES.get(st.session_state.mood, PALETTES[None])

# --------------------------------------------------
# GLOBAL STYLES (LIGHT TOUCH)
# --------------------------------------------------
st.markdown(
    f"""
    <style>
    html, body, .stApp {{
        background-color: {palette['bg']} !important;
        transition: background-color 0.5s ease;
    }}

    h1, h2, h3 {{
        color: {palette['accent']} !important;
        font-family: 'Playfair Display', Georgia, serif;
        margin-bottom: 0.4em;
    }}

    p, label {{
        color: {palette['accent']} !important;
        font-family: 'Inter', Arial, sans-serif;
        font-size: 16px;
        line-height: 1.65;
        margin-bottom: 0.8em;
    }}

    .soft {{
        background: rgba(255,255,255,0.25);
        border-radius: 14px;
        padding: 1.2em 1.4em;
    }}

    .stButton > button {{
        background-color: transparent;
        border: 1px solid {palette['accent']};
        color: {palette['accent']};
        padding: 0.35em 1.3em;
        border-radius: 22px;
    }}

    * {{
        cursor: url("https://emojiapi.dev/api/v1/rose/32.png"), auto;
    }}
    </style>
    """,
    unsafe_allow_html=True
)

# --------------------------------------------------
# PAGE 1
# --------------------------------------------------
if st.session_state.page == 1:
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

# --------------------------------------------------
# PAGE 2
# --------------------------------------------------
elif st.session_state.page == 2:
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
        st.session_state.mood = mood
        st.query_params["mood"] = mood

        SONGS = {
            "Calm": {
                "title": "Coldplay – Sparks",
                "link": "https://open.spotify.com/track/7D0RhFcb3CrfPuTJ0obrod",
                "caption": "Soft. Unrushed. Almost weightless."
            },
            "Soft happy": {
                "title": "Rex Orange County – Sunflower",
                "link": "https://open.spotify.com/track/0xY0i9l2E12LHG0L1r5Q3s",
                "caption": "Light, warm, and uncomplicated."
            },
            "Nostalgic": {
                "title": "Chhu Kar Mere Mann Ko",
                "link": "https://open.spotify.com/track/1ZyudLFv35SRvY5tq7Lz4k",
                "caption": "Some songs remember things better than we do."
            },
            "Late night": {
                "title": "Arctic Monkeys – 505",
                "link": "https://open.spotify.com/track/2eVYJ2eJv9Fbl9p1h4pY7X",
                "caption": "Best heard when everything else goes quiet."
            },
        }

        FINAL_MESSAGES = {
            "Calm": "If the day feels slow and unhurried, I wouldn’t mind keeping it that way.",
            "Soft happy": "If today carries a lighter kind of smile, that feels nice to share.",
            "Nostalgic": "If you find yourself drifting a little, I’m not far.",
            "Late night": "If the night feels longer than usual, conversations still work after midnight.",
        }

        song = SONGS[mood]

        st.markdown("### 🌹")
        st.markdown(f"**🎧 {song['title']}**")
        st.markdown(f"[Open song ↗]({song['link']})")
        st.caption(song["caption"])

        st.markdown(
            f"<div class='soft'><p>{FINAL_MESSAGES[mood]}</p></div>",
            unsafe_allow_html=True
        )
