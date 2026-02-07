# safety.py

# ----------------- CRISIS KEYWORDS -----------------
CRISIS_KEYWORDS = [
    "kill myself",
    "end my life",
    "suicide",
    "hurt myself",
    "want to die",
    "better off dead",
    "no reason to live",
    "don't see a reason to keep going",
    "don't want to exist anymore",
    "do not want to exist anymore",
    "don't want to live anymore",
    "do not want to live anymore",
    "i don't want to live",
    "i do not want to live",
    "people would be better off without me"
]

# ----------------- DISTRESS KEYWORDS -----------------
DISTRESS_KEYWORDS = [
    # exhaustion
    "tired of everything",
    "so tired all the time",
    "exhausted with life",
    "emotionally exhausted",
    "burned out",
    "drained",
    "worn out",
    "no energy anymore",
    "can’t keep up anymore",
    "feel like dying",

    # hopelessness
    "hopeless",
    "nothing will change",
    "nothing gets better",
    "nothing looks good anymore",
    "nothing feels right anymore",
    "everything feels pointless",
    "what’s the point anymore",
    "no hope left",
    "lost all hope",

    # anhedonia
    "nothing makes me happy",
    "don’t enjoy anything anymore",
    "nothing feels good",
    "can’t feel joy",
    "lost interest in everything",
    "nothing excites me anymore",

    # numbness
    "feel empty",
    "feel numb",
    "feel nothing",
    "emotionally numb",
    "detached from everything",
    "disconnected from life",

    # worthlessness
    "feel worthless",
    "feel useless",
    "don’t matter",
    "feel like a burden",
    "not good enough",

    # confusion
    "don’t know what I’m feeling",
    "feel lost",
    "overwhelmed",
    "can’t think straight",
    "everything feels too much",

    # apathy
    "don’t care about anything",
    "nothing matters anymore",
    "stopped caring",
    "checked out",
    "just existing",
    "going through the motions",

    # life fatigue
    "tired of life",
    "fed up with life",
    "life feels heavy",
    "life feels pointless",
    "can’t do this anymore",
    "don’t want to deal with anything"
]


# ----------------- SAFETY CHECK -----------------
def safety_check(text: str) -> str:
    """
    Determines safety level of user input.
    Returns: NORMAL, DISTRESS, or CRISIS
    """
    text = text.lower()

    for phrase in CRISIS_KEYWORDS:
        if phrase in text:
            return "CRISIS"

    for phrase in DISTRESS_KEYWORDS:
        if phrase in text:
            return "DISTRESS"

    return "NORMAL"
