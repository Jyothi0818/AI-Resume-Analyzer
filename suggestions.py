def generate_suggestions(missing_skills):

    suggestions = []

    if len(missing_skills) == 0:
        suggestions.append("Excellent! Your resume matches the job description well.")

    else:

        for skill in missing_skills:

            suggestions.append(f"Add {skill} to your resume if you have experience with it.")

    return suggestions