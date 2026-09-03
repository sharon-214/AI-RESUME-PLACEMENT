import streamlit as st
import sqlite3
import pandas as pd

st.set_page_config(
    page_title="Admin",
    page_icon="🛠",
    layout="wide"
)

st.title("🛠 Admin Panel")

conn = sqlite3.connect("users.db")

try:

    users = pd.read_sql(
        "SELECT fullname, email, username FROM users",
        conn
    )

    # Remove empty rows
    users = users[
        users["fullname"].notna() &
        (users["fullname"].str.strip() != "")
    ]

    users = users.reset_index(drop=True)

    st.subheader("Registered Users")

    st.dataframe(users, use_container_width=True)

    st.write("Total Users :", len(users))

except Exception as e:

    st.error(f"Error: {e}")
conn.close()