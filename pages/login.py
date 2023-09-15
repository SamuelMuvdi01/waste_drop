import streamlit as st
from streamlit.source_util import _on_pages_changed, get_pages
from streamlit_extras.switch_page_button import switch_page
import psycopg2

st.set_page_config(page_title="Login")

st.title("Please login!")

@st.cache_resource
def init_connection():
    return psycopg2.connect(**st.secrets["postgres"])

conn = init_connection()

def run_query(query):
    with conn.cursor() as cur:
        cur.execute(query)
        return cur.fetchall()
    
email_login = st.text_input("Please enter email", placeholder="JohnDoe@gmail.com")
password_login = st.text_input("Please enter password", placeholder="*****")

if st.button("Sign Up"):
    switch_page("sign_up")
