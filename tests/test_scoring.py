from journal.scoring import classify

def test_classify():
    def test_classifier(text,top_k=None):
        return [{"label": "LABEL_2", "score": 0.98},
            {"label": "LABEL_1", "score": 0.01},
            {"label": "LABEL_0", "score": 0.01}
                ]
    assert classify(test_classifier, "test")[0] == "Positive"

