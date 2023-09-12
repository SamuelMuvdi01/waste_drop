import streamlit as st
import pandas
import requests
from urllib.error import URLError
import mysql.connector


st.title('WasteDrop')

st.write("Home Page")

cnx = mysql.connector.connect(user="wastedrop_admin", password="Team_7_pass$", host="waste-drop-server.mysql.database.azure.com", port=3306, database="wastedrop_db", ssl_ca="DigiCertGlobalRootCA.crt.pem", ssl_disabled=False)

cursor = cnx.cursor()

query = ("SELECT * from wastedrop_db.users")

"""
conn = mysql.connector.connect(**st.secrets["mysql"])

@st.cache_data(ttl=600)
def run_query(query):
    with conn.cursor() as cur:
        cur.execute(query)
        return cur.fetchall()
    
rows = run_query("SELECT * FROM wastedrop_db.users")

print(rows)
"""