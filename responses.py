# responses.py

# ----------------- NORMAL RESPONSES -----------------

POSITIVE_RESPONSES = {
    "joy": (
        "It sounds like you're feeling joy. "
        "That's really nice to hear. "
        "What’s been going well for you?"
    ),
    "love_care": (
        "It sounds like you're feeling warmth or care. "
        "That connection can be really meaningful. "
        "Want to share more about it?"
    ),
    "surprise": (
        "It sounds like something unexpected came up. "
        "How did that make you feel?"
    )
}

NEUTRAL_RESPONSES = {
    "neutral": (
        "Thanks for sharing. "
        "If there's anything on your mind, you can talk about it here."
    ),
    "confusion": (
        "It sounds like things might feel a bit unclear right now. "
        "If you want, we can try to unpack that together."
    )
}

NEGATIVE_RESPONSES = {
    "sadness": (
        "It sounds like you're feeling sadness. "
        "That can be heavy to carry. "
        "If you want, you can tell me more about what's been going on."
    ),
    "anger": (
        "It sounds like you're feeling anger. "
        "That can be really intense. "
        "Do you want to talk about what triggered it?"
    ),
    "fear_anxiety": (
        "It sounds like you're feeling anxious or afraid. "
        "That can be overwhelming. "
        "You're not alone here."
    )
}

DISTRESS_TEMPLATE = (
    "I'm really sorry you're feeling this way. "
    "Carrying these feelings for a while can be exhausting, "
    "and you're not wrong for feeling like this. "
    "You're not alone here."
)

CRISIS_TEMPLATE = (
    "I'm really sorry that you're feeling this much pain. "
    "I can't help with anything that could harm you, "
    "but you deserve care and support.\n\n"
    "If you can, please consider reaching out to someone you trust."
)

CRISIS_RESOURCES = {
    "India": {
        "name": "AASRA",
        "phone": "+91-9820466726",
        "hours": "24/7",
        "website": "https://www.aasra.info"
    }
}

# ----------------- RESPONSE ROUTING -----------------

def crisis_response(region="India") -> str:
    resource = CRISIS_RESOURCES.get(region)
    message = CRISIS_TEMPLATE

    if resource:
        message += (
            f"\n\nYou may also contact {resource['name']} "
            f"({resource['hours']}) at {resource['phone']} "
            f"or visit {resource['website']}."
        )

    return message


def route_response(text: str, top_emotion: str) -> str:
    from safety import safety_check

    safety_level = safety_check(text)

    if safety_level == "CRISIS":
        return crisis_response()

    if safety_level == "DISTRESS":
        return DISTRESS_TEMPLATE

    if top_emotion in POSITIVE_RESPONSES:
        return POSITIVE_RESPONSES[top_emotion]

    if top_emotion in NEUTRAL_RESPONSES:
        return NEUTRAL_RESPONSES[top_emotion]

    return NEGATIVE_RESPONSES.get(
        top_emotion,
        "Thanks for sharing. If you want to say more, I'm here to listen."
    )
