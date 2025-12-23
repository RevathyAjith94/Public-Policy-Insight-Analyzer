import re
import nltk
from nltk.tokenize import sent_tokenize

nltk.download('punkt')

def clean_text(text):
    # Remove extra spaces
    text = re.sub(r'\s+', ' ', text)

    # Remove page numbers
    text = re.sub(r'\n?\s*\d+\s*\n?', ' ', text)

    return text.strip()


def split_sentences(text):
    return sent_tokenize(text)


def extract_basic_sections(text):
    sections = {
        "objective": "",
        "key_provisions": "",
        "definitions": "",
        "miscellaneous": ""
    }

    lower_text = text.lower()

    if "objective" in lower_text:
        sections["objective"] = text[:1000]

    sections["key_provisions"] = text[1000:3000]
    sections["definitions"] = text[3000:4000]
    sections["miscellaneous"] = text[4000:5000]

    return sections
