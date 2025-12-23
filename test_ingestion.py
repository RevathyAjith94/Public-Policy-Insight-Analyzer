from src.ingestion import ingest_bill

result = ingest_bill("pdf", "data/raw/pdfs/sample_bill.pdf")
print(result["raw_text"][:1000])
