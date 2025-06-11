# Passgen v1.0

**Passgen v1.0** is a smart password list generator that creates thousands of personalized password guesses based on names, dates of birth, pet names, hobbies, and other personal info. Perfect for ethical hacking, red teaming, OSINT, and cybersecurity training.

---

## Features

- Input personal info: names, nicknames, DOB, pet names, favorite hobbies, locations, and more  
- Parses DOB into day, month, year, last two digits, etc.  
- Generates a wide variety of password mutations and combos  
- Supports leet speak, reversed strings, capitalization variants, and common suffixes/prefixes  
- CLI interface with green color prompts for ease of use  
- Outputs password list to `password_list.txt`  
- Generate 1000+ passwords easily with custom limit  

---

## Installation & Usage

### Requirements

- Python 3.x  
- `colorama` Python package (for colored CLI)  
- Git (optional, for cloning repo)

---

### Clone, install dependencies, and run

#### Windows CMD (with Git installed)

```cmd
git clone https://github.com/yourusername/Passgen.git
cd Passgen
pip install -r requirements.txt
python Passgen.py

Windows CMD (without Git)

    Download ZIP from the GitHub repo:
    https://github.com/yourusername/Passgen

    Extract the ZIP and open CMD in that folder

    Run:

pip install -r requirements.txt
python Passgen.py

Linux / macOS Terminal

git clone https://github.com/the570j/Passgen
cd Passgen
pip3 install -r requirements.txt
python3 source.py

Running the script

The script will ask you several questions about personal information (name, DOB, pet names, etc.) and how many passwords to generate. After completion, the password list will be saved to password_list.txt.
Donations / Support

If you find this tool useful, consider supporting me:

    Solana (SOL): 41w1tuNRkw9fmrcLXntQZ8PsaMEeg9weofRvUk5NgmMN

    Ethereum (ETH): 0x5D6029cC4339d7Fc811F9c1A1b0aAefA66347f2D

    Bitcoin (BTC): bc1pynjsln94mmnthcfhwfmwce390hv5xngw90g58nne8cvmxwjqnpzscca7xl

License

This project is open source and free to use for ethical and educational purposes.
Disclaimer

Use responsibly. This tool is designed for security testing and educational use only. Do not use it for illegal activities.

Made with ❤️ by 570j
