import streamlit as st
import pandas as pd
from urllib.error import URLError
from streamlit.source_util import _on_pages_changed, get_pages
from streamlit_extras.switch_page_button import switch_page
import sys
from extra_streamlit_components import CookieManager
import psycopg2
import helperfuncs as hf
from pages.login import conn
import pages.home as hm
import time

if "login_status" not in st.session_state:
    st.session_state['login_status'] = False

if "saved_user_id" not in st.session_state:
    st.session_state["saved_user_id"] = ""

if "selected_binz" not in st.session_state:
    st.session_state["selected_binz"] = ""

if(st.session_state["login_status"] == False):
    st.write('PLEASE LOG IN!')
else:

    cursor = conn.cursor()

    st.title(st.session_state["selected_binz"])

    user_id = st.session_state["saved_user_id"]
    user_id = user_id.replace("'", "").replace("[", "").replace("]", "")

    binz_item = st.text_input("Add an Item to bin: ")
    exp_date = st.date_input("Please Enter Item Expiration: ")
    count = st.number_input("Please Enter Item Quantity: ", step=1, min_value=1)
    add_binz_item = st.button("Add Item")
    binz_name = st.session_state["selected_binz"]
    time.sleep(3)
    cursor.execute("SELECT binz_id FROM public.binz_owners WHERE binz_name = '{}' and user_id = '{}';").format(binz_name, user_id)
    binz_uuid = cursor.fetchone()




    #cursor.execute("INSERT INTO public.items(binz_id, quantity, expiry_date) VALUES('{}', '{}', '{}')".format(binz_uuid, count, exp_date))
    #cursor.commit()
    #st.write(":green[Item Added!]")