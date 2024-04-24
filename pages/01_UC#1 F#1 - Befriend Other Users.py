
import streamlit as st
from data import util

st.title("UC#1 F#1 - Befriend Other Users")

table_name = "uc1"

st.write(f"Table name is `{table_name}`")
select_query = f"select * from {table_name} where invite_status = 'accepted'"

conn = util.get_connection()

result_df = conn.query(
    select_query,
    ttl=0,  # don't cache results
)
st.dataframe(
    result_df,
    use_container_width=True,
    hide_index=True,
)
