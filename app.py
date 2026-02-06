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
# COLOR PALETTES (UNCHANGED)
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
# GLOBAL STYLES (STRUCTURE + POLISH)
# --------------------------------------------------
st.markdown(
    f"""
    <style>
    html, body, .stApp {{
        background-color: {palette['bg']} !important;
        transition: background-color 0.6s ease;
    }}

    h1, h2, h3 {{
        color: {palette['accent']} !important;
        font-family: 'Playfair Display', Georgia, serif;
        letter-spacing: 0.4px;
    }}

    p, label {{
        color: {palette['accent']} !important;
        font-family: 'Inter', Arial, sans-serif;
        font-size: 16px;
        line-height: 1.75;
    }}

    /* Soft card */
    .card {{
        background: rgba(255,255,255,0.35);
        border-radius: 20px;
        padding: 2em;
        margin: 2em 0;
        box-shadow: 0 8px 30px rgba(0,0,0,0.03);
    }}

    .spacer {{
        height: 2.5em;
    }}

    .divider {{
        width: 40px;
        height: 2px;
        background-color: {palette['accent']}55;
        margin: 2.5em auto;
        border-radius: 2px;
    }}

    .stButton > button {{
        background-color: transparent;
        border: 1px solid {palette['accent']};
        color: {palette['accent']};
        padding: 0.45em 1.6em;
        border-radius: 24px;
        transition: all 0.3s ease;
    }}

    .stButton > button:hover {{
        background-color: {palette['accent']};
        color: {palette['bg']};
    }}

    * {{
        cursor: url("https://emojiapi.dev/api/v1/rose/32.png"), auto;
    }}
    </style>
    """,
    unsafe_allow_html=True
)

# --------------------------------------------------
# PAGE 1 — STORY
# --------------------------------------------------
if st.session_state.page == 1:
    left, center, right = st.columns([1, 4, 1])

    with center:
        st.title("Hey")

        st.markdown(
            """
            <div class="card">
            <p>
            This started pretty randomly.<br><br>

            I was bored, pretending to be productive,
            glanced at the calendar —
            and realised it’s Valentine’s week already.<br><br>

            No big reason.
            No grand plan.<br><br>

            Just one of those moments where you build something
            because you can.<br><br>

            Anyway,
            since you’ve made it this far —
            might as well keep going.
            </p>
            </div>
            """,
            unsafe_allow_html=True
        )

        st.markdown("<div class='spacer'></div>", unsafe_allow_html=True)

        if st.button("Continue →"):
            st.session_state.page = 2
            st.rerun()

# --------------------------------------------------
# PAGE 2 — EXPERIENCE
# --------------------------------------------------
elif st.session_state.page == 2:
    left, center, right = st.columns([1, 4, 1])

    with center:
        st.title("A quieter take on the week")

        st.markdown(
            """
            <div class="card">
            <p>
            Valentine’s week usually comes with a lot of labels.<br>
            I thought I’d reinterpret it —
            gently.
            </p>
            </div>
            """,
            unsafe_allow_html=True
        )

        st.markdown("<div class='divider'></div>", unsafe_allow_html=True)

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

            st.markdown("<div class='spacer'></div>", unsafe_allow_html=True)
            st.markdown("## 🌹")

            st.markdown(
                f"""
                <div class="card">
                <h3>🎧 {song['title']}</h3>
                <p><a href="{song['link']}" target="_blank">Open song ↗</a></p>
                <p><em>{song['caption']}</em></p>
                </div>
                """,
                unsafe_allow_html=True
            )

            st.markdown("<div class='divider'></div>", unsafe_allow_html=True)

            st.markdown(
                f"""
                <div class="card">
                <p>{FINAL_MESSAGES[mood]}</p>
                </div>
                """,
                unsafe_allow_html=True
            )
