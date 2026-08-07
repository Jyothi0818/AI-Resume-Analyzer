from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from datetime import datetime


def generate_report(score, similarity, skills, matched_skills, missing_skills):

    pdf = SimpleDocTemplate("Resume_Report.pdf")

    styles = getSampleStyleSheet()

    title = styles["Title"]
    heading = styles["Heading2"]
    normal = styles["BodyText"]

    elements = []

    # Title
    elements.append(Paragraph("AI Resume Analyzer Report", title))
    elements.append(Paragraph("Candidate Resume Analysis", heading))
    elements.append(Paragraph(datetime.now().strftime("Date: %d-%m-%Y %I:%M %p"), normal))
    elements.append(Spacer(1, 20))

    # Scores
    elements.append(Paragraph(f"<b>ATS Score:</b> {score}%", heading))
    elements.append(Paragraph(f"<b>Resume Similarity:</b> {similarity}%", heading))
    elements.append(Spacer(1, 20))

    # Skills Found
    elements.append(Paragraph("Skills Found", heading))
    for skill in skills:
        elements.append(Paragraph(f"• {skill}", normal))
    elements.append(Spacer(1, 15))

    # Matched Skills
    elements.append(Paragraph("Matched Skills", heading))
    if matched_skills:
        for skill in matched_skills:
            elements.append(Paragraph(f"• {skill}", normal))
    else:
        elements.append(Paragraph("No matched skills.", normal))
    elements.append(Spacer(1, 15))

    # Missing Skills
    elements.append(Paragraph("Missing Skills", heading))
    if missing_skills:
        for skill in missing_skills:
            elements.append(Paragraph(f"• {skill}", normal))
    else:
        elements.append(Paragraph("No Missing Skills - Great Job!", normal))
    elements.append(Spacer(1, 15))

    # AI Suggestions
    elements.append(Paragraph("AI Suggestions", heading))

    if missing_skills:
        for skill in missing_skills:
            elements.append(
                Paragraph(f"✔ Consider adding {skill} if you have experience.", normal)
            )
    else:
        elements.append(
            Paragraph(" Excellent! Your resume matches the job description well.", normal)
        )

    pdf.build(elements)

    return "Resume_Report.pdf"