# Risk Score Generator for Support Tickets

This AI-powered tool classifies incoming support messages by urgency and security relevance, then assigns a risk score based on category.

## Categories
- Urgent
- Security Breach
- Billing Problem
- Data Access Request
- General

## Example Risk Mapping
- Security Breach → 90/100
- Data Access Request → 75/100
- Urgent → 60/100
- Billing Problem → 50/100
- General → 10/100

## How to Use
1. Install dependencies:
```bash
pip install transformers torch
```

2. Run the script:
```bash
python risk_score.py
```

3. Paste in a support ticket or customer message and get a risk score.

---

Part of my AI + cybersecurity career rebuild series.