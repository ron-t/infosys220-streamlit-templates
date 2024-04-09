import streamlit as st
from data import util

st.title("Create and Read a table")

TABLE_NAME = "pet_owners"
# We use a form to control when the page is (re)loaded and hence when the data is reset or retrieved.
st.markdown(f"Table name is `{TABLE_NAME}`")
with st.form("form"):
    should_reset = st.checkbox("(Re)create database with table?")
    submitted = st.form_submit_button("Run")

if submitted:
    assert TABLE_NAME in util.VALID_TABLE_NAMES, "Invalid table name"

    conn = util.get_connection()
    if should_reset:
        util.reset_table(conn, TABLE_NAME)

    result_df = conn.query(
        f"select * from {TABLE_NAME}",
        ttl=0,  # don't cache results so changes in the database are immediately retrieved
    )
    st.dataframe(
        result_df,
        use_container_width=True,
        hide_index=True,
    )
