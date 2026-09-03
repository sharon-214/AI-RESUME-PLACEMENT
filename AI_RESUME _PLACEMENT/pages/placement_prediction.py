import streamlit as st
from placement_predictor import predict_placement

st.set_page_config(
    page_title="Placement Prediction",
    page_icon="🎯",
    layout="wide"
)

st.title("🎯 AI Placement Prediction")

# Check Resume Analysis completed
if "technical_skills" not in st.session_state:
    st.warning("⚠ Please complete Resume Analysis first.")
    st.stop()

st.subheader("Enter Academic Details")

cgpa = st.number_input(
    "CGPA",
    min_value=0.0,
    max_value=10.0,
    value=7.5,
    step=0.1
)

communication = st.slider(
    "Communication Skills",
    1,
    10,
    6
)

backlogs = st.number_input(
    "Current Backlogs",
    min_value=0,
    max_value=20,
    value=0
)

# Automatically from Resume Analysis
projects = st.session_state.get("projects", 0)
internships = st.session_state.get("internships", 0)
technical_skills = st.session_state.get("technical_skills", 0)
certifications = st.session_state.get("certifications", 0)
workshops = st.session_state.get("workshops", 0)
coding_score = st.session_state.get("coding_score", 0)

st.markdown("---")
st.subheader("Resume Details")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Projects", projects)
    st.metric("Internships", internships)

with col2:
    st.metric("Technical Skills", technical_skills)
    st.metric("Certifications", certifications)

with col3:
    st.metric("Workshops", workshops)
    st.metric("Coding Score", coding_score)

st.markdown("---")

if st.button("Predict Placement Probability"):

    prediction = predict_placement(
        cgpa,
        communication,
        backlogs,
        internships,
        projects,
        technical_skills,
        certifications,
        workshops,
        coding_score
    )

    st.subheader("Prediction Result")

    st.progress(int(prediction))

    st.success(f"Placement Probability : {prediction:.2f}%")

    if prediction >= 80:
        st.balloons()
        st.success("Excellent placement chances 🎉")

    elif prediction >= 60:
        st.info("Good placement chances 👍")

    elif prediction >= 40:
        st.warning("Average placement chances")

    else:
        st.error("Low placement chances. Improve your profile.")

st.markdown("---")

if st.button("⬅ Back to Dashboard"):
    st.switch_page("pages/dashboard.py")