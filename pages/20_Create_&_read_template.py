import streamlit as st
from data import util

st.title("Create and Read a table")

table_name = "..."  # edit this: choose a table from the VALID_TABLE_NAMES in data/util.py

# We use a form to control when the page is (re)loaded and hence when the data is reset or retrieved.
st.write(f"Table name is `{table_name}`")
select_query = f"select * from {table_name}"
st.write(f"Query is: `{select_query}`")

with st.form("form"):
    should_reset = st.checkbox("(Re)create database with table?")
    submitted = st.form_submit_button("Run")

if submitted:
    conn = util.get_connection()
    if should_reset:
        util.reset_table(conn, table_name)

    result_df = conn.query(
        select_query,
        ttl=0,  # don't cache results
    )
    st.dataframe(
        result_df,
        use_container_width=True,
        hide_index=True,
    )

# exercise notes:
# 1. hard code table name
# 2. select table names from selectbox
# 3. [extra] if you know sql, change the query to select something else from the table (e.g. add a where clause)

# functions 3 onwards are demo and useful to copy/paste/modify for group assignment
# crawl, walk, run, fly framework.