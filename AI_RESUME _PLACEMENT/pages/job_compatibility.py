import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Job Compatibility",
    page_icon="💼",
    layout="wide"
)

st.title("💼 Job Compatibility Analysis")

# ---------------- Check Resume Analysis ----------------

if "skills" not in st.session_state:
    st.warning("⚠ Please complete Resume Analysis first.")
    st.stop()

# ---------------- Resume Skills ----------------

resume_skills = [
    skill.lower().strip()
    for skill in st.session_state["skills"]
]

# ---------------- Load Dataset ----------------

df = pd.read_csv("dataset/job_description.csv")

results = []

# ---------------- Compare Skills ----------------

for _, row in df.iterrows():

    role = row["role"]

    role_skills = [
        skill.replace("_", " ").lower().strip()
        for skill in row["skills"].split()
    ]

    matched_skills = []

    missing_skills = []

    for skill in role_skills:

        if skill in resume_skills:
            matched_skills.append(skill)
        else:
            missing_skills.append(skill)

    match_percentage = round(
        (len(matched_skills) / len(role_skills)) * 100,
        2
    )

    results.append({
        "Role": role,
        "Match": match_percentage,
        "Matched Skills": matched_skills,
        "Missing Skills": missing_skills
    })

# ---------------- Sort ----------------

results = sorted(
    results,
    key=lambda x: x["Match"],
    reverse=True
)

# ---------------- Display ----------------

# ---------------- Display ----------------

st.subheader("🎯 Top Suitable Jobs")

for job in results[:5]:

    st.markdown("---")

    # Job Role (Large)
    st.markdown(
        f"<h2 style='font-size:36px;color:#2E7D32;'>{job['Role']}</h2>",
        unsafe_allow_html=True
    )

    # Progress Bar
    st.progress(int(job["Match"]))

    # Job Match
    st.markdown(
        f"<h4 style='font-size:22px;'>✅ Job Match : {job['Match']}%</h4>",
        unsafe_allow_html=True
    )

    # Matching Skills Heading
    st.markdown(
        "<h5 style='font-size:18px;'>✅ Matching Skills</h5>",
        unsafe_allow_html=True
    )

    if len(job["Matched Skills"]) > 0:

        cols = st.columns(4)

        for i, skill in enumerate(job["Matched Skills"]):
            cols[i % 4].success(skill.title())

    else:
        st.warning("No Matching Skills")

    # Missing Skills Heading
    st.markdown(
        "<h5 style='font-size:18px;'>❌ Missing Skills</h5>",
        unsafe_allow_html=True
    )

    if len(job["Missing Skills"]) > 0:

        cols = st.columns(4)

        for i, skill in enumerate(job["Missing Skills"]):
            cols[i % 4].error(skill.title())

    else:
        st.success("No Missing Skills")

# ---------------- Save Best Match ----------------

st.session_state["best_match"] = results[0]["Role"]
st.session_state["match_percentage"] = results[0]["Match"]
st.session_state["missing_skills"] = results[0]["Missing Skills"]

# ---------------- Recommendation ----------------

st.markdown("---")

st.success(f"🏆 Recommended Job Role : {results[0]['Role']}")

st.info(f"🎯 Match Percentage : {results[0]['Match']} %")

# ---------------- Next ----------------

st.markdown("---")

if st.button("🎯 Proceed to Placement Prediction", use_container_width=True):
    st.switch_page("pages/placement_prediction.py")