import streamlit as st
import pandas
import requests
from urllib.error import URLError
import mysql.connector

st.title('WasteDrop')

st.write("Home Page")

conn = st.experimental_connection('mysql', type='sql')
df = conn.query('SELECT * from wastedrop_db.users;', ttl=600)

