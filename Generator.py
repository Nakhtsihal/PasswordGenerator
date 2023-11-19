import random

digits = "0123456789"
lowercase_letters = "abcdefghijklmnopqrstuvwxyz"
uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
punctuation = "!#$%&*+-=?@^_"

chars = " "

n = int(input("Введите количество паролей для генерации: "))
length = int(input("Введите длину пароля: "))
add_digit = input("Включить цифры? (д = да, н = нет) ").strip()
add_lowercase = input("Включить прописные буквы? (д = да, н = нет) ").strip()
add_uppercase = input("Включить строчные буквы? (д = да, н = нет)").strip()
add_punctuation = input("Включить символы, такие как !#$%&*+-=?@^_? (д = да, н = нет").strip()
remove_badsymbols = input("Исключить символы il1Lo0O? (д = да, н = нет)").strip()

