import streamlit as st
from content import PALETTES

def apply_theme(mood):
    palette = PALETTES.get(mood, PALETTES[None])

    st.markdown(
        f"""
        <style>
        html, body, .stApp {{
            background-color: {palette['bg']} !important;
            transition: background-color 0.4s ease;
        }}

        h1, h2, h3 {{
            color: {palette['accent']} !important;
            font-family: 'Playfair Display', Georgia, serif;
        }}

        p, label {{
            color: {palette['accent']} !important;
            font-family: 'Inter', Arial, sans-serif;
            font-size: 16px;
            line-height: 1.65;
        }}

        .soft {{
            background: rgba(255,255,255,0.25);
            border-radius: 14px;
            padding: 1.2em 1.4em;
        }}

        .stButton > button {{
            background: transparent;
            border: 1px solid {palette['accent']};
            color: {palette['accent']};
            border-radius: 22px;
            padding: 0.35em 1.3em;
        }}

        * {{
            cursor: url("https://emojiapi.dev/api/v1/chocolate_bar/32.png"), auto;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )
