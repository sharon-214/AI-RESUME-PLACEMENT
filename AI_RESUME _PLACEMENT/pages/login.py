import streamlit as st
import hashlib
from database import cursor


st.set_page_config(
    page_title="Login",
    page_icon="🔐",
    layout="centered"
)


# Password hashing
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


# Page Design
st.markdown("""
<h1 style='text-align:center;color:#1565C0;'>
🔐 Login
</h1>

<p style='text-align:center;color:#666;font-size:18px;'>
AI Resume Analysis & Placement Prediction Platform
</p>
""", unsafe_allow_html=True)


st.markdown("<br>", unsafe_allow_html=True)


# Login Form

username = st.text_input("👤 Username")

password = st.text_input(
    "🔒 Password",
    type="password"
)


st.markdown("<br>", unsafe_allow_html=True)


if st.button("Login", use_container_width=True):

    if username == "" or password == "":
        st.warning("Please enter username and password.")

    else:

        try:

            hashed_password = hash_password(password)

            cursor.execute(
                """
                SELECT * FROM users
                WHERE username=? AND password=?
                """,
                (
                    username,
                    hashed_password
                )
            )

            user = cursor.fetchone()


            if user:

                st.session_state.logged_in = True
                st.session_state.username = user[2]
                st.session_state.fullname = user[1]


                st.success("Login Successful ✅")

                st.switch_page(
                    "pages/dashboard.py"
                )


            else:

                st.error(
                    "Invalid Username or Password"
                )


        except Exception as e:

            st.error(
                f"Error: {e}"
            )



st.markdown("<br><br>", unsafe_allow_html=True)


if st.button("👤 Create New Account"):
    st.switch_page(
        "pages/register.py"
    )