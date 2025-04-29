import streamlit as st
from transformers import pipeline

st.set_page_config(page_title="Risk Score Analyzer", layout="centered")
st.title("Risk Score Analyzer")

# Load the zero-shot classifier
@st.cache_resource
def load_classifier():
    return pipeline(
        "zero-shot-classification",
        model="facebook/bart-large-mnli",
        device=-1          # CPU inference
    )

classifier = load_classifier()

# Define the labels you want to classify into
labels = ["Low Risk", "Medium Risk", "High Risk"]

# User input
text = st.text_area("Paste or describe the incident/problem:")

# Run classification
if text:
    result = classifier(text, labels)
    st.subheader("Prediction")
    for lbl, score in zip(result["labels"], result["scores"]):
        st.write(f"**{lbl}**: {score:.2%}")
