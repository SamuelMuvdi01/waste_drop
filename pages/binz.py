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

binz_item = st.text_input("Add an Item to bin: ")
create_binz_but = st.button("Create")