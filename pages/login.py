import streamlit as st
from streamlit.source_util import _on_pages_changed, get_pages
import streamlit_authenticator as stauth
from streamlit_extras.switch_page_button import switch_page
import psycopg2

st.set_page_config(page_title="Login")
st.title("Welcome, please log in below")

@st.cache_resource
def init_connection():
    return psycopg2.connect(**st.secrets["postgres"])

conn = init_connection()
conn.autocommit = True
cursor = conn.cursor()

def authenticate_user(email, password):
    cursor.execute("SELECT * FROM public.users WHERE email=%s", (email,))
    user = cursor.fetchone()
    if user:
        hashed_password = user[3]
        # Add a '[' character to the front of the stored hashed password
        hashed_password = '[' + hashed_password
        if stauth.Hasher.verify(password, hashed_password):
            return True
    return False

email_val = st.text_input("Email", key="email")
password_val = st.text_input("Password", key="password", type="password")

login_button = st.button("Login", key="login_button")

if login_button:
    if email_val and password_val:
        if authenticate_user(email_val, password_val):
            st.write("Login successful!")
            # Add code here to redirect to a dashboard or another page
        else:
            st.error("Invalid email or password")
    else:
        st.error("Please enter both email and password")

if st.button("Sign Up"):
    switch_page("sign_up")
