import streamlit as st
from streamlit.source_util import _on_pages_changed, get_pages
from streamlit_extras.switch_page_button import switch_page
import streamlit_authenticator as stauth
import re
import psycopg2
import helperfuncs as hf
import hashlib

st.set_page_config(page_title="Sign_Up")

@st.cache_resource
def init_connection():
    return psycopg2.connect(**st.secrets["postgres"])

conn = init_connection()

cursor = conn.cursor()

def clear_inputs():
    st.session_state['first_name'] = ""
    st.session_state['last_name'] = ""
    st.session_state['email'] = ""
    st.session_state['password'] = ""

def log_out():
    st.session_state['login_status'] = False
    switch_page("sign_up")
    

if "first_name" not in st.session_state:
    st.session_state['first_name'] = ""
if "last_name" not in st.session_state:
    st.session_state['last_name'] = ""
if "email" not in st.session_state:
    st.session_state['email'] = ""
if "password" not in st.session_state:
    st.session_state['password'] = ""
if "login_status" not in st.session_state:
    st.session_state['login_status'] = False

if st.session_state["login_status"] == True:
    st.write("Please Log Out To Create a New Account!")
    logout_button = st.sidebar.button("Log Off", on_click=log_out)
    return_home_btn = st.button("Return to Home")
    if return_home_btn:
        switch_page("home")

else:
    st.title("Welcome, please sign up below")
    first_name_val = st.text_input("Please enter first name", placeholder="John", key="first_name")
    last_name_val = st.text_input("Please enter last name", placeholder="Doe", key="last_name")
    email_val = st.text_input("Please enter email", placeholder="JohnDoe@gmail.com", key="email")
    password_val = st.text_input("Please enter a password", key="password", placeholder="********", help="Password must be at least 8 characters long, have an upper case letter, and have a symbol")

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        create_user_button = st.button("Create account", key="create_user_button")
    with col3:
        if(st.button("Login")):
            switch_page("login")

    with col2:
        clear_button = st.button("Clear", on_click=clear_inputs)
        
    email_valid = bool(re.match(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b', email_val))
    pass_valid = bool(re.match(r"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@#$%^&+=!]).{8,}$", password_val))

    def email_exists(email):
        cursor.execute("SELECT email FROM public.users WHERE email ilike %s;", (email,))
        return cursor.fetchone() is not None

    def get_all_emails():
        cursor.execute("SELECT email FROM public.users WHERE email ilike %s;", (email_val,))
        return cursor.fetchall()

    if create_user_button:
        if pass_valid and len(last_name_val) > 2 and len(first_name_val) > 2 and email_valid:
            hashed_password = "SHA-512:" + hashlib.sha512(password_val.encode('utf-8')).hexdigest()
            try:
                existing_emails = get_all_emails()
                if any(email_val in row for row in existing_emails):
                    st.error(":red[This email is already in use!]")
                else:
                    cursor.execute("INSERT INTO public.users(email, first_name, last_name, password) VALUES(%s, %s, %s, %s);",
                                   (email_val, hf.capitalize(first_name_val), hf.capitalize(last_name_val), hashed_password))
                    conn.commit()
                    st.write(":green[Account created!]")
            except Exception as e:
                print(f"Error during user creation: {e}")
                st.error(":red[Error creating the account. Please try again later.]")

        if pass_valid is False:
            st.error(":red[Oops! The password isn't strong enough, please check the question mark for criteria!]")
        if email_valid is False:
            st.error(":red[Oops! The email is not complete!]")
        if len(first_name_val) < 2:
            st.error(":red[Please enter a valid first name!]")
        if len(last_name_val) < 2:
            st.error(":red[Please enter a valid last name!]")