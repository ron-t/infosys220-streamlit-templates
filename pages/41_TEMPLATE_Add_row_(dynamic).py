import streamlit as st
from data import util

st.title("Add a row (dynamic example)")


table_name = st.selectbox("Table name", util.VALID_TABLE_NAMES)
assert table_name in util.VALID_TABLE_NAMES, "Invalid table name"

conn = util.get_connection()
columns_df = conn.query(
    f"select name, type from pragma_table_info('{table_name}')",
    ttl=0,  # don't cache results
)

col_values = {n: None for n in columns_df["name"].values}
for col in columns_df.itertuples():
    col_values[col.name] = st.text_input(f"Value for {col.name} (type {col.type})")

# We use a form to control when the page is (re)loaded and hence when the row is attempted to be added.
with st.form("form"):
    submitted = st.form_submit_button("Add new row")

if submitted:
    conn._instance.execute(
        f'insert into {table_name} values ({", ".join([f":{n}" for n in col_values])})',
        col_values,
    )
    row_count = conn.query(
        f"select count(1) from {table_name}",
        ttl=0,  # don't cache results so changes in the database are immediately retrieved
    )
    st.write(f"{table_name} now has {row_count.iat[0,0]} rows.")
