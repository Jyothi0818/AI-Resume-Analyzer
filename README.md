# 🤖 AI Resume Analyzer

An AI-powered Resume Analyzer built using Python, Streamlit, Natural Language Processing (NLP), and Machine Learning techniques. The application compares a candidate's resume with a job description and provides an ATS score, resume similarity score, skill analysis, AI suggestions, and a downloadable PDF report.

---

## 🚀 Features

- 📄 Upload Resume (PDF)
- 📝 Extract Resume Text
- 🧹 NLP Text Preprocessing using spaCy
- 💻 Skill Extraction
- 🎯 ATS Score Calculation
- 📊 Resume Similarity using TF-IDF & Cosine Similarity
- ✅ Matched Skills
- ❌ Missing Skills
- 💡 AI Suggestions
- 📥 Download Analysis Report (PDF)

---

## 🛠️ Technologies Used

- Python
- Streamlit
- spaCy
- scikit-learn
- pandas
- PyPDF2
- ReportLab

---

## 📂 Project Structure

```
AI_Resume_Analyzer/
│
├── app.py
├── resume_parser.py
├── utils.py
├── skill_extractor.py
├── ats_score.py
├── similarity.py
├── suggestions.py
├── report.py
├── skills.csv
├── requirements.txt
├── README.md
└── uploads/
```

---

## ⚙️ Installation

1. Clone the repository

```bash
git clone <repository-url>
```

2. Move into the project folder

```bash
cd AI_Resume_Analyzer
```

3. Install dependencies

```bash
pip install -r requirements.txt
```

4. Run the application

```bash
streamlit run app.py
```

---

## 📖 How It Works

1. Upload a resume in PDF format.
2. Paste the job description.
3. Click **Analyze Resume**.
4. The system extracts text from the resume.
5. Skills are identified using NLP.
6. ATS Score is calculated.
7. Resume Similarity is calculated using TF-IDF and Cosine Similarity.
8. Matched and Missing Skills are displayed.
9. AI Suggestions are generated.
10. Download the PDF report.

---

## 📸 Output

- ATS Score
- Resume Similarity
- Skills Found
- Matched Skills
- Missing Skills
- AI Suggestions
- PDF Report

---

## 👩‍💻 Developed By

**Jyothirmayee Gayala**

B.Tech – CSE (AI & ML)
