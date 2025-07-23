test_dict = {'Codingal': 3, 'is': 2, 'best': 2, 'for': 2, 'Coding': 1}
print("Test Dictionary:", test_dict)
key = input("Enter the word you want to check the frequency for: ")
if key in test_dict:
    print(f"The frequency of {key} is:", test_dict[key])
else:
    print(f"{key} is not found in the dictionary.")