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
clear_button = st.button("Clear")
pass_valid= bool(re.match(r"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@#$%^&+=]).{8,}$", password ))


if(clear_button):
    first_name = st.empty(),
    last_name = st.empty(),
    email = st.empty(),
    password = st.empty()

