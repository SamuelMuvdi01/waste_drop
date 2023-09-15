import streamlit as st
from streamlit.source_util import _on_pages_changed, get_pages
from streamlit_extras.switch_page_button import switch_page


st.set_page_config(page_title="login")

st.title("Please login!")

def clear_inputs():
    st.session_state['email'] = ""
    st.session_state['password'] = ""

if st.button("Sign Up"):
    switch_page("sign_up")
