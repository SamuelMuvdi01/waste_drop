
import streamlit as st
import pandas as pd
from urllib.error import URLError
from streamlit.source_util import _on_pages_changed, get_pages
from streamlit_extras.switch_page_button import switch_page
import sys
from extra_streamlit_components import CookieManager
import psycopg2
import helperfuncs as hf


if "login_status" not in st.session_state:
    st.session_state['login_status'] = False

if "saved_user_name" not in st.session_state:
    st.session_state["saved_user_name"] = ""

if "saved_user_id" not in st.session_state:
    st.session_state["saved_user_id"] = ""


def log_out():
    st.session_state['login_status'] = False
    switch_page("sign_up")


st.title('WasteDrop')


if(st.session_state["login_status"] == True):

    @st.cache_resource
    def init_connection():
        return psycopg2.connect(**st.secrets["postgres"])

    conn = init_connection()

    cursor = conn.cursor()

    def get_all_binz_names():
        cursor.execute("SELECT binz_name FROM public.binz_owners WHERE user_id = '{}';".format(user_id))
        return cursor.fetchone()

    st.write("Welcome! ",st.session_state["saved_user_name"])
    logout_button = st.sidebar.button("log off", on_click=log_out)
    user_id = st.session_state["saved_user_id"]
    st.header("Create new Binz below")
    st.write(user_id)
    binz_name = st.text_input("Enter the name of binz to create")
    create_binz_but = st.button("Create")

    if create_binz_but:
        try:
            cursor.execute("INSERT INTO public.binz_owners(binz_name, user_id) VALUES('{}', '{}')".format(hf.capitalize(binz_name), user_id))
        except:
            if(binz_name in get_all_binz_names()):
                st.error(":red[This binz already exists!]")


    st.header('View all binz')
    cursor.execute("SELECT binz_name FROM public.binz_owners WHERE user_id = '{}';".format(user_id))
    binz_results = cursor.fetchall()
    st.dataframe(binz_results)



    

else:
    st.write("Please login to continue")
