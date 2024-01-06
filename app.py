import streamlit as st

import langchain_helper as lh

st.title("This is sample restaurant name and menu items generated using OPEN AI")

cuisine = st.sidebar.radio(
    "Pick a cuisine", ("Indian", "Mexican", "Italian", "Chinese", "French", "Afghani")
)


if cuisine:
    response = lh.generate_restaurant_name_items(cuisine)
    st.header(response["restaurant_name"].strip().replace('"', ""))
    st.write("**Menu items**")
    menu_items = response["menu_items"].strip().split(",")
    for items in menu_items:
        st.write(items)
