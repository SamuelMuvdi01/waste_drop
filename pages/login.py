import streamlit as st
from streamlit.source_util import _on_pages_changed, get_pages
import streamlit_authenticator as stauth
from streamlit_extras.switch_page_button import switch_page
import psycopg2
import bcrypt

st.set_page_config(page_title="Login")
st.title("Welcome, please log in below")

@st.cache_resource
def init_connection():
    return psycopg2.connect(**st.secrets["postgres"])

conn = init_connection()

cursor = conn.cursor()
    


email_login = st.text_input("Please enter email", placeholder="JohnDoe@gmail.com")
password_login = st.text_input("Please enter password", type="password", placeholder="********")

login_button = st.button("Login")

if login_button:
    hashed_password = bcrypt.hashpw(password_login, bcrypt.gensalt(12))
    st.write(hashed_password)
    cursor.execute("SELECT * FROM public.users WHERE email ilike '{}' AND password = '{}'".format(email_login, hashed_password))
    query_results = ''
    for que in cursor.fetchall():
        query_results = que
    st.write(query_results)

    #if(cursor.fetchone() != None):
      #  st.write("Login successful!")
      #  switch_page("home")
  # else:
   #     st.write("Invalid email or password.")

if st.button("Sign Up"):
    switch_page("sign_up")
