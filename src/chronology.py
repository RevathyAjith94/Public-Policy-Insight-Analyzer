import re

def extract_related_acts(text: str):
    patterns = [
        r"(Finance Act,?\s*\d{4})",
        r"(GST Act,?\s*\d{4})",
        r"(Companies Act,?\s*\d{4})",
        r"(Act\s+No\.?\s*\d+\s+of\s+\d{4})",
        r"(amends?|repeals?)\s+(the\s+)?([A-Za-z\s]+Act,?\s*\d{4})"
    ]

    related_acts = set()

    for pattern in patterns:
        matches = re.findall(pattern, text, flags=re.IGNORECASE)
        for match in matches:
            if isinstance(match, tuple):
                related_acts.add(match[-1])
            else:
                related_acts.add(match)

    return {
        "related_acts": list(related_acts)
    }
