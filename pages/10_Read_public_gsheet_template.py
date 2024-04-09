import streamlit as st
from streamlit_gsheets import GSheetsConnection

st.title("Read data from a public google sheet")

url = "..."  # edit this to a suitable url

conn = st.connection(
    "gsheets",
    type=GSheetsConnection,
)

conn.read(spreadsheet=url)  # edit this to store the result in a dataframe

st.dataframe(
    ...,  # edit this to show the dataframe from above
    hide_index=True,
)

# exercise notes:
# 1. hardcode url
# 2. accept from text input
# 3. [extra] use form
