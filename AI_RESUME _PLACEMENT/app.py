import streamlit as st

st.set_page_config(
    page_title="AI Resume Analysis",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Hide Streamlit default menu
st.markdown("""
<style>
#MainMenu {visibility:hidden;}
header {visibility:hidden;}
footer {visibility:hidden;}

.block-container{
    padding-top:2rem;
    max-width:1200px;
}

html, body, .stApp{
    background:white;
    font-family:'Segoe UI',sans-serif;
}

.title{
    text-align:center;
    font-size:64px;
    font-weight:900;
    color:#1565C0;
    margin-bottom:0;
}

.subtitle{
    text-align:center;
    font-size:38px;
    font-weight:800;
    color:#2E7D32;
    margin-top:-10px;
}

.tagline{
    text-align:center;
    color:#666;
    font-size:20px;
    margin-top:15px;
    margin-bottom:40px;
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="title">
AI-Powered Resume Analysis
</div>

<div class="subtitle">
& Placement Prediction Platform
</div>

<div class="tagline">
Analyse • Match • Predict • Succeed
</div>
""", unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown("""
    <div style="
        text-align:center;
        padding:20px;
        border-radius:15px;
        border:1px solid #E3F2FD;
        box-shadow:0px 4px 12px rgba(0,0,0,0.08);
        background:white;
        height:220px;">
        <div style="font-size:55px;">📄</div>
        <h3 style="color:#1565C0;">ANALYZE</h3>
        <p style="color:#555;font-size:18px;">
        Your Resume
        </p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div style="
        text-align:center;
        padding:20px;
        border-radius:15px;
        border:1px solid #E8F5E9;
        box-shadow:0px 4px 12px rgba(0,0,0,0.08);
        background:white;
        height:220px;">
        <div style="font-size:55px;">🎯</div>
        <h3 style="color:#2E7D32;">MATCH</h3>
        <p style="color:#555;font-size:18px;">
        Jobs & Internships
        </p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div style="
        text-align:center;
        padding:20px;
        border-radius:15px;
        border:1px solid #E3F2FD;
        box-shadow:0px 4px 12px rgba(0,0,0,0.08);
        background:white;
        height:220px;">
        <div style="font-size:55px;">📈</div>
        <h3 style="color:#1565C0;">PREDICT</h3>
        <p style="color:#555;font-size:18px;">
        Placement Chances
        </p>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown("""
    <div style="
        text-align:center;
        padding:20px;
        border-radius:15px;
        border:1px solid #E8F5E9;
        box-shadow:0px 4px 12px rgba(0,0,0,0.08);
        background:white;
        height:220px;">
        <div style="font-size:55px;">🏆</div>
        <h3 style="color:#2E7D32;">SUCCEED</h3>
        <p style="color:#555;font-size:18px;">
        In Your Career
        </p>
    </div>
    """, unsafe_allow_html=True)
    st.markdown("<br><br>", unsafe_allow_html=True)

st.markdown("""
<h3 style='text-align:center;
color:#444;
font-size:24px;
font-weight:600;'>

SMART ANALYSIS • BETTER MATCHES • BRIGHTER FUTURE

</h3>
""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

col1, col2, col3, col4, col5 = st.columns([2,1,0.3,1,2])

with col2:
    if st.button("🔐 Login", width="stretch"):
        st.switch_page("pages/login.py")

with col4:
    if st.button("👤 Register", use_container_width="stretch"):
        st.switch_page("pages/register.py")

st.markdown("<br><br>", unsafe_allow_html=True)

st.markdown("""
<hr style="margin-top:40px;margin-bottom:15px;">

<p style='text-align:center;
color:#777;
font-size:16px;'>

© 2026 AI-Powered Resume Analysis & Placement Prediction Platform

</p>
""", unsafe_allow_html=True)