import streamlit as st
from config import APP_TITLE

def set_page_config():
    st.set_page_config(
        page_title=APP_TITLE,
        page_icon="🛒",
        layout="wide"
    )

def apply_custom_style():
    st.markdown(
        """
        <style>
            .stApp {
                background-color: #87CEEB;
                color: black;
            }
            .stMarkdown, .stTitle, .stTextInput > label, .stCheckbox > label {
                color: black;
            }
        </style>
        """,
        unsafe_allow_html=True
    )