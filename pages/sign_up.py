import streamlit as st
from streamlit.source_util import _on_pages_changed, get_pages
from streamlit_extras.switch_page_button import switch_page
import streamlit_authenticator as stauth
import re
import psycopg2

st.set_page_config(page_title="Sign_Up")
st.title("welcome, please sign up below")


@st.cache_resource
def init_connection():
    return psycopg2.connect(**st.secrets["postgres"])

conn = init_connection()
conn.autocommit = True

def run_query(query):
    with conn.cursor() as cur:
        cur.execute(query)
        return cur.fetchall()

def clear_inputs():
    st.session_state['first_name'] = ""
    st.session_state['last_name'] = ""
    st.session_state['email'] = ""
    st.session_state['password'] = ""

if "first_name" not in st.session_state:
    st.session_state['first_name'] = ""
if "last_name" not in st.session_state:
    st.session_state['last_name'] = ""
if "email" not in st.session_state:
    st.session_state['email'] = ""
if "password" not in st.session_state:
    st.session_state['password'] = ""

first_name_val = st.text_input("Please enter first name", placeholder="John", key="first_name")
last_name_val = st.text_input("Please enter last name", placeholder="Doe", key="last_name")
email_val = st.text_input("Please enter email", placeholder="JohnDoe@gmail.com", key="email")
password_val = st.text_input("Please enter a password", key="password", placeholder="********", help="Password must be at least 8 characters long, have an upper case letter, and have a symbol")
create_user_button = st.button("Create account", key="create_user_button")


clear_button = st.button("Clear", on_click=clear_inputs)
pass_email = bool(re.match(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b', email_val))
pass_valid= bool(re.match(r"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@#$%^&+=]).{8,}$", password_val ))

if(pass_valid == True and len(last_name_val) > 2 and len(last_name_val) > 2 and pass_email == True and create_user_button):
    hashed_password = stauth.Hasher(password_val).generate()
    for (hashed_passwords) in (hashed_password):
        run_query("INSERT INTO public.users(email, first_name, last_name, password) VALUES({}, {}, {}, {});".format(email_val, first_name_val, last_name_val, password_val))
conn.commit()
st.write("Account created!")