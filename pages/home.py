
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


    cursor = conn.cursor()



    st.write("Welcome! ",st.session_state["saved_user_name"])
    logout_button = st.sidebar.button("log off", on_click=log_out)
    user_id = st.session_state["saved_user_id"]
    user_id = user_id.replace("'", "").replace("[", "").replace("]", "")
    st.header("Create new Binz below")
    binz_name = st.text_input("Enter the name of binz to create")
    create_binz_but = st.button("Create")

    cursor.execute("SELECT binz_name FROM public.binz_owners WHERE user_id = '{}';".format(user_id))
    user_binz_list = cursor.fetchall()
    st.write(user_binz_list)

    if create_binz_but:
            for i in user_binz_list:
                if(i in user_binz_list):
                    st.error(":red[This binz already exists!]")
            else:
                cursor.execute("INSERT INTO public.binz_owners(binz_name, user_id) VALUES('{}', '{}')".format(binz_name, user_id))
                conn.commit()
                st.write(":green[Binz created!]")



    st.header('View all binz')
    cursor.execute("SELECT binz_name FROM public.binz_owners WHERE user_id = '{}';".format(user_id))
    binz_results = cursor.fetchall()
    binz_results = pd.DataFrame(binz_results, columns=['Binz Name'])
    st.dataframe(binz_results)



    

else:
    st.write("Please login to continue")
