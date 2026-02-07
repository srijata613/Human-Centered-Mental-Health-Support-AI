# explainability.py

EMOTION_HINTS = {
    "sadness": ["empty", "tired", "lonely", "hopeless", "pointless"],
    "fear_anxiety": ["scared", "worried", "anxious", "afraid"],
    "anger": ["angry", "frustrated", "annoyed", "mad"],
    "joy": ["happy", "excited", "relieved", "glad"],
    "love_care": ["love", "care", "grateful", "appreciate"],
    "confusion": ["confused", "lost", "uncertain"],
    "surprise": ["surprised", "shocked", "unexpected"],
    "neutral": []
}

def get_explainability_hints(text: str, top_emotion: str):
    """
    Returns indicative words that may have influenced the prediction.
    """
    text_lower = text.lower()
    hints = []

    for word in EMOTION_HINTS.get(top_emotion, []):
        if word in text_lower:
            hints.append(word)

    return hints
