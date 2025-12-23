def classify_bill(text):
    text = text.lower()

    categories = {
        "Finance": ["tax", "gst", "revenue", "duty", "income"],
        "Agriculture": ["farmer", "crop", "agriculture", "land"],
        "Healthcare": ["health", "hospital", "medical"],
        "Education": ["education", "school", "university"],
        "Technology": ["digital", "data", "technology", "cyber"],
        "Environment": ["environment", "climate", "pollution"]
    }

    scores = {}

    for category, keywords in categories.items():
        scores[category] = sum(text.count(word) for word in keywords)

    predicted = max(scores, key=scores.get)

    return {
        "predicted_category": predicted,
        "scores": scores
    }
