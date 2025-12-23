import pdfplumber
import requests
from bs4 import BeautifulSoup

def extract_text_from_pdf(pdf_path):
    text = ""
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text += page.extract_text() + "\n"
    return text.strip()


def extract_text_from_url(url):
    response = requests.get(url, timeout=10)
    soup = BeautifulSoup(response.content, "html.parser")

    # Remove scripts & styles
    for tag in soup(["script", "style"]):
        tag.decompose()

    text = soup.get_text(separator=" ")
    return " ".join(text.split())


def ingest_bill(source_type, source):
    """
    source_type: 'pdf' or 'url'
    source: file path or url
    """
    if source_type == "pdf":
        raw_text = extract_text_from_pdf(source)
    elif source_type == "url":
        raw_text = extract_text_from_url(source)
    else:
        raise ValueError("Unsupported source type")

    return {
        "source_type": source_type,
        "raw_text": raw_text
    }
