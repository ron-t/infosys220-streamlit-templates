import streamlit as st
from data import util

st.title("Add a row to pet_owners")

conn = util.get_connection()
person_value = st.text_input(f"Value for person (text)")
pet_value = st.text_input(f"Value for pet (text)")

list_of_values = [
    person_value,
    pet_value,
]
# We use a form to control when the page is (re)loaded and hence when the row is attempted to be added.
with st.form("form"):
    submitted = st.form_submit_button("Add new row")

if submitted:
    conn._instance.execute(
        f"insert into pet_owners values (?, ?)",
        list_of_values,
    )
    row_count = conn.query(f"select count(1) from pet_owners", ttl=0)
    st.write(f"pet_owners now has {row_count.iat[0,0]} rows.")
