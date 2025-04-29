#!/bin/bash
python -c "from transformers import pipeline; pipeline('zero-shot-classification', model='facebook/bart-large-mnli')"