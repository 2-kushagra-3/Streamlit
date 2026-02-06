import streamlit as st

st.set_page_config(page_title="Just a Small App", layout="centered")

if "page" not in st.session_state:
    st.session_state.page = 1

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
    st.title("A small Valentine’s week experiment")

    st.write("""
    Valentine’s week has themes for each day.
    I figured I’d reinterpret them… quietly.
    """)

    st.subheader("🌹 Feb 7 — Rose Day (but not really)")

    mood = st.radio(
        "Pick a mood for today:",
        ["Calm", "Soft happy", "Slightly nostalgic", "Random energy"]
    )

    songs = {
        "Calm": {
            "title": "Coldplay – Sparks",
            "link": "https://open.spotify.com/track/7D0RhFcb3CrfPuTJ0obrod",
            "caption": "Low volume. No distractions."
        },
        "Soft happy": {
            "title": "Rex Orange County – Sunflower",
            "link": "https://open.spotify.com/track/0xY0i9l2E12LHG0L1r5Q3s",
            "caption": "Feels like a good afternoon."
        },
        "Slightly nostalgic": {
            "title": "Prateek Kuhad – Kasoor (Acoustic)",
            "link": "https://open.spotify.com/track/4A9tZpP0R9zRkD6rP8b0Fs",
            "caption": "Some songs just sit quietly."
        },
        "Random energy": {
            "title": "Lauv – Paris in the Rain",
            "link": "https://open.spotify.com/track/41CgzGD7xlgnJe14R4cqkL",
            "caption": "No particular reason. Just because."
        }
    }

    st.markdown(f"### 🎧 {songs[mood]['title']}")
    st.markdown(f"[Open song ↗]({songs[mood]['link']})")
    st.caption(songs[mood]['caption'])

    st.divider()

    st.write("Quick reaction (optional):")
    reaction = st.radio(
        "",
        ["This fits today", "Not my vibe", "Saving this"]
    )

    st.caption("That’s it for today. Nothing to overthink.")

