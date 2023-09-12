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
    ssl_disabled=st.secrets.mysql.ssl_disabed
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

