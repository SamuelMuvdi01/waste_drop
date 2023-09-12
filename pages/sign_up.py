import streamlit as st
from streamlit.source_util import _on_pages_changed, get_pages
from streamlit_extras.switch_page_button import switch_page

st.set_page_config(page_title="sign_up")
st.title("welcome, please sign up below")

first_name = st.text_input("Please enter first name", placeholder="John")
last_name = st.text_input("Please enter last name", placeholder="Doe")
email = st.text_input("Please enter email", placeholder="JohnDoe@gmail.com")
