from src.ingestion import ingest_bill
from src.preprocessing import clean_text, extract_basic_sections

data = ingest_bill("pdf", "data/raw/pdfs/sample_bill.pdf")
cleaned = clean_text(data["raw_text"])
sections = extract_basic_sections(cleaned)

print(sections.keys())
print(sections["objective"][:500])
