# moderation.py
# This file handles content moderation logic

import re

UNSAFE_WORDS = [
     "sexual", "erotic", "nudity",
    "rape", "abuse", "cocaine",
   "explicit", "Orgasm", "Porno", "Porn"
    "sex",
    "sexual",
    "erotic",
    "porno",
    "orgasm",
    "nudity",
    "explicit", "horror", "Horror"
]


def contains_unsafe_words(text):
    """
    Checks whether a given text contains unsafe words.
    Returns True if unsafe content is found.
    """

    if not isinstance(text, str):
        return False

    text = text.lower()

    for word in UNSAFE_WORDS:
        pattern = r"\b" + re.escape(word) + r"\b"
        if re.search(pattern, text):
            return True

    return False