
import streamlit as st
import pandas as pd
from urllib.error import URLError
from streamlit.source_util import _on_pages_changed, get_pages
from streamlit_extras.switch_page_button import switch_page
import sys
from pages import login
from extra_streamlit_components import CookieManager

if "login_status" not in st.session_state:
    st.session_state['login_status'] = False


def log_out():
    st.session_state['login_status'] = False
    switch_page("sign_up")

st.title('WasteDrop')

st.write("Home Page")

if(st.session_state["login_status"] == True):
    st.write("Welcome!")
    with st.sidebar:
        logout_button = st.button("Log off", on_click=log_out())
else:
    st.write("Please login to continue")
