import streamlit as st
from streamlit.source_util import _on_pages_changed, get_pages
import streamlit_authenticator as stauth
from streamlit_extras.switch_page_button import switch_page
import psycopg2
import hashlib
import pandas as pd

st.set_page_config(page_title="Login")
st.title("Welcome, please log in below")

@st.cache_resource
def init_connection():
    return psycopg2.connect(**st.secrets["postgres"])

columns_db = ["id", "email", "first_name", "last_name", "timestamp", "password"]

conn = init_connection()

cursor = conn.cursor()



email_login = st.text_input("Please enter email", placeholder="JohnDoe@gmail.com")
password_login = st.text_input("Please enter password", type="password", placeholder="********")

login_button = st.button("Login")

if login_button:
    hashed_password ="SHA-512:" + hashlib.sha512(password_login.encode('utf-8')).hexdigest()
    cursor.execute("SELECT * FROM public.users WHERE email ilike '{}' AND password = '{}'".format(email_login, hashed_password))
    login_results_query = cursor.fetchall()
    query_df = pd.DataFrame(login_results_query,columns=columns_db)
    st.write("hashed password: ", hashed_password)
    st.write("password from db: ", query_df["password"])
    if(hashed_password == query_df["password"].values):
        switch_page("home")
    else:
        st.write("Invalid email or password.")

if st.button("Sign Up"):
    switch_page("sign_up")
