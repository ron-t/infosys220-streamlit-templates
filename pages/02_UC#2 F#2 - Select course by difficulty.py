
import streamlit as st
from data import util

st.title("UC#2 F#2 - Select course by difficulty")

table_name = "uc2"

conn = util.get_connection()
value = st.text_input("course difficulty level")

result_df = conn.query(
    f"select * from {table_name} where difficulty = :value",
    params=dict(value=value),
    ttl=0,  # don't cache results so changes in the database are immediately retrieved
)
num_rows_found = len(result_df)
st.write(f'{num_rows_found} row{"" if num_rows_found == 1 else "s"} found for `{value}`')
st.dataframe(
    result_df,
    use_container_width=True,
    hide_index=True,
)
