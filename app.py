import streamlit as st
import torch

from analysis import analyze_text
from responses import route_response, crisis_response

# ----------------- PAGE CONFIG -----------------
st.set_page_config(
    page_title="Human-Centered Mental Health AI",
    layout="centered"
)

# ----------------- HEADER -----------------
st.title("Human-Centered Mental Health Support AI")
st.caption("Emotion-aware • Safety-first • Explainable")

st.warning(
    "⚠️ This system is not a medical professional. "
    "It does not provide diagnosis or treatment. "
    "If you are in immediate danger, seek local emergency help."
)

# ----------------- TEXT INPUT -----------------
text = st.text_area(
    "Enter text to analyze",
    placeholder="Type how you're feeling here...",
    height=150
)

analyze_btn = st.button("Analyze")

# ----------------- ANALYSIS -----------------
if analyze_btn and text.strip():

    result = analyze_text(text)

    # ---- SAFETY STATUS ----
    st.subheader("🛡 Safety Status")

    if result["safety_level"] == "CRISIS":
        st.error("CRISIS")
    elif result["safety_level"] == "DISTRESS":
        st.warning("DISTRESS")
    else:
        st.success("NORMAL")

    # ---- EMOTION ANALYSIS ----
    st.subheader("🧠 Emotion Analysis")
    st.write(f"**Top Emotion:** {result['top_emotion']}")

    st.bar_chart(result["emotion_probs"])

    # ---- EXPLAINABILITY ----
    st.subheader("🔍 Explainability")

    if result["explainability_hints"]:
        st.write("Indicative words detected:")
        for w in result["explainability_hints"]:
            st.markdown(f"- **{w}**")
    else:
        st.write("No strong lexical cues detected.")

    # ---- SYSTEM RESPONSE ----
    st.subheader("💬 System Response")

    if result["safety_level"] == "CRISIS":
        st.write(crisis_response("India"))
    else:
        st.write(route_response(text, result["top_emotion"]))
