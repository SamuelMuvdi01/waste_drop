import streamlit as st
import pandas as pd
from urllib.error import URLError
from streamlit.source_util import _on_pages_changed, get_pages
from streamlit_extras.switch_page_button import switch_page
import sys
from pages import login

st.set_page_config(page_title="Home")

st.sidebar.success("Sign up or login!")

st.title('WasteDrop')

st.write("Home Page")

if(login.login_status == True):
    st.write("Welcome! ", login.user_first_name)
else:
    st.write("Please login to continue")