def map_label(label): #Maps each label to the emotion from the pipeline
    label_map = {'LABEL_2': "Positive", 'LABEL_0': "Negative", 'LABEL_1': "Neutral"}
    return label_map.get(label,"Neutral")

def classify(classifier, text):
    if not text:
        return "Neutral", 100
    result = classifier(text,top_k=None)
    prob_map = {item['label']: item['score'] for item in result}
    max_label = max(prob_map,key = prob_map.get)
    max_score = prob_map[max_label]
    sentiment = map_label(max_label)
    sorted_scores = sorted(prob_map.values(), reverse = True)
    if(len(sorted_scores) > 1):
        second = sorted_scores[1]
        confidence = max_score - second
    else:
        confidence = max_score
    return sentiment, round(confidence*100)

def energy_score(classifier, text):
    if not text:
        return 50
    results = classifier(text,top_k = None)

    prob_map = {item['label']: item['score'] for item in results}
    tot = prob_map.get("LABEL_2", 0)*100 + prob_map.get("LABEL_1", 0)*50
    return round(tot)