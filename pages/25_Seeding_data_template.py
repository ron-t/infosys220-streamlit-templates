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

# exercise:
# 1. run as-is and inspect db
# 2. change table name and re-run and inspect db; choose an object to create data about
# 3. change REPLACEMEcol* (and add more if needed) to attributes about the object
# 4. re-run and inspect db
# 5. change REPLACEMErow* values (to match updated cols) to rows of the object
# 6. re-run and inspect db
# 7. change the function name to reflect your code: `create_seed_data_REPLACEME`
#       - where it's defined, and where it's called (used)
