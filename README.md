# Mental Wellbeing Journal - CLI Sentiment Analyzer
This project is a command line journal tool that takes journal entries as input, and outputs an analysis of the sentiment of those entries. This is made to allow unorganized inputs with inconsistent grammar, slang, and emojis. 

This tool uses the RoBERTa sentiment analysis tool from the HuggingFace transformers library to classify entries as Positive, Negative, or Neutral and calculates an energy score from 0 to 100, and includes a confidence percentage for each entry. 

---

## Installation
### 1. Clone the repository

git clone https://github.com/MgSO3/PANW-Hackathon

cd Mental-Wellbeing-Journal

### 2. Install dependencies

pip install -r requirements.txt

### 3. Run the CLI
python -m journal --input entries.json --output output.json

**OR**

pip install -e .

journal

### 4. Run tests

pytest
## Usage

Add entries by appending to `entries.json`
    Output is stored in `output.json`

    
## Design Choices and Methodology
This project was made using an AI sentiment analysis model from the HuggingFace `transformers` library. ChatGPT was used for data generation, research, and help understanding certain unfamiliar libraries. The final codebase is fully owned and validated by the developer.

I selected the RoBERTa emotion-analysis model by prompting ChatGPT for the best sentiment analysis model. I then checked to see that it was trained on a lot of social media style text, and would be a great model to use for this project. 

To design the pipeline, I separated functions into multiple files for proper organization. This allows me to easily navigate between files based on functionality.

To calculate energy score, I took the actual scores from the model, multiplied the positive score by 100 and the neutral score by 50, and added them to get an energy score.

To calculate confidence, I used the mean squared difference between the highest score and the lowest two scores.

To minimize messiness, I optimized for few commands to run the system, and to have an easily readable output. 

I decided to use click as well for robustness.


## Notes 
Sentiment Analysis is probabilistic, and a pre-trained model was used for the scores created. Therefore, some ambiguous entries are not always classified correctly. To combat this, I created the energy score and confidence interval, for more depth than just a qualitative output.
