from src.summarizer import generate_summary

sample_text = """
This bill proposes amendments related to taxation and digital payments.
"""

result = generate_summary(sample_text)
print(result["citizen_summary"])

