import streamlit as st
from transformers import pipeline

st.set_page_config(page_title="Risk Analyzer", layout="centered")

@st.cache_resource
def load_classifier():
    return pipeline("zero-shot-classification", model="facebook/bart-large-mnli")

classifier = load_classifier()

st.title("Risk Score Analyzer")

labels = ["Low Risk", "Medium Risk", "High Risk"]

text = st.text_area("Paste or describe the incident/problem:")

if text:
    result = classifier(text, labels)
    st.write("### Prediction")
    for lbl, score in zip(result["labels"], result["scores"]):
        st.write(f"**{lbl}**: {score:.2%}")