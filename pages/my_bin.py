import streamlit as st
import pandas as pd
from urllib.error import URLError
from streamlit.source_util import _on_pages_changed, get_pages
from streamlit_extras.switch_page_button import switch_page
import sys
from extra_streamlit_components import CookieManager
import psycopg2
import helperfuncs as hf
from pages.home import conn

if "login_status" not in st.session_state:
    st.session_state['login_status'] = False

if "saved_user_id" not in st.session_state:
    st.session_state["saved_user_id"] = ""

if "selected_binz" not in st.session_state:
    st.session_state["selected_binz"] = ""

if(st.session_state["login_status"] == False):
    st.write('PLEASE LOG IN!')
else:
    pass