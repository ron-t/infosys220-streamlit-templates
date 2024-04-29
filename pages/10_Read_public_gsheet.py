import streamlit as st
from streamlit_gsheets import GSheetsConnection

st.title("Read data from a public google sheet")

# Accept url as user input
url = st.text_input(
    "URL of the public googlesheet. Include the #gid=... part of the URL.",
    value="paste URL here",
)

conn = st.connection(
    "gsheets",
    type=GSheetsConnection,
)

df = conn.read(spreadsheet=url)  # edit this to store the result in a dataframe

st.dataframe(
    df,  # edit this to show the dataframe from above
    hide_index=True,
)
