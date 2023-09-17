import streamlit as st
from streamlit.source_util import _on_pages_changed, get_pages
import streamlit_authenticator as stauth
from streamlit_extras.switch_page_button import switch_page
import psycopg2

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
    hashed_password = stauth.Hasher(password_login).generate()
    hashed_password = str(hashed_password[1])
    login_query = "SELECT * FROM public.users WHERE email ilike '{}' AND password = '{}'".format(email_login, hashed_password)
    if(cursor.fetchone() != None):
        st.write("Login successful!")
        switch_page("home")
    else:
        st.write("Invalid email or password.")

if st.button("Sign Up"):
    switch_page("sign_up")
