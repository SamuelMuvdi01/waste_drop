import streamlit as st
from streamlit.source_util import _on_pages_changed, get_pages
from streamlit_extras.switch_page_button import switch_page
import streamlit_authenticator as stauth
import re

st.set_page_config(page_title="sign_up")
st.title("welcome, please sign up below")





first_name = st.text_input("Please enter first name", placeholder="John", key="first_name")
last_name = st.text_input("Please enter last name", placeholder="Doe", key="last_name")
email = st.text_input("Please enter email", placeholder="JohnDoe@gmail.com", key="email")
password = st.text_input("Please enter a password", key="password", placeholder="xxxxxxxx", help="Password must be at least 8 characters long, have an upper case letter, and have a symbol")
create_user_button = st.button("Create account", key="create_user_button")


if first_name not in st.session_state:
    st.session_state['first_name']
if last_name not in st.session_state:
    st.session_state['last_name']
if email not in st.session_state:
    st.session_state['email']
if password not in st.session_state:
    st.session_state['password']


def clear_inputs():
    st.session_state['first_name'] = ""
    st.session_state['last_name'] = ""
    st.session_state['email'] = ""
    st.session_state['password'] = ""



clear_button = st.button("Clear", on_click=clear_inputs)
pass_valid= bool(re.match(r"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@#$%^&+=]).{8,}$", password ))




