secret = input("Secret Phrase?")
first_two_letters = secret[:2]
last_two_letters = secret[-2:]
sentence = f"The treasure is buried in {first_two_letters}{last_two_letters}"
print(sentence)
