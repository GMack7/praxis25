word = input("Enter word: ")
first_letter = word[0]
rest_word = word[1:]
pig_latin = rest_word + first_letter + "ay"
print(pig_latin)