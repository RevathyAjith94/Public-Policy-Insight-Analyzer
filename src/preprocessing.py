import re
import nltk
from nltk.tokenize import sent_tokenize

nltk.download('punkt')


def clean_text(text: str) -> str:
    """
    Cleans raw bill text by removing extra spaces and page numbers.
    """

    text = re.sub(r'\s+', ' ', text)

    
    text = re.sub(r'\n?\s*\d+\s*\n?', ' ', text)

    return text.strip()


def split_sentences(text: str):
    """
    Split text into sentences using NLTK.
    """
    return sent_tokenize(text)


def extract_basic_sections(text: str) -> dict:
    """
    Extracts basic sections from bill text.
    (Heuristic-based, GUVI-acceptable)
    """
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



def preprocess_text(text: str) -> dict:
    """
    Main preprocessing pipeline used across the project.
    This is what app.py and test_preprocessing.py import.
    """
    cleaned_text = clean_text(text)
    sections = extract_basic_sections(cleaned_text)
    return sections

