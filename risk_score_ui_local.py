import streamlit as st

st.set_page_config(page_title="Risk Analyzer", layout="centered")
st.title("Risk Score Analyzer")

st.markdown("""
This tool analyzes text and assigns a risk level using local keyword-based logic.
No external models or downloads required.
""")

# Define keyword lists
high_risk_keywords = ["explosive", "fatal", "critical", "hostile", "armed", "threat"]
medium_risk_keywords = ["urgent", "pressure", "delay", "unauthorized", "suspicious"]
low_risk_keywords = ["routine", "resolved", "minor", "safe", "normal"]

def score_text(text):
    text_lower = text.lower()
    score = {"High Risk": 0, "Medium Risk": 0, "Low Risk": 0}

    for word in high_risk_keywords:
        if word in text_lower:
            score["High Risk"] += 1
    for word in medium_risk_keywords:
        if word in text_lower:
            score["Medium Risk"] += 1
    for word in low_risk_keywords:
        if word in text_lower:
            score["Low Risk"] += 1

    return sorted(score.items(), key=lambda x: x[1], reverse=True)

text = st.text_area("Paste or describe the incident/problem:")

if text:
    result = score_text(text)
    st.subheader("Prediction")
    for label, count in result:
        if count > 0:
            st.write(f"**{label}**: {count} keyword match{'es' if count != 1 else ''}")
    if all(count == 0 for _, count in result):
        st.write("**No risk-related keywords detected.**")