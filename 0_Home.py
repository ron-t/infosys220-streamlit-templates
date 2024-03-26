import streamlit as st

st.set_page_config(
    page_title="Template title",  # Change this for your group project
    # page_icon="👋", # Uncoment and modify this if you wish
)

st.header("Home page")
st.write("This page describes ...")  # Change this for your group project


# Change the data function names and descriptions for your project project

st.subheader("Data Function 1")
st.write("The template for Data Function 1 is to read from a public Google Sheet.")
st.info("You will modify this template as the Week 9 lab exercise.")
st.write("\n")


def group_project_modify_info_footer():
    st.info("You can modify/reuse this to suit your group project task.")
    st.write("\n")


st.subheader("Data Function 2")
st.write("The template for Data Function 2 is to read a table from a local sqlite database file.")
group_project_modify_info_footer()

st.subheader("Data Function 2a")
st.write("The code for Data Function 2a demonstates how to read a dynamically selected table.")
st.write("\n")

st.subheader("Data Function 3")
st.write("The template for Data Function 3 is to search for a row by id from a table in a local sqlite database file.")
group_project_modify_info_footer()

st.subheader("Data Function 3a")
st.write(
    "The code for Data Function 3a demonstrates how to search for a row by dynamically selecting a table and "
    "column to enter a value for."
)
st.write("\n")

st.subheader("Data Function 4")
st.write("The template for Data Function 4 is to add a new row to a table in a local sqlite database file.")
group_project_modify_info_footer()

st.subheader("Data Function 4a")
st.write("The code for Data Function 4a demonstrates how to add a new row to a dynamically selected table.")
