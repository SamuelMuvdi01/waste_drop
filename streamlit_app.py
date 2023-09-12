import streamlit as st
import pandas
import requests
from urllib.error import URLError
import pymysql


st.title('WasteDrop')

st.write("Home Page")

conn = pymysql.connect(
    host=st.secrets.mysql.host,
    user=st.secrets.mysql.user,
    password=st.secrets.mysql.password,
    port=st.secrets.mysql.port,
    database=st.secrets.mysql.database,
    ssl_disabled=st.secrets.mysql.ssl_disabled
    )

curr = conn.cursor()
curr.execute('SELECT * FROM wastedrop_db.users')
output = curr.fetchall()

for i in output:
    print(i)

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