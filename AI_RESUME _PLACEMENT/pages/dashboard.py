import streamlit as st

st.set_page_config(
    page_title="Dashboard",
    page_icon="🎓",
    layout="wide"
)

# ---------------- Login Check ----------------

if "username" not in st.session_state:
    st.warning("Please login first.")
    st.switch_page("app.py")

username = st.session_state["username"]

# ---------------- Header ----------------

st.markdown(f"""
<div style="background-color:#0E76A8;padding:20px;border-radius:12px;">
    <h2 style="color:white;text-align:center;">
        🎓 AI Resume Analysis & Placement Prediction Platform
    </h2>
    <h3 style="color:white;text-align:center;">
        Welcome, {username} 👋
    </h3>
</div>
""", unsafe_allow_html=True)

st.markdown("---")

# ---------------- Features ----------------

col1, col2, col3 = st.columns(3)

with col1:
    st.info("📄 Resume Analysis")
    st.write("""
✔ Upload Resume

✔ Extract Skills

✔ Projects

✔ Internships

✔ Certifications

✔ Workshops

✔ Coding Score
""")

    if st.button("📄 Resume Analysis", use_container_width=True):
        st.switch_page("pages/resume_analyzer.py")

with col2:
    st.info("💼 Job Compatibility")
    st.write("""
✔ Best Job Role

✔ Matching Skills

✔ Missing Skills

✔ Job Match %
""")

    if st.button("💼 Job Compatibility", use_container_width=True):
        st.switch_page("pages/job_compatibility.py")

with col3:
    st.info("🎯 Placement Prediction")
    st.write("""
✔ Enter CGPA

✔ Communication

✔ Backlogs

✔ Placement Probability
""")

    if st.button("🎯 Placement Prediction", use_container_width=True):
        st.switch_page("pages/placement_prediction.py")

st.markdown("---")

# ---------------- Bottom Buttons ----------------

col4, col5, col6 = st.columns(3)

with col4:
    if st.button("👤 Profile", use_container_width=True):
        st.switch_page("pages/profile.py")

with col5:
    if st.button("🛠 Admin", use_container_width=True):
        st.switch_page("pages/admin.py")

with col6:
    if st.button("🚪 Logout", use_container_width=True):
        st.session_state.clear()
        st.switch_page("app.py")

st.markdown("---")
st.caption("© 2026 AI Resume Analysis & Placement Prediction Platform")