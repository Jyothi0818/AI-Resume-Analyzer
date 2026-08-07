import pandas as pd
import re

def extract_skills(text):

    skills_df = pd.read_csv("skills.csv")

    skills = skills_df["Skill"].tolist()

    text = text.lower()

    found = []

    for skill in skills:

        pattern = r"\b" + re.escape(skill.lower()) + r"\b"

        if re.search(pattern, text):
            found.append(skill)

    return sorted(set(found))