import streamlit as st
import pandas as pd
from urllib.error import URLError
import psycopg2
from streamlit.source_util import _on_pages_changed, get_pages
from streamlit_extras.switch_page_button import switch_page

st.set_page_config(page_title="home")

st.sidebar.success("Sign up or login!")

st.title('WasteDrop')

st.write("Home Page")

"""

@st.cache_resource
def init_connection():
    return psycopg2.connect(**st.secrets["postgres"])

conn = init_connection()

def run_query(query):
    with conn.cursor() as cur:
        cur.execute(query)
        return cur.fetchall()
    
rows = run_query("SELECT * FROM public.users")

st.write(rows)
"""