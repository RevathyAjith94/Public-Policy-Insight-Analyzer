from src.chronology import extract_related_acts

sample_text = """
This Act amends the Finance Act, 2019 and repeals certain provisions
of the Taxation Laws Act, 2020.
"""

print(extract_related_acts(sample_text))
