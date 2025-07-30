import random
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
digits = '0123456789'
all_characters = uppercase_letters + lowercase_letters + digits
password_length = int(input("Enter the length of the password: "))
password = ''
for _ in range(password_length):
    password += random.choice(all_characters)
print("Generated Password:", password)
