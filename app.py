import streamlit as st

st.set_page_config(page_title="Valentine Week Journey", page_icon="V", layout="centered")

THEMES = {
    "Beige Aesthetic (Default)": {
        "bg": "#F7F1E8",
        "card": "#FFF8EE",
        "text": "#3E362E",
        "muted": "#7A6F63",
        "accent": "#D6A87A",
        "accent_2": "#C76D5E",
        "btn_text": "#2B2420",
    },
    "Blush Rose": {
        "bg": "#FCEFF1",
        "card": "#FFF7F9",
        "text": "#3B2B2F",
        "muted": "#7A5C66",
        "accent": "#E39AA9",
        "accent_2": "#C46A7A",
        "btn_text": "#2B1D21",
    },
    "Midnight Blue": {
        "bg": "#121826",
        "card": "#1A2233",
        "text": "#E7ECF3",
        "muted": "#A4B0C3",
        "accent": "#7DA2FF",
        "accent_2": "#F2C14E",
        "btn_text": "#0F1220",
    },
}

if "theme_name" not in st.session_state:
    st.session_state.theme_name = "Beige Aesthetic (Default)"

if "step" not in st.session_state:
    st.session_state.step = 1

if "started" not in st.session_state:
    st.session_state.started = False

def apply_theme(theme):
    st.markdown(
        f"""
        <style>
        :root {{
            --bg: {theme["bg"]};
            --card: {theme["card"]};
            --text: {theme["text"]};
            --muted: {theme["muted"]};
            --accent: {theme["accent"]};
            --accent-2: {theme["accent_2"]};
            --btn-text: {theme["btn_text"]};
        }}
        .stApp {{
            background: linear-gradient(135deg, var(--bg) 0%, #ffffff 100%);
            color: var(--text);
        }}
        .card {{
            background: var(--card);
            border: 1px solid rgba(0,0,0,0.05);
            border-radius: 16px;
            padding: 18px 20px;
            box-shadow: 0 8px 24px rgba(0,0,0,0.08);
        }}
        .muted {{
            color: var(--muted);
        }}
        .accent {{
            color: var(--accent-2);
            font-weight: 600;
        }}
        .stButton > button {{
            background: var(--accent);
            color: var(--btn-text);
            border: none;
            border-radius: 10px;
            padding: 8px 14px;
            font-weight: 600;
        }}
        .stTextInput > div > div > input {{
            background: #ffffff;
            border-radius: 10px;
        }}
        </style>
        """,
        unsafe_allow_html=True,
    )

def goto_step(step):
    st.session_state.step = step

def next_step():
    st.session_state.step = min(5, st.session_state.step + 1)

def prev_step():
    st.session_state.step = max(1, st.session_state.step - 1)

st.title("Valentine Week Journey")
st.write("A gentle, playful journey for someone who is a friend (for now).")

theme_name = st.selectbox(
    "Choose a color theme",
    list(THEMES.keys()),
    index=list(THEMES.keys()).index(st.session_state.theme_name),
)
st.session_state.theme_name = theme_name
apply_theme(THEMES[theme_name])

if not st.session_state.started:
    st.subheader("Before we begin")
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.write(
        "I was bored, scrolling through a quiet evening, when it hit me: "
        "it’s Valentine’s Week. Instead of overthinking it, I decided to make "
        "something small and simple—just a little journey, made because… why not."
    )
    st.write(
        "It’s subtle on purpose. No big declarations—just soft notes, gentle "
        "moments, and a vibe that feels like us."
    )
    if st.button("Start the journey"):
        st.session_state.started = True
    st.markdown("</div>", unsafe_allow_html=True)
    st.stop()

with st.container():
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.caption("Progress")
    st.progress((st.session_state.step - 1) / 4)
    st.markdown("</div>", unsafe_allow_html=True)

st.divider()

col1, col2, col3 = st.columns([1, 1, 1])
with col1:
    st.button("Step 1", on_click=goto_step, args=(1,))
with col2:
    st.button("Step 2", on_click=goto_step, args=(2,))
with col3:
    st.button("Step 3", on_click=goto_step, args=(3,))

col4, col5 = st.columns([1, 1])
with col4:
    st.button("Step 4", on_click=goto_step, args=(4,))
with col5:
    st.button("Step 5", on_click=goto_step, args=(5,))

st.divider()

if st.session_state.step == 1:
    st.subheader("Step 1: February 7 — Soft start")
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    name = st.text_input("Your name", "Friend")
    vibe = st.slider("How are you feeling today?", 0, 10, 7)
    if st.button("Open the door"):
        st.success(f"Welcome in, {name}. Your vibe level is {vibe}/10.")
    st.markdown(
        "<p class='muted'>This is a cozy start. Next comes tiny surprises.</p>",
        unsafe_allow_html=True,
    )
    st.markdown("</div>", unsafe_allow_html=True)

elif st.session_state.step == 2:
    st.subheader("Step 2: Little Valentine notes")
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.write("Pick a note to reveal:")
    c1, c2, c3 = st.columns(3)
    with c1:
        if st.button("Note 1"):
            st.info("You make ordinary days feel lighter.")
    with c2:
        if st.button("Note 2"):
            st.info("I like how easy it is to be around you.")
    with c3:
        if st.button("Note 3"):
            st.info("Thanks for being my calm in the noise.")
    st.markdown("</div>", unsafe_allow_html=True)

elif st.session_state.step == 3:
    st.subheader("Step 3: Valentine playlist + films")
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.write("Here are some picks. Replace these with your real links.")
    st.markdown(
        """
        **Music**
        - [Song 1](https://open.spotify.com/)
        - [Song 2](https://music.youtube.com/)
        - [Song 3](https://soundcloud.com/)

        **Movies**
        - [Movie 1](https://www.imdb.com/)
        - [Movie 2](https://www.netflix.com/)
        - [Movie 3](https://www.primevideo.com/)
        """,
    )
    choice = st.radio("Pick the vibe for tonight", ["Soft", "Playful", "Cozy"], index=0)
    st.success(f"Tonight's vibe: {choice}")
    st.markdown("</div>", unsafe_allow_html=True)

elif st.session_state.step == 4:
    st.subheader("Step 4: Tiny favorites")
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    q1 = st.selectbox("Coffee order?", ["Latte", "Mocha", "Cold brew", "Tea"])
    q2 = st.selectbox("Valentine snack?", ["Chocolate", "Strawberries", "Popcorn", "Cookies"])
    q3 = st.selectbox("Sweet or savory?", ["Sweet", "Savory"])
    if st.button("Reveal my guess"):
        st.info(f"My guess: {q1}, {q2}, and {q3}.")
    st.markdown("</div>", unsafe_allow_html=True)

elif st.session_state.step == 5:
    st.subheader("Step 5: A small promise")
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.write("We’re in different cities, so this stays gentle and simple.")
    col_yes, col_no = st.columns(2)
    with col_yes:
        if st.button("Send a note"):
            st.success("A tiny note goes a long way. I’m glad you’re here.")
    with col_no:
        if st.button("Keep it quiet"):
            st.info("Quiet is good too. This is enough.")
    with st.expander("Final message"):
        st.write(
            "Thanks for being here. This week is just a small way to say you matter."
        )
    st.markdown("</div>", unsafe_allow_html=True)

st.divider()
nav_col1, nav_col2 = st.columns(2)
with nav_col1:
    st.button("Back", on_click=prev_step, disabled=st.session_state.step == 1)
with nav_col2:
    st.button("Next", on_click=next_step, disabled=st.session_state.step == 5)

st.caption("Customize the notes and links inside `app.py`.")
