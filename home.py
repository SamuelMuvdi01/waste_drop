import streamlit as st
import pandas as pd
from urllib.error import URLError
from streamlit.source_util import _on_pages_changed, get_pages
from streamlit_extras.switch_page_button import switch_page

st.set_page_config(page_title="Home")

st.sidebar.success("Sign up or login!")

st.title('WasteDrop')

st.write("Home Page")

