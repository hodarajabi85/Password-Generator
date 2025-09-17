# 🔐 Password Generator
A Python project that provides flexible password generation utilities.
It includes three types of password generators:

* PinGenerator → Numeric PINs

* RandomPasswordGenerator → Strong random passwords (letters, numbers, symbols)

* MemorablePasswordGenerator → Easy-to-remember passwords using words

***
# 🚀 Features

* Abstract base class (PasswordGenerator) for consistency across all generators.

* Simple PIN generator for numeric codes.

* Random password generator with configurable length, numbers, and symbols.

* Memorable password generator using natural words (via nltk corpus).

* Easily extendable for custom password strategies.
***
# 🛠 Requirements

* Python 3.8+

* Jupyter Notebook (optional, if running inside .ipynb)

* Libraries:

  nltk

* random (standard library)

* string (standard library)

## Install dependencies:
pip install nltk

## First-time setup for NLTK words:
import nltk
nltk.download("words")

# 📖 Usage
## 1️⃣ PIN Generator
from password import PinGenerator

pin = PinGenerator(length=6)
print(pin.generate())   # Example: 482917

## 2️⃣ Random Password Generator
from password import RandomPasswordGenerator

rand_pass = RandomPasswordGenerator(length=10, include_numbers=True, include_symbols=True)
print(rand_pass.generate())   # Example: aB9$kfP1!Q

## 3️⃣ Memorable Password Generator
from password import MemorablePasswordGenerator

memorable = MemorablePasswordGenerator(number_of_words=5, separator="-", capitalize=True)
print(memorable.generate())   # Example: apple-Bridge-horse-dream-Cloud

***
# 📂 Project Structure
password-generator/
│
├── password.ipynb        # Notebook implementation
├── password.py           # Python module version (recommended for reuse)
├── README.md             # Documentation
└── requirements.txt      # Dependencies

# 📜 License

This project is open-source and available under the MIT License.