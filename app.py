import streamlit as st
from suggestions import generate_suggestions
from resume_parser import extract_text_from_pdf
from utils import preprocess_text
from skill_extractor import extract_skills
from ats_score import calculate_ats_score
from similarity import calculate_similarity
from report import generate_report
# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="📄",
    layout="wide"
)

# -----------------------------
# Title
# -----------------------------
st.title("🤖 AI Resume Analyzer")

st.markdown("""
### NLP-Based ATS Resume Screening System

Analyze your resume using Artificial Intelligence and Natural Language Processing.

### Features

- 📄 Resume Upload
- 🎯 ATS Score
- 📊 Resume Similarity
- 💻 Skill Extraction
- 💡 AI Suggestions
- 📥 Download PDF Report
""")

st.markdown("---")
# -----------------------------
# File Upload
# -----------------------------
uploaded_file = st.file_uploader(
    "Upload Resume (PDF)",
    type=["pdf"]
)

# -----------------------------
# Job Description
# -----------------------------
job_description = st.text_area(
    "Paste Job Description"
)

# -----------------------------
# Analyze Button
# -----------------------------
if st.button("Analyze Resume"):

    if uploaded_file is None:
        st.warning("Please upload a resume.")

    elif job_description.strip() == "":
        st.warning("Please enter the job description.")

    else:

        # Extract Resume Text
        resume_text = extract_text_from_pdf(uploaded_file)

        # Clean Resume
        cleaned_text = preprocess_text(resume_text)

        # Extract Skills
        skills = extract_skills(resume_text)

        # Calculate ATS Score
        score, matched_skills, missing_skills = calculate_ats_score(
            skills,
            job_description
        )
        suggestions = generate_suggestions(missing_skills)
        similarity_score = calculate_similarity( 
            resume_text,
            job_description
        )


        # -----------------------------
        # Success
        # -----------------------------
        st.success("Resume uploaded successfully!")

        # -----------------------------
        # Resume Text
        # -----------------------------
        st.subheader("📄 Extracted Resume Text")

        st.text_area(
            "Resume",
            resume_text,
            height=250
        )

        # -----------------------------
        # Cleaned Text
        # -----------------------------
        st.subheader("🧹 Cleaned Resume Text")

        st.text_area(
            "Processed Resume",
            cleaned_text,
            height=250
        )

        # -----------------------------
        # Skills
        # -----------------------------
        st.subheader("💻 Skills Found")

        if skills:
            st.write(", ".join(skills))
        else:
            st.warning("No skills found.")
        col1, col2 = st.columns(2)
        with col1:
            st.subheader("🎯 ATS Score")
            st.progress(score / 100)
            st.metric("ATS Score", f"{score}%")
        with col2:
            st.subheader("📊 Resume Similarity")
            st.progress(similarity_score / 100)
            st.metric("Similarity", f"{similarity_score}%")

        # -----------------------------
        # ATS Score
        # -----------------------------
        

        # -----------------------------
        # Matched Skills
        # -----------------------------
        st.subheader("✅ Matched Skills")

        if matched_skills:
            for skill in matched_skills:
                st.success(skill)
        else:
            st.warning("No matching skills found.")

        # -----------------------------
        # Missing Skills
        # -----------------------------
        st.subheader("❌ Missing Skills")

        if missing_skills:
            for skill in missing_skills:
                st.error(skill)
        else:
            st.success("No missing skills!")
        st.subheader("💡 AI Suggestions")
        for suggestion in suggestions:
            st.info(suggestion)
        report_file = generate_report(
            score,
            similarity_score,
            skills,
            matched_skills,
            missing_skills
        )
    with open(report_file, "rb") as pdf:
        st.download_button(
            "📥 Download Report",
            pdf,
            file_name="Resume_Report.pdf",
            mime="application/pdf"
        )