import streamlit as st
import pandas as pd
from urllib.error import URLError
import psycopg2



st.title('WasteDrop')

st.write("Home Page")


@st.cache_resource
def init_connection():
    return psycopg2.connect(**st.secrets["postgres"])

conn = init_connection()

def run_query(query):
    with conn.cursor() as cur:
        cur.execute(query)
        return cur.fetchall()
    
rows = run_query("SELECT * FROM public.users")





#cnx = mysql.connector.connect(user="wastedrop_admin", password="Team_7_pass$", host="waste-drop-server.mysql.database.azure.com", port=3306, database="wastedrop_db", ssl_ca="DigiCertGlobalRootCA.crt.pem", ssl_disabled=False)
#cursor = cnx.cursor()
#cursor.execute("SELECT * from wastedrop_db.users")
#result = cursor.fetchall()
#print(result)



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