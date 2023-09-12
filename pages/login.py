import streamlit as st
from pages import login
from multiapp import MultiApp
from pages import sign_up
app = MultiApp

st.set_page_config(page_title="login")

st.title("Please login!")


app.add_app("Sign Up", sign_up.app)