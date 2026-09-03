import streamlit as st
import pdfplumber

st.set_page_config(
    page_title="Resume Analysis",
    page_icon="📄",
    layout="wide"
)

st.title("📄 Resume Analysis")

st.write("Upload your Resume (PDF)")

# ---------------- Upload Resume ----------------

uploaded_file = st.file_uploader(
    "Choose Resume (PDF)",
    type=["pdf"]
)

if uploaded_file is None:
    st.info("Please upload your resume to continue.")
    st.stop()

st.session_state["uploaded_resume"] = uploaded_file

# ---------------- Extract Resume Text ----------------

def extract_text_from_pdf(file):
    text = ""

    with pdfplumber.open(file) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()

            if page_text:
                text += page_text + " "

    return text.lower()

resume_text = extract_text_from_pdf(uploaded_file)

# ---------------- Load Skill Master ----------------

with open("dataset/skill_master.txt", "r", encoding="utf-8") as f:
    skills_master = [
        skill.strip().lower()
        for skill in f.readlines()
    ]

# ---------------- Extract Skills ----------------

skills = []

for skill in skills_master:

    if skill in resume_text:
        skills.append(skill)

technical_skills = len(skills)

# ---------------- Extract Projects ----------------

project_keywords = [
    "project",
    "developed",
    "implemented",
    "designed"
]

projects = sum(
    resume_text.count(word)
    for word in project_keywords
)

# ---------------- Extract Internships ----------------

internship_keywords = [
    "internship",
    "intern",
    "trainee"
]

internships = sum(
    resume_text.count(word)
    for word in internship_keywords
)
# ---------------- Extract Certifications ----------------

certification_keywords = [
    "certification",
    "certificate",
    "certified"
]

certifications = sum(
    resume_text.count(word)
    for word in certification_keywords
)

# ---------------- Extract Workshops ----------------

workshop_keywords = [
    "workshop",
    "training",
    "bootcamp"
]

workshops = sum(
    resume_text.count(word)
    for word in workshop_keywords
)

# ---------------- Coding Score ----------------

coding_keywords = [
    "python",
    "java",
    "c",
    "c++",
    "sql",
    "html",
    "css",
    "javascript",
    "react",
    "nodejs",
    "django",
    "machine learning",
    "deep learning",
    "tensorflow",
    "pytorch",
    "git",
    "github"
]

coding_score = 0

for skill in coding_keywords:
    if skill in resume_text:
        coding_score += 1

# ---------------- Save in Session ----------------

st.session_state["skills"] = skills
st.session_state["technical_skills"] = technical_skills
st.session_state["projects"] = projects
st.session_state["internships"] = internships
st.session_state["certifications"] = certifications
st.session_state["workshops"] = workshops
st.session_state["coding_score"] = coding_score

# ---------------- Display Results ----------------

st.success("✅ Resume Analysis Completed Successfully")

st.subheader("📌 Extracted Skills")

if skills:
    cols = st.columns(3)
    for i, skill in enumerate(skills):
        cols[i % 3].success(skill.title())
else:
    st.error("No Skills Found")

st.markdown("---")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Technical Skills", technical_skills)

with col2:
    st.metric("Projects", projects)

with col3:
    st.metric("Internships", internships)

col4, col5, col6 = st.columns(3)

with col4:
    st.metric("Certifications", certifications)

with col5:
    st.metric("Workshops", workshops)

with col6:
    st.metric("Coding Score", coding_score)

st.markdown("---")

if st.button("➡ Proceed to Job Compatibility", use_container_width=True):
    st.switch_page("pages/job_compatibility.py")