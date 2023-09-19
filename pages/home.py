
import streamlit as st
import pandas as pd
from urllib.error import URLError
from streamlit.source_util import _on_pages_changed, get_pages
from streamlit_extras.switch_page_button import switch_page
import sys
from extra_streamlit_components import CookieManager
import pages.login

if "login_status" not in st.session_state:
    st.session_state['login_status'] = False


def log_out():
    st.session_state['login_status'] = False
    switch_page("sign_up")


st.title('WasteDrop')


if(st.session_state["login_status"] == True):
    st.write("Welcome! ",pages.login.st.session_state["saved_user_name"])
    logout_button = st.sidebar.button("log off", on_click=log_out)
    

else:
    st.write("Please login to continue")
