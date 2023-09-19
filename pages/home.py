
import streamlit as st
import pandas as pd
from urllib.error import URLError
from streamlit.source_util import _on_pages_changed, get_pages
from streamlit_extras.switch_page_button import switch_page
import sys
from st_pages import Page, show_pages, hide_pages
from extra_streamlit_components import CookieManager

if "login_status" not in st.session_state:
    st.session_state['login_status'] = False

show_pages([
    Page("sign_up.py","sign_up"),
    Page("login.py", "login")
        ])


def log_out():
    st.session_state['login_status'] = False
    switch_page("sign_up")
    hide_pages([
    Page("sign_up.py","sign_up"),
    Page("pages/login.py", "login")
        ])
    

st.title('WasteDrop')

st.write("Home Page")

if(st.session_state["login_status"] == True):
    st.write("Welcome!")
    logout_button = st.sidebar.button("log off", on_click=log_out)

else:
    st.write("Please login to continue")
