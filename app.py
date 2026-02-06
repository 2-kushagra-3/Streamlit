import streamlit as st

st.set_page_config(page_title="Streamlit Cloud Starter", page_icon="??", layout="centered")

st.title("Streamlit Cloud Starter")
st.write("This is a minimal example app you can deploy on Streamlit Community Cloud.")

st.subheader("Demo")
name = st.text_input("Your name", "World")
if st.button("Say hello"):
    st.success(f"Hello, {name}!")

st.caption("Edit `app.py` to start building your app.")
