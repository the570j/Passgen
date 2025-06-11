import itertools
import random
from colorama import Fore, Style, init
init(autoreset=True)

def leetify(word):
    leet = {'a': '@', 's': '$', 'i': '1', 'e': '3', 'o': '0', 'l': '1', 't': '7'}
    return ''.join(leet.get(c.lower(), c) for c in word)

def mutate(word, dob_parts):
    variations = set()
    year, year2, day, month = dob_parts.get("year", ""), dob_parts.get("year2", ""), dob_parts.get("day", ""), dob_parts.get("month", "")

    suffixes = [
        '', '123', '!', '@', '#', '$', '321', '###',
        year, year2, day+month, day, month,
        year + '!', '!' + year2, month + '123', day + '###'
    ]
    
    base = [word, word.lower(), word.upper(), word.capitalize(), word[::-1], leetify(word)]
    for w in base:
        for s in suffixes:
            variations.add(w + s)
            variations.add(s + w)
    return variations

def ask(question):
    return input(Fore.GREEN + "[?] " + question + ": ").strip()

def extract_dob_parts(dob):
    dob_parts = {}
    if len(dob) == 8 and dob.isdigit():
        dob_parts["day"] = dob[:2]
        dob_parts["month"] = dob[2:4]
        dob_parts["year"] = dob[4:]
        dob_parts["year2"] = dob[6:]
    return dob_parts

def generate_passwords(words, dob_parts, minlen=6, maxlen=20, limit=1000):
    all_variants = set()
    for word in words:
        all_variants.update(mutate(word, dob_parts))

    combos = set()

    for w in all_variants:
        if minlen <= len(w) <= maxlen:
            combos.add(w)
        if len(combos) >= limit:
            break

    for a, b in itertools.product(all_variants, repeat=2):
        pw = a + b
        if minlen <= len(pw) <= maxlen:
            combos.add(pw)
        if len(combos) >= limit:
            break

    return list(combos)

print(Fore.GREEN + Style.BRIGHT + "\n--- PassGen v1.0 ---\n")

name = ask("Full name")
nickname = ask("Nicknames (comma separated)").split(',')
dob = ask("Date of birth (DDMMYYYY)")
pet = ask("Pet names (comma separated)").split(',')
fav = ask("Favorite words, hobbies, teams (comma separated)").split(',')
location = ask("City or location names (comma separated)").split(',')
extra = ask("Other personal hints (comma separated)").split(',')

dob_parts = extract_dob_parts(dob)
words = [name] + nickname + pet + fav + location + extra
words = [w.strip() for w in words if w.strip()]

try:
    amount = int(ask("How many passwords to generate (e.g. 1000, 5000, 10000)"))
except:
    amount = 1000

print(Fore.GREEN + f"\n[+] Generating {amount} passwords...")

passwords = generate_passwords(words, dob_parts, limit=amount)

with open("password_list.txt", "w") as f:
    for pw in passwords:
        f.write(pw + "\n")

print(Fore.GREEN + f"[✓] {len(passwords)} passwords saved to password_list.txt\n")
