# Risk Score Analyzer

A Streamlit app that uses Hugging Face’s zero-shot classifier (`facebook/bart-large-mnli`) to score free-form text on a 3-level risk scale.

## Setup

1. Clone the repo
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the app:
   ```bash
   streamlit run risk_score_ui.py
   ```

## How It Works

- Loads the `facebook/bart-large-mnli` model
- Classifies any input text into **High Risk**, **Medium Risk**, or **Low Risk**
- Caches the model in memory for fast repeated inference

## License

MIT
