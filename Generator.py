import random

digits = "0123456789"
lowercase_letters = "abcdefghijklmnopqrstuvwxyz"
uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
punctuation = "!#$%&*+-=?@^_"

chars = " "

n = int(input("Введите количество паролей для генерации: "))
length = int(input("Введите длину пароля: "))
add_digit = input("Включить цифры? (да = да, нет = нет) ").strip()
add_lowercase = input("Включить прописные буквы?").strip()
add_uppercase = input("Включить строчные буквы?").strip()
add_punctuation = input("Включить символы, такие как !#$%&*+-=?@^_?").strip()
remove_badsymbols = input("Исключить символы il1Lo0O?").strip()

if add_digit.lower() == "да":
    chars += digits
if add_lowercase.lower() == "да":
    chars += lowercase_letters
if add_uppercase.lower() == "да":
    chars += uppercase_letters
if add_punctuation.lower() == "да":
if remove_badsymbols.lower() == "да":
    for c in "il1Lo0O":
        chars = chars.replace(c, "")

def generate_password(length, chars):
    password = ""
    for j in range(length):
        password += random.choice(chars)
    return password

for _ in range(n):
    generate_password(length, chars)