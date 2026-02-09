WAKE_WORDS = ["eva", "hey eva", "hi eva"]

def is_wake_word(text: str) -> bool:
    if not text:
        return False
    return any(w in text for w in WAKE_WORDS)
