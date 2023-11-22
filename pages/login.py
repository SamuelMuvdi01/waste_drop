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

if "saved_user_id" not in st.session_state:
    st.session_state["saved_user_id"] = ""

if "login_status" not in st.session_state:
    st.session_state['login_status'] = False

def log_out():
    st.session_state['login_status'] = False
    switch_page("sign_up")

@st.cache_resource
def init_connection():
    return psycopg2.connect(**st.secrets["postgres"])

@st.cache_resource
def logged_in():
    st.session_state["login_status"] = True
    switch_page("home")
    
if st.session_state["login_status"] == True:
     st.write("Successfully Logged In!")
     logout_button = st.sidebar.button("Log Off", on_click=log_out)
     return_home_btn = st.button("Return to Home")
     if return_home_btn:
        switch_page("home")

else:
    st.title("Welcome, please log in below")
    conn = init_connection()

    cursor = conn.cursor()


    columns_db = ["id", "first_name", "last_name", "email", "timestamp", "password"]
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

        def save_user_name():
            st.session_state["saved_user_name"] = str(query_df["first_name"].values)

        def save_user_id():
            st.write("id val as string", str(query_df["id"].values))
            st.session_state["saved_user_id"] = str(query_df["id"].values)

        if(hashed_password == query_df["password"].values):
            save_user_name()
            save_user_id()
            st.session_state["login_status"] = True
            logged_in()
        else:
            st.write("Invalid email or password.")

    with col2:
        if st.button("Sign Up"):
            switch_page("sign_up")