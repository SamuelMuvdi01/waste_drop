import streamlit as st
import pandas as pd
import psycopg2
from streamlit_extras.switch_page_button import switch_page
from extra_streamlit_components import CookieManager
from pages.login import conn

if "saved_user_name" not in st.session_state:
    st.session_state["saved_user_name"] = ""

if "saved_user_id" not in st.session_state:
    st.session_state["saved_user_id"] = ""

if "login_status" not in st.session_state:
    st.session_state['login_status'] = False

def log_out():
    st.session_state['login_status'] = False
    switch_page("sign_up")

def switch_to_binz_page():
    switch_page("my_bin")

def delete_bin(binz_name, user_id):
    cursor = conn.cursor()
    cursor.execute("DELETE FROM public.binz_owners WHERE binz_name = '{}' AND user_id = '{}';".format(binz_name, user_id))
    conn.commit()
    st.success(f":red['{binz_name}' successfully deleted!]")

def rename_bin(old_bin_name, new_bin_name, user_id):
    cursor = conn.cursor()
    cursor.execute("UPDATE public.binz_owners SET binz_name = '{}' WHERE binz_name = '{}' AND user_id = '{}';".format(new_bin_name, old_bin_name, user_id))
    conn.commit()
    st.success(f":green[Binz '{old_bin_name}' renamed to '{new_bin_name}']")

image_path = "WD.jpg"

st.title('WasteDrop')

if st.session_state["login_status"] == True:
    cursor = conn.cursor()
    
    users_name = st.session_state["saved_user_name"]
    users_name = users_name.replace("'", "").replace("[","").replace("]","")
    st.write("Welcome ", users_name, "!")
    logout_button = st.sidebar.button("Log Off", on_click=log_out)
    user_id = st.session_state["saved_user_id"]
    user_id = user_id.replace("'", "").replace("[", "").replace("]", "")
    
    # Bin Creation
    st.header("Create new Binz below")
    binz_name_to_create = st.text_input("Enter the name of binz to create")
    create_binz_but = st.button("Create")
    
    cursor.execute("SELECT binz_name FROM public.binz_owners WHERE user_id = '{}';".format(user_id))
    user_binz_list = cursor.fetchall()
    user_binz_arr = [elem2 for elem1 in user_binz_list for elem2 in elem1]

    if create_binz_but:
        if binz_name_to_create in user_binz_arr:
            st.error(":red[This binz already exists!]")
        else:
            cursor.execute("INSERT INTO public.binz_owners(binz_name, user_id) VALUES('{}', '{}')".format(binz_name_to_create, user_id))
            conn.commit()
            st.write(":green[Binz created!]")

    # Bin Renaming
    st.header("Rename Binz below")
    old_bin_name_to_rename = st.text_input("Enter the current name of binz")
    new_bin_name_to_rename = st.text_input("Enter the new name of binz")
    rename_bin_but = st.button("Rename")

    if rename_bin_but:
        if old_bin_name_to_rename not in user_binz_arr:
            st.error(":red[This binz does not exist!]")
        elif new_bin_name_to_rename in user_binz_arr:
            st.error(":red[The new binz name is already taken!]")
        else:
            rename_bin(old_bin_name_to_rename, new_bin_name_to_rename, user_id)
            st.session_state["selected_binz"] = ""

    # Bin Deletion
    st.header("Delete Binz below")
    binz_name_to_delete = st.text_input("Enter the name of binz to delete")
    delete_binz_but = st.button("Delete")

    if delete_binz_but:
        if binz_name_to_delete not in user_binz_arr:
            st.error(":red[This binz does not exist!]")
        else:
            delete_bin(binz_name_to_delete, user_id)
            st.session_state["selected_binz"] = ""

    # Display User's Bins
    st.sidebar.title("Your Binz")
    for binz_result in user_binz_list:
        binz_name = binz_result[0]

        if st.sidebar.button(binz_name, key=binz_name):
            st.session_state["selected_binz"] = binz_name
            switch_to_binz_page()

else:
    st.write("Welcome to WasteDrop!")
    st.write("Please Login or Sign up to continue:")
    if(st.button("Login")):
        switch_page("login")
    if(st.button("Sign Up")):
        switch_page("sign_up")
