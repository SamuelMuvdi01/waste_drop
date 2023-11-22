import streamlit as st
import psycopg2
from streamlit_extras.switch_page_button import switch_page
from extra_streamlit_components import CookieManager
from pages.login import conn

# Initialize session state
if "saved_user_name" not in st.session_state:
    st.session_state["saved_user_name"] = ""

if "saved_user_id" not in st.session_state:
    st.session_state["saved_user_id"] = ""

if "login_status" not in st.session_state:
    st.session_state['login_status'] = False

# Logout callback
def logout_callback():
    st.session_state['login_status'] = False
    # Reset other session state variables if needed
    switch_page("sign_up")

# Switch to bin page callback
def switch_to_bin_page(binz_name):
    st.session_state["selected_binz"] = binz_name
    switch_page("my_bin")

# Delete bin callback
def delete_bin_callback(binz_name):
    cursor = conn.cursor()
    try:
        cursor.execute("DELETE FROM public.items WHERE binz_id = (SELECT binz_id FROM public.binz_owners WHERE binz_name = %s AND user_id = %s);", (binz_name, st.session_state["saved_user_id"]))
        cursor.execute("DELETE FROM public.binz_owners WHERE binz_name = %s AND user_id = %s;", (binz_name, st.session_state["saved_user_id"]))
        conn.commit()
        st.success(f"Bin '{binz_name}' deleted successfully!")
    except Exception as e:
        st.error(f"Error deleting bin '{binz_name}': {str(e)}")
    finally:
        cursor.close()

st.title('WasteDrop')

if st.session_state["login_status"]:
    cursor = conn.cursor()

    users_name = st.session_state["saved_user_name"]
    st.write("Welcome! ", users_name)

    # Logout button in sidebar
    logout_button = st.sidebar.button("Log Off", on_click=logout_callback)
    
    st.sidebar.title("Binz")
    
    # Create new bin section
    st.header("Create new Binz below")
    binz_name_create = st.text_input("Enter the name of binz to create")
    create_bin_button = st.button("Create Bin")

    cursor.execute("SELECT binz_name FROM public.binz_owners WHERE user_id = '{}';".format(st.session_state["saved_user_id"]))
    user_bin_names = [elem[0] for elem in cursor.fetchall()]

    if create_bin_button:
        if binz_name_create in user_bin_names:
            st.error("This binz already exists!")
        else:
            cursor.execute("INSERT INTO public.binz_owners(binz_name, user_id) VALUES('{}', '{}')".format(binz_name_create, st.session_state["saved_user_id"]))
            conn.commit()
            st.success("Binz created!")

    # Display user's bins in the sidebar
    for bin_name in user_bin_names:
        if st.sidebar.button(bin_name, key=f"switch_bin_{bin_name}"):
            switch_to_bin_page(bin_name)

    # Delete bin section
    st.header("Delete Bin")
    binz_name_delete = st.text_input("Enter the name of binz to delete")
    delete_bin_button = st.button("Delete Bin")

    if delete_bin_button:
        if binz_name_delete in user_bin_names:
            delete_bin_callback(binz_name_delete)
        else:
            st.error(f"Bin '{binz_name_delete}' does not exist!")

else:
    st.write("Please log in to continue")
