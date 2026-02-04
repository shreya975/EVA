WAKE_WORD = "eva"

def is_wake_word(text: str) -> bool:
    return WAKE_WORD in text
