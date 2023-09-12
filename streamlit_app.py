import streamlit as st
import pandas as pd
import requests
from urllib.error import URLError



st.title('WasteDrop')

st.write("Home Page")


conn = st.experimental_connection('mysql', type='sql')

df = conn.query('SELECT * from wastedrop_db.users')

for row in df.itertuples():
    st.write(f"{row.last_name}")




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