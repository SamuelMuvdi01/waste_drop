import streamlit as st
import pandas
import requests
from urllib.error import URLError
import mysql.connector

st.title('WasteDrop')

st.write("Home Page")

conn = mysql.connector.connect(**st.secrets["mysql"])

@st.cache_data(ttl=600)
def run_query(query):
    with conn.cursor() as cur:
        cur.execute(query)
        return cur.fetchall()
    
rows = run_query("SELECT * FROM wastedrop_db.users")

print(rows)