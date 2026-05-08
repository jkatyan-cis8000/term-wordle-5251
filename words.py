import random

# Common 5-letter English words (70 words, alphabetically sorted, no duplicates)
WORD_LIST = [
    "ABUSE", "ADULT", "AGENT", "ANGER", "AWARD", "BASIS", "BIRTH", "BLOCK", "BLOOD", "BOARD",
    "BRAIN", "BREAD", "BREAK", "BROWN", "BUYER", "CAUSE", "CHAIN", "CHAIR", "CHEST", "CHIEF",
    "CHILD", "CHINA", "CLAIM", "CLASS", "CLOCK", "COACH", "COAST", "COURT", "COVER", "CREAM",
    "CRANE", "CRASH", "CRIME", "CROSS", "CROWD", "CROWN", "CYCLE", "DANCE", "DEATH", "DEPTH",
    "DOUBT", "DRAFT", "DRAMA", "DREAM", "DRESS", "DRINK", "DRIVE", "EARTH", "ENEMY", "ENTRY",
    "ERROR", "EVENT", "FAITH", "FAULT", "FIELD", "FINAL", "FLOOR", "FOCUS", "FORCE", "FRAME",
    "FRANK", "FRONT", "FRUIT", "GLASS", "GRANT", "GREEN", "GROUP", "GUIDE", "HEART", "HORSE"
]

def get_daily_word() -> str:
    """Return a random 5-letter word from the word list."""
    return random.choice(WORD_LIST)

def is_valid_word(word: str) -> bool:
    """Check if a word is in the word list."""
    return word.upper() in WORD_LIST
