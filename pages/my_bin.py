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
from datetime import datetime

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
    binz_name = st.session_state["selected_binz"]
    cursor.execute("SELECT binz_id FROM public.binz_owners WHERE binz_name = '{}' and user_id = '{}';".format(binz_name, user_id))
    binz_uuid = cursor.fetchone()
    binz_uuid = binz_uuid[0]

    crud_status = 'add'

    if crud_status == 'add':
        binz_item = st.text_input("Add an Item to bin: ")
        exp_date = st.date_input("Please Enter Item Expiration: ")
        count = st.number_input("Please Enter Item Quantity: ", step=1, min_value=1)
        add_binz_item = st.button("Add Item")
        now = datetime.now().date()  # Convert datetime to date
        
        if add_binz_item and len(binz_item) >= 2:
            if exp_date < now:
                st.error('Date must be greater than today!')
            else:
                cursor.execute("INSERT INTO public.items(binz_id, quantity, expiry_date, item_name) VALUES('{}', '{}', '{}', '{}')".format(binz_uuid, count, exp_date, binz_item))
                conn.commit()
                st.write(":green[Item Added!]")
        elif add_binz_item and len(binz_item) < 2:
            st.error("Binz item must have a name!")
    
    elif crud_status == 'updt':
        item_name_updt = st.text_input("Enter name of item you wish to update")
        updt_quantity = st.number_input("Please Enter Item Quantity: ", step=1, min_value=1)
        updt_button = st.button("update item")
        if updt_button:
            cursor.execute("UPDATE public.items SET quantity = '{}' WHERE item_name = '{}' and binz_id = '{}';".format(updt_quantity, item_name_updt, binz_uuid))
            st.write(":green[Item updated!]")


    
    cursor.execute("SELECT item_name, quantity, timestamp, expiry_date FROM public.items WHERE binz_id= '{}';".format(binz_uuid))
    items_results = cursor.fetchall()
    item_results_frame = pd.DataFrame(items_results, columns = ['item_name', 'quantity', 'added_on_date', 'expiry_date'])
  
    st.data_editor(item_results_frame, use_container_width=True, hide_index=True, disabled=True)
