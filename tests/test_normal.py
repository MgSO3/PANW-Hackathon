from journal.normalize import clean_text

def test_clean_text_basic():
    assert clean_text("  hello 😎 ") == "hello 😎"


def test_clean_text_empty():
    assert clean_text("   ") is None
    assert clean_text("") is None