# Mental Wellbeing Journal - CLI Sentiment Analyzer

## Overview
    This project is a command line journal tool that takes journal entries as input, and outputs an analysis of the sentiment of those entries. This is made to allow unorganized inputs with inconsistent grammar, slang, and emojis. 

    This tool uses the **RoBERTa sentiment analysis tool** from the HuggingFace `transformers` library to classify entries as Positive, Negative, or Neutral and calculates an energy score from 0 to 100.

---

## Installation
    1. Clone the repo
        ```bash
        git clone 
        cd journal
    2. Install dependencies
        pip install -r requirements.txt
    3. Run the CLI
        python -m journal
    4. Run test cases
        pytest
## Usage

    Adding entries
        Add entries by appending to `entries.json`
        Output is stored in `output.json`

    
## AI Disclosure
    This project was made using an AI sentiment analysis model from the HuggingFace `transformers` library. ChatGPT was used for data generation, research, and help understanding certain unfamiliar libraries. The final codebase is fully owned and validated by the developer.
## Notes 
    Sentiment Analysis is probabilistic, and a pre-trained model was used for the scores created. Therefore, some ambiguous entries are not always classified correctly. To combat this, I created the energy score and confidence interval, for more depth than just a qualitative output.
