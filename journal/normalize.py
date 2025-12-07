# Normalizes all entries to remove extra whitespace, and to handle empty files
def clean_text(text):

    if not text or not text.strip():

        return None
    
    text = text.strip()

    return text