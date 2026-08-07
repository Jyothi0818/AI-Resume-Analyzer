from skill_extractor import extract_skills

def calculate_ats_score(resume_skills, job_description):

    # Extract skills from the job description
    required_skills = extract_skills(job_description)

    matched_skills = []
    missing_skills = []

    for skill in required_skills:
        if skill in resume_skills:
            matched_skills.append(skill)
        else:
            missing_skills.append(skill)

    if len(required_skills) == 0:
        score = 0
    else:
        score = round((len(matched_skills) / len(required_skills)) * 100)

    return score, matched_skills, missing_skills