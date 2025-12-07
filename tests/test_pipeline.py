from journal.pipeline import run
import json

def test_pipeline(tmp_path,monkeypatch):
    entries = [
        {"entry": "I am crushing it 😁"},
        {"entry": "Today is crushing me 😭"},
        {"entry": "Feeling meh today 😐"},
        {"entry": "Great energy! 🔥"}
    ]
    input = "entries_test.json"
    output = "output_test.json"

    with open(input, "w", encoding="utf-8") as f:
        json.dump(entries,f)
    
    monkeypatch.setattr("journal.scoring.classify", lambda clf, text: "Positive")
    res = run(input,output)

    assert len(res) == 3
    assert res[0]["entry"] == "Today is crushing me 😭"
    assert res[-1]["entry"] == "Great energy! 🔥"