#!/usr/bin/env python3

def word_count(text: str) -> dict:
    """Count how often each word appears in text (case-insensitive)."""
    counts = {}
    for word in text.lower().split():
        word = word.strip(".,!?;:\"'()")
        if word:
            counts[word] = counts.get(word, 0) + 1
    return counts


if __name__ == "__main__":
    print(word_count("The cat and the hat. The end!"))
