import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "model")))
import streamlit as st
from pages._pages import home
from pages._pages import try_it

routes = {
    "Home": home.main,
    "Try it out": try_it.main,
}

st.set_page_config(
    page_title="Brain Tumor Detection",
    page_icon=":brain:",
    layout="wide",
    menu_items={
        "Get Help": "https://github.com/Oct4Pie/brain-tumor-detection",
        "Report a bug": "https://github.com/Oct4Pie/brain-tumor-detection/issues",
        "About": "Detecting brain tumors using *deep Convolutional Neural Networks*",
    },
    initial_sidebar_state="collapsed",
)

st.markdown(
    """
<style>
    [data-testid="collapsedControl"] {
        display: none
    }
   [data-testid="stSelectbox"] .st-emotion-cache-13bfgw8 p {
        font-size: 24px;
        font-weight: bold;
    }
</style>
""",
    unsafe_allow_html=True,
)

def format_func(page):
    return page[0]

page = st.selectbox(
    "Menu",
    list(routes.items()),
    index=0,
    format_func=format_func,
)

page[1]()
