import streamlit as st
import pandas as pd
from urllib.error import URLError
from streamlit.source_util import _on_pages_changed, get_pages
from streamlit_extras.switch_page_button import switch_page
import sys
from extra_streamlit_components import CookieManager
import psycopg2
import helperfuncs as hf
from pages.login import conn

st.title(st.session_state["selected_binz"])

def log_out():
    st.session_state['login_status'] = False
    switch_page("sign_up")

def back():
    switch_page("home")


binz_item = st.text_input("Add an Item to bin: ")
exp_date = st.date_input("Please Enter Item Expiration")
add_binz_item = st.button("Add Item")

logout_button = st.sidebar.button("Log Off", on_click=log_out)
back_button = st.sidebar.button("Back", on_click=back)