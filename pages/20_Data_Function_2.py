import streamlit as st
from data import util

st.title("Read a table")

table_name = "pet_owners"
# We use a form to control when the page is (re)loaded and hence when the data is reset or retrieved.
st.markdown(f"Table name is `{table_name}`")
with st.form("form"):
    should_reset = st.checkbox("(Re)create database with table?")
    submitted = st.form_submit_button("Run")

if submitted:
    assert table_name in util.VALID_TABLE_NAMES, "Invalid table name"

    conn = util.get_connection()
    if should_reset:
        util.reset_table(conn, table_name)

    result_df = conn.query(
        f"select * from {table_name}",
        ttl=0,  # don't cache results
    )
    st.dataframe(
        result_df,
        use_container_width=True,
        hide_index=True,
    )
