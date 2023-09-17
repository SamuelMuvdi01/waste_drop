import streamlit as st
from streamlit.source_util import _on_pages_changed, get_pages
from streamlit_extras.switch_page_button import switch_page
import streamlit_authenticator as stauth
import re
import psycopg2
import helperfuncs as hf
import hashlib

st.set_page_config(page_title="Sign_Up")
st.title("Welcome, please sign up below")


@st.cache_resource
def init_connection():
    return psycopg2.connect(**st.secrets["postgres"])

conn = init_connection()
conn.autocommit = True

cursor = conn.cursor()

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
email_valid = bool(re.match(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b', email_val))
pass_valid = bool(re.match(r"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@#$%^&+=!]).{8,}$", password_val))


def get_all_emails():
    cursor.execute("SELECT email FROM public.users WHERE email ilike '{}';".format(email_val))
    return cursor.fetchone()


if create_user_button:
    if pass_valid and len(last_name_val) > 2 and len(first_name_val) > 2 and email_valid:
        hashed_password = "md5" + hashlib.md5(password_val).hexdigest()
        try:
            cursor.execute("INSERT INTO public.users(email, first_name, last_name, password) VALUES('{}', '{}', '{}', '{}')".format(email_val, hf.capitalize(first_name_val), hf.capitalize(last_name_val), hashed_password))
            conn.commit()
            st.write(":green[Account created!]")
        except:
            if(email_val in get_all_emails()):
                st.error(":red[This email already is in use!]")
            else:
                st.error(":red[One of the fields above are invalid!]")
  
    if(pass_valid==False):
            st.error(":red[Oops! The password isnt strong enough, please check the question mark for criteria!]")
    if(email_valid == False):
             st.error(":red[Oops! The email is not complete!]")
    if(len(first_name_val) < 2):
         st.error(":red[Please enter a valid first name!]")
    if(len(last_name_val) < 2):
         st.error(":red[Please enter a valid last name!]")

