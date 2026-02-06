import streamlit as st

st.set_page_config(page_title="Just a Small App", layout="centered")

if "page" not in st.session_state:
    st.session_state.page = 1

# ---------- PAGE 1 : STORY ----------
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

# ---------- PAGE 2 : VALENTINE WEEK ----------
elif st.session_state.page == 2:
    st.title("Valentine’s Week")

    st.subheader("🌹 Feb 7 — Rose Day")
    color = st.radio(
        "If today had a color, what would it be?",
        ["Soft red", "Pink-ish", "Yellow", "Something else"]
    )

    st.divider()

    st.subheader("💬 A small question")
    st.write("What’s something you enjoy talking about but don’t get to often?")

    answer = st.text_input("You don’t have to answer seriously.")

    st.divider()

    st.subheader("☕ Comfort pick")
    comfort = st.selectbox(
        "After a long day, what sounds best?",
        ["Chocolate", "Coffee", "Sleep", "Music"]
    )

    st.write("That’s it. No pressure. Just vibes.")

