from transformers import pipeline
from .normalize import clean_text
from .scoring import classify, energy_score
from .storage import read,write,overwrite

def run(input = "entries.json", out = "output.json"):
    # RoBERTa sentiment analysis pipeline
    classifier = pipeline("sentiment-analysis",model="cardiffnlp/twitter-roberta-base-sentiment")
    overwrite(out)
    entries = read(input) or []
    output = []
    #Runs pipeline on every entry
    for row in entries:
        text = clean_text(row["entry"])
        sentiment, confidence = classify(classifier,text)
        energy = energy_score(classifier,text)
        output.append({
            "entry" : row["entry"],
            "sentiment" : sentiment,
            "confidence" : confidence,
            "energy_score": energy
        })
    #Writes to output and returns last 3
    write(out,output)
    return output[-3:]
