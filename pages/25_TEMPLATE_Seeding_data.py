import streamlit as st
from data import util

st.title("Data seeding example")

with st.form("form"):
    submitted = st.form_submit_button("Seed data")

if submitted:
    conn = util.get_connection()

    table_name = util.create_seed_data_REPLACEME(conn)

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

    ###################################################################################
    # To create multiple tables in a single page/form, uncomment the lines below and
    # change the REPLACEME part.
    ###################################################################################

    # table_name = util.create_seed_data_REPLACEME2(conn)
    # result_df = conn.query(
    #     f"select * from {table_name}",
    #     ttl=0,  # don't cache results so changes in the database are immediately retrieved
    # )
    # st.write("Table created:")
    # st.dataframe(
    #     result_df,
    #     use_container_width=True,
    #     hide_index=True,
    # )

    # table_name = util.create_seed_data_REPLACEME3(conn)
    # result_df = conn.query(
    #     f"select * from {table_name}",
    #     ttl=0,  # don't cache results so changes in the database are immediately retrieved
    # )
    # st.write("Table created:")
    # st.dataframe(
    #     result_df,
    #     use_container_width=True,
    #     hide_index=True,
    # )

    # table_name = util.create_seed_data_REPLACEME4(conn)
    # result_df = conn.query(
    #     f"select * from {table_name}",
    #     ttl=0,  # don't cache results so changes in the database are immediately retrieved
    # )
    # st.write("Table created:")
    # st.dataframe(
    #     result_df,
    #     use_container_width=True,
    #     hide_index=True,
    # )

    # table_name = util.create_seed_data_REPLACEME5(conn)
    # result_df = conn.query(
    #     f"select * from {table_name}",
    #     ttl=0,  # don't cache results so changes in the database are immediately retrieved
    # )
    # st.write("Table created:")
    # st.dataframe(
    #     result_df,
    #     use_container_width=True,
    #     hide_index=True,
    # )
