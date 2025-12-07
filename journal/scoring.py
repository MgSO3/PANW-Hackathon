def map_label(label): #Maps each label to the emotion from the pipeline
    label_map = {'LABEL_2': "Positive", 'LABEL_0': "Negative", 'LABEL_1': "Neutral"}
    return label_map.get(label,"Neutral")

def classify(classifier, text):
    if not text:
        return "Neutral", 100
    #Gets classifier result, with scoring for use in confidence and energy score
    result = classifier(text,top_k=None)
    #Creates map and chooses the largest one to predict the sentiment
    prob_map = {item['label']: item['score'] for item in result}
    max_label = max(prob_map,key = prob_map.get)
    max_score = prob_map[max_label]
    sentiment = map_label(max_label)
    #Sorts scores, chooses confidence to be the difference between the largest and second largest score.
    sorted_scores = sorted(prob_map.values(), reverse = True)
    confidence = (sorted_scores[0]**2 - sorted_scores[1]**2 - sorted_scores[2]**2)**(1/2)
    return sentiment, round(confidence*100)

def energy_score(classifier, text):
    if not text:
        return 50
    results = classifier(text,top_k = None)
    #Calculates energy score from 0 to 100 by scoring positive as 100, neutral as 50, and negative as 0
    prob_map = {item['label']: item['score'] for item in results}
    tot = prob_map.get("LABEL_2", 0)*100 + prob_map.get("LABEL_1", 0)*50
    return round(tot)