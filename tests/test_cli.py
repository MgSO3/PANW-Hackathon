import json
import pytest
from click.testing import CliRunner
from journal.cli import main

TEST_ENTRIES = [
    {"entry": "I am crushing it 😁"},
    {"entry": "Today is crushing me 😭"},
    {"entry": "Feeling meh today 😐"},
    {"entry": "Great energy! 🔥"}
]

@pytest.fixture
def setup_entries(tmp_path):
    input_file = tmp_path / "entries.json"
    output_file = tmp_path / "output.json"
    # Write test entries to a fresh file
    with open(input_file, "w", encoding="utf-8") as f:
        json.dump(TEST_ENTRIES, f)
    return str(input_file), str(output_file)

def test_cli_output(monkeypatch, setup_entries):
    input_file, output_file = setup_entries

    # Patch classify to always return Positive
    monkeypatch.setattr("journal.scoring.classify", lambda clf, text: "Positive")

    runner = CliRunner()
    result = runner.invoke(main, ["--input", input_file, "--output", output_file])

    assert result.exit_code == 0

    # Only check the last 3 entries
    for entry in TEST_ENTRIES[-3:]:
        assert entry["entry"] in result.output
