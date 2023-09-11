import streamlit as st
import pandas
import requests
from urllib.error import URLError

st.title('WasteDrop')

st.write("Home Page")

conn = st.experimental_connection('mysql', type='sql')

# Perform query.
df = conn.query('SELECT * from wastedrop_db.users;', ttl=600)

print(df)