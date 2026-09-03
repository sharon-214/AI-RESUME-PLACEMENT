import streamlit as st

st.set_page_config(
    page_title="Profile",
    page_icon="👤",
    layout="wide"
)

st.title("👤 Student Profile")

username = st.session_state.get("username", "Student")
email = st.session_state.get("email", "Not Available")

st.write("### Personal Information")

st.text_input("Full Name", username, disabled=True)
st.text_input("Email", email, disabled=True)

st.markdown("---")

st.write("### Resume Summary")

st.write("Technical Skills :", st.session_state.get("technical_skills", 0))
st.write("Projects :", st.session_state.get("projects", 0))
st.write("Internships :", st.session_state.get("internships", 0))
st.write("Certifications :", st.session_state.get("certifications", 0))
st.write("Workshops :", st.session_state.get("workshops", 0))
st.write("Coding Score :", st.session_state.get("coding_score", 0))

st.markdown("---")

st.write("### Job Recommendation")

st.success(st.session_state.get("best_match", "Not Available"))

st.write("Match Percentage :",
         st.session_state.get("match_percentage", 0),
         "%")