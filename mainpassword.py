"""
Author: Hoda Rajabi
Date created: 17/09/2025
Description: password generator
"""

import random
import string
from abc
import ABC, abstractmethod
import nltk
from typing import List, Optional


# --- Base Abstract Class ---
class PasswordGenerator(ABC):
    # Abstract class defining the interface for all password generators
    @abstractmethod
    def generate(self) -> str:
        # Generate and return a password string
        pass


# --- PIN Generator ---
class PinGenerator(PasswordGenerator):
    # Generates a numeric PIN with a fixed length
    def __init__(self, length: int) -> None:
        self.length: int = length  # length of the PIN

    def generate(self) -> str:
        # Generate a random PIN by picking digits repeatedly
        return "".join(random.choice(string.digits) for _ in range(self.length))


# --- Random Password Generator ---
class RandomPasswordGenerator(PasswordGenerator):
    # Generates a random password with optional numbers and symbols
    def __init__(self, length: int = 8, include_number: bool = False, include_symbol: bool = False) -> None:
        self.length: int = length
        self.characters: str = string.ascii_letters  # start with letters
        if include_number:
            self.characters += string.digits  # add digits if requested
        if include_symbol:
            self.characters += string.punctuation  # add symbols if requested

    def generate(self) -> str:
        # Randomly pick characters from the allowed set to form the password
        return "".join(random.choice(self.characters) for _ in range(self.length))


# --- Memorable Password Generator ---
class MemorablePasswordGenerator(PasswordGenerator):
    # Generates a password from real words for better memorability
    def __init__(
        self,
        number_of_words: int = 4,
        separator: str = "_",
        capitalize: bool = False,
        vocabulary: Optional[List[str]] = None
    ) -> None:
        if vocabulary is None:
            vocabulary = nltk.corpus.words.words()  # use NLTK words corpus if no custom vocabulary
        self.vocabulary: List[str] = vocabulary
        self.number_of_words: int = number_of_words
        self.capitalize: bool = capitalize
        self.separator: str = separator

    def generate(self) -> str:
        # Pick random words, optionally capitalize them, and join with a separator
        password_words: List[str] = [random.choice(self.vocabulary) for _ in range(self.number_of_words)]

        if self.capitalize:
            password_words = [
                word.upper() if random.choice([True, False]) else word.lower()
                for word in password_words
            ]

        return self.separator.join(password_words)
