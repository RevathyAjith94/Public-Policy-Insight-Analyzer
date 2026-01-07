def analyze_impact(text):
    text = text.lower()

    sector_keywords = {
        "Finance": ["tax", "gst", "duty", "revenue"],
        "Agriculture": ["farmer", "crop", "land"],
        "Healthcare": ["hospital", "health", "medicine"],
        "Education": ["school", "education", "student"],
        "Technology": ["internet", "data", "digital"]
    }

    affected_sectors = []

    for sector, keywords in sector_keywords.items():
        for word in keywords:
            if word in text:
                affected_sectors.append(sector)
                break

    citizen_impact = "Minimal impact"
    if "tax" in text or "fee" in text:
        citizen_impact = "Possible increase in cost of living"

    business_impact = "Compliance changes possible"
    government_impact = "Policy implementation required"

    return {
        "affected_sectors": affected_sectors,
        "citizen_impact": citizen_impact,
        "business_impact": business_impact,
        "government_impact": government_impact
    }