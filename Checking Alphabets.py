def check_alphabet(ch):
    return ch.isalpha()
char = input("Enter a character: ")
if len(char) == 1:
    if check_alphabet(char):
        print(f"'{char}' is an alphabet.")
    else:
        print(f"'{char}' is not an alphabet.")
else:
    print("Please enter exactly one character.")