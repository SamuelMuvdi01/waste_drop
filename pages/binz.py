import streamlit as st
import streamlit_authenticator as stauth
from streamlit_extras.switch_page_button import switch_page
import psycopg2
import hashlib
import pandas as pd

st.set_page_config(page_title="binz")