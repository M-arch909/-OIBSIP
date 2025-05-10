import random
letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
digits = "0123456789"
symbols = "!@#$%^&*()-_=+[]{};:,.<>?/"
length = int(input("Enter password length: "))
use_letters = input("Include letters? (Yes/No): ").strip().lower() == 'yes'
use_digits = input("Include numbers? (Yes/No): ").strip().lower() == 'yes'
use_symbols = input("Include symbols? (Yes/No): ").strip().lower() == 'yes'
pool = ""
if use_letters:
    pool += letters
if use_digits:
    pool += digits
if use_symbols:
    pool += symbols
if not pool:
    print("No character type selected. Using letters by default.")
    pool = letters
password = ''.join(random.choice(pool) for _ in range(length))
print("\nGenerated Password:", password)
