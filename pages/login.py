import streamlit as st
from streamlit.source_util import _on_pages_changed, get_pages
import streamlit_authenticator as stauth
from streamlit_extras.switch_page_button import switch_page
import psycopg2
import hashlib
import pandas as pd

st.set_page_config(page_title="login")


if "saved_user_name" not in st.session_state:
    st.session_state["saved_user_name"] = ""

if "login_status" not in st.session_state:
    st.session_state['login_status'] = False

st.title("Welcome, please log in below")

@st.cache_resource
def init_connection():
    return psycopg2.connect(**st.secrets["postgres"])

@st.cache_resource
def logged_in():
    st.session_state["login_status"] = True
    switch_page("home")
    

conn = init_connection()

cursor = conn.cursor()


columns_db = ["id", "email", "first_name", "last_name", "timestamp", "password"]
email_login = st.text_input("Please enter email", placeholder="JohnDoe@gmail.com")
password_login = st.text_input("Please enter password", type="password", placeholder="********")

col1, col2, col3, col4 = st.columns(4)
with col1:
    login_button = st.button("Login")

if login_button:
    hashed_password ="SHA-512:" + hashlib.sha512(password_login.encode('utf-8')).hexdigest()
    cursor.execute("SELECT * FROM public.users WHERE email ilike '{}' AND password = '{}'".format(email_login, hashed_password))
    login_results_query = cursor.fetchall()
    query_df = pd.DataFrame(login_results_query,columns=columns_db)

    @st.cache_resource
    def save_user_name():
        st.session_state["saved_user_name"] = query_df["last_name"].values

    if(hashed_password == query_df["password"].values):
        save_user_name()
        logged_in()
    else:
        st.write("Invalid email or password.")

with col2:
    if st.button("Sign Up"):
        switch_page("sign_up")
