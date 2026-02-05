import difflib

WAKE_WORD = "eva"
ALIASES = ["eva", "ava", "ever", "evar", "e wa", "evaa"]

def is_wake_word(text: str) -> bool:
    if not text:
        return False

    text = text.lower().strip()

    # Direct match
    if WAKE_WORD in text:
        return True

    # Alias match
    for a in ALIASES:
        if a in text:
            return True

    # Fuzzy match (last resort)
    similarity = difflib.SequenceMatcher(None, text, WAKE_WORD).ratio()
    return similarity > 0.6
