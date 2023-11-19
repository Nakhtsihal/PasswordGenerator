import random

digits = "0123456789"
lowercase_letters = "abcdefghijklmnopqrstuvwxyz"
uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
punctuation = "!#$%&*+-=?@^_"

chars = " "

n = int(input("Enter number of passwords: "))
length = int(input("Enter length of passwords: "))
add_digit = input("Add digits? (yes | no)>>>").strip()
add_lowercase = input("Add upper letters?  (yes | no)>>>").strip()
add_uppercase = input("Add lower letters?  (yes | no)>>>").strip()
add_punctuation = input("Add symbols like? : !#$%&*+-=?@^_? (yes | no)>>>").strip()
remove_badsymbols = input("Exclude symbols? : il1Lo0O?  (yes | no)>>>").strip()

if add_digit.lower() == "yes":
    chars += digits
if add_lowercase.lower() == "yes":
    chars += lowercase_letters
if add_uppercase.lower() == "yes":
    chars += uppercase_letters
if add_punctuation.lower() == "yes":
    chars += punctuation
if remove_badsymbols.lower() == "yes":
    for c in "il1Lo0O":
        chars = chars.replace(c, "")

def generate_password(length, chars):
    password = ""
    for j in range(length):
        password += random.choice(chars)
    print(password)

for _ in range(n):
    generate_password(length, chars)