import streamlit as st
from streamlit_gsheets import GSheetsConnection

st.title("Read data from a public google sheet")

# We use a form to control when the page is (re)loaded and hence when the sheet is retrieved.
with st.form("form"):
    # Accept url as user input
    url = st.text_input(
        "URL of the public googlesheet. Include the #gid=... part of the URL.",
        value="paste URL here",
    )

    # header is a pandas.read_csv parameter. We pass either None or 0. Behaviour is described here: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html
    header_row = None
    use_first_row_as_header = st.checkbox("Use first row as header?")
    if use_first_row_as_header:
        header_row = 0

    submitted = st.form_submit_button("Retrieve")

if submitted:
    # Create a connection object.
    conn = st.connection(
        "gsheets",
        type=GSheetsConnection,
    )

    df = conn.read(
        spreadsheet=url,
        header=header_row,
    )

    # Show data using st.dataframe.
    st.dataframe(
        df,
        hide_index=True,
    )
