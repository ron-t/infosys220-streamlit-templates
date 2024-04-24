import streamlit as st
from data import util

st.title("Create data for all UCs")

with st.form("form"):
    submitted = st.form_submit_button("Create data")

if submitted:
    conn = util.get_connection()

    table_name = util.create_seed_data_uc1(conn)

    result_df = conn.query(
        f"select * from {table_name}",
        ttl=0,  # don't cache results so changes in the database are immediately retrieved
    )

    st.write("Table created:")
    st.dataframe(
        result_df,
        use_container_width=True,
        hide_index=True,
    )
    table_name = util.create_seed_data_uc2(conn)

    result_df = conn.query(
        f"select * from {table_name}",
        ttl=0,  # don't cache results so changes in the database are immediately retrieved
    )

    st.write("Table created:")
    st.dataframe(
        result_df,
        use_container_width=True,
        hide_index=True,
    )
