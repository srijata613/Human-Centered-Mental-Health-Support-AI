import torch
from transformers import (
    DistilBertTokenizerFast,
    DistilBertForSequenceClassification
)

from safety import safety_check
from explainability import get_explainability_hints

# ----------------- DEVICE -----------------
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# ----------------- MODEL NAME -----------------
MODEL_NAME = "srijata05/Human-Centered_Mental_Health_Support_AI"
# Example:
# MODEL_NAME = "srijata613/human-centered-emotion-model"

# ----------------- TOKENIZER -----------------
tokenizer = DistilBertTokenizerFast.from_pretrained(MODEL_NAME)

# ----------------- MODEL -----------------
model = DistilBertForSequenceClassification.from_pretrained(MODEL_NAME)

model.to(device)
model.eval()

# ----------------- EMOTIONS -----------------
EMOTION_NAMES = [
    "joy",
    "sadness",
    "anger",
    "fear_anxiety",
    "love_care",
    "surprise",
    "confusion",
    "neutral"
]

# ----------------- ANALYSIS FUNCTION -----------------
def analyze_text(text: str):
    inputs = tokenizer(
        text,
        return_tensors="pt",
        truncation=True,
        padding=True,
        max_length=64
    ).to(device)

    with torch.no_grad():
        outputs = model(**inputs)

    probs = torch.sigmoid(outputs.logits)[0].cpu().numpy()
    emotion_probs = dict(zip(EMOTION_NAMES, probs))

    top_emotion = max(emotion_probs, key=emotion_probs.get)
    safety_level = safety_check(text)
    hints = get_explainability_hints(text, top_emotion)

    return {
        "emotion_probs": emotion_probs,
        "top_emotion": top_emotion,
        "safety_level": safety_level,
        "explainability_hints": hints
    }
