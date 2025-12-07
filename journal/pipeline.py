from transformers import pipeline
from .normalize import clean_text
from .scoring import classify, energy_score
from .storage import read,write,overwrite
from .logger import logger
def run(input = "entries.json", out = "output.json", model="cardiffnlp/twitter-roberta-base-sentiment"):
    # RoBERTa sentiment analysis pipeline
    logger.info("Starting sentiment analysis pipeline")
    try:
        classifier = pipeline("sentiment-analysis",model)
    except Exception as e:
        logger.critical("Failed to load sentiment model: %s", e)
        raise SystemExit("Cannot proceed without sentiment model")
    overwrite(out)
    logger.info(f"Cleared output file: {out}")
    entries = read(input) or []
    logger.info(f"Read {len(entries)} entries from {input}")
    output = []
    #Runs pipeline on every entry
    for i, row in enumerate(entries):
        text = clean_text(row["entry"])
        sentiment, confidence = classify(classifier,text)
        energy = energy_score(classifier,text)
        output.append({
            "entry" : row["entry"],
            "sentiment" : sentiment,
            "confidence" : confidence,
            "energy_score": energy
        })
        logger.info(f"Processed entry {i} : {row['entry'][:50]} -> Sentiment: {sentiment}, Energy Score: {energy_score}, Confidence: {confidence}")
    #Writes to output and returns last 3
    write(out,output)
    logger.info(f"Wrote {len(output)} entries to {output}")
    return output[-3:]
