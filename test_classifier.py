from src.ingestion import ingest_bill
from src.preprocessing import clean_text
from src.classifier import classify_bill

data = ingest_bill("pdf", "data/raw/pdfs/sample_bill.pdf")
cleaned = clean_text(data["raw_text"])

result = classify_bill(cleaned)

print(result)
