import spacy
import subprocess
import sys

try:
    nlp = spacy.load("en_core_web_sm")
except OSError:
    subprocess.run(
        [sys.executable, "-m", "spacy", "download", "en_core_web_sm"],
        check=True
    )
    nlp = spacy.load("en_core_web_sm")
def preprocess_text(text):
    """
    Cleans and preprocesses the extracted resume text.
    """

    doc = nlp(text.lower())

    cleaned_words = []

    for token in doc:

        if (
            not token.is_stop
            and not token.is_punct
            and not token.is_space
        ):
            cleaned_words.append(token.lemma_)

    return " ".join(cleaned_words)


