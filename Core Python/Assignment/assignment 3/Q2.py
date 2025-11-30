alphabet = input("Enter an alphabet to check whether it is a vowel or consonant: ")

if alphabet.lower() in ('a', 'e', 'i', 'o', 'u'):
    print(alphabet, "is a vowel")
else:
    print(alphabet, "is a consonant")
    