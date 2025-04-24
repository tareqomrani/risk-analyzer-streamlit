import streamlit as st
from transformers import pipeline

# Force the pipeline to use CPU
classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli", device=-1)

# Risk-related categories
labels = ["Urgent", "Security Breach", "Billing Problem", "Data Access Request", "General"]

# Risk scoring map
risk_map = {
    "Security Breach": 90,
    "Data Access Request": 75,
    "Urgent": 60,
    "Billing Problem": 50,
    "General": 10
}

st.title("Risk Score Generator for Support Tickets")
st.write("Paste a support ticket message to get an AI-generated category and risk score.")

ticket = st.text_area("Ticket or Message", height=200)

if st.button("Generate Risk Score"):
    if ticket.strip():
        result = classifier(ticket, labels)
        top_label = result['labels'][0]
        confidence = result['scores'][0]
        risk_score = risk_map.get(top_label, 0)

        st.subheader("Classification Result")
        st.write(f"**Category:** {top_label}")
        st.write(f"**Confidence:** {confidence:.2f}")
        st.write(f"**Estimated Risk Score:** {risk_score}/100")
    else:
        st.warning("Please enter a support message to analyze.")