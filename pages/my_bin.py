import streamlit as st
import pandas as pd
from urllib.error import URLError
from streamlit.source_util import _on_pages_changed, get_pages
from streamlit_extras.switch_page_button import switch_page
import sys
from extra_streamlit_components import CookieManager
import psycopg2
import helperfuncs as hf
from pages.home import conn

if "login_status" not in st.session_state:
    st.session_state['login_status'] = False

if "saved_user_id" not in st.session_state:
    st.session_state["saved_user_id"] = ""

if "selected_binz" not in st.session_state:
    st.session_state["selected_binz"] = ""

if(st.session_state["login_status"] == False):
    st.write('PLEASE LOG IN!')
else:


    st.title(st.session_state["selected_binz"])

   
    cursor = conn.cursor()

    def log_out():
        st.session_state['login_status'] = False
        switch_page("sign_up")

    
    binz_item = st.text_input("Add an Item to bin: ")
    exp_date = st.date_input("Please Enter Item Expiration: ")
    count = st.number_input("Please Enter Item Quantity: ", step=1, min_value=1)
    add_binz_item = st.button("Add Item")
    binz_uuid = st.session_state["selected_binz"]
    logout_button = st.sidebar.button("Log Off", on_click=log_out)

    cursor.execute("INSERT INTO public.items(binz_id, quantity, expiry_date) VALUES('{}', '{}', '{}')".format(binz_uuid, count, exp_date))
    conn.commit()
    st.write(":green[Item Added!]")