import streamlit as st
import hashlib
from database import conn, cursor


st.set_page_config(
    page_title="Register",
    page_icon="👤",
    layout="centered"
)


# Password encryption
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


# Title
st.markdown("""
<h1 style='text-align:center;color:#1565C0;'>
Create Account
</h1>

<p style='text-align:center;color:#666;'>
AI Resume Analysis & Placement Prediction Platform
</p>
""", unsafe_allow_html=True)


st.write("")


# Input fields

fullname = st.text_input("👤 Full Name")

email = st.text_input("📧 Email")

username = st.text_input("🔑 Username")

password = st.text_input(
    "🔒 Password",
    type="password"
)

confirm_password = st.text_input(
    "🔒 Confirm Password",
    type="password"
)


st.write("")


# Register button

if st.button("Register", use_container_width=True):

    # Validation

    if fullname.strip() == "":
        st.warning("Please enter Full Name")

    elif email.strip() == "":
        st.warning("Please enter Email")

    elif username.strip() == "":
        st.warning("Please enter Username")

    elif password.strip() == "":
        st.warning("Please enter Password")

    elif confirm_password.strip() == "":
        st.warning("Please confirm Password")

    elif password != confirm_password:
        st.error("Passwords do not match")

    else:

        try:

            # Check existing user

            cursor.execute(
                """
                SELECT username, email 
                FROM users
                WHERE username=? OR email=?
                """,
                (
                    username,
                    email
                )
            )

            user = cursor.fetchone()


            if user:

                st.error(
                    "Username or Email already exists"
                )


            else:

                encrypted_password = hash_password(password)


                cursor.execute(
                    """
                    INSERT INTO users
                    (
                        fullname,
                        email,
                        username,
                        password
                    )
                    VALUES
                    (?,?,?,?)
                    """,
                    (
                        fullname,
                        email,
                        username,
                        encrypted_password
                    )
                )


                conn.commit()


                st.success(
                    "Registration Successful ✅"
                )

                st.info(
                    "Now login with your username and password."
                )


        except Exception as e:

            st.error(
                f"Database Error: {e}"
            )


st.write("")


# Go to login

if st.button("🔐 Go To Login"):
    st.switch_page(
        "pages/login.py"
    )