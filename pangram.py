"""Verify if the sentence is a pangram"""
from string import ascii_lowercase

def is_pangram(sentence: str) -> bool:
    """Verify if the sentence is a pangram"""
    return set(ascii_lowercase).issubset(sentence.lower())
