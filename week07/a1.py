word = input("Enter word: ")
if word[0].lower()in ["a","e","i","o","u"]:
    print(word+"yay")
else: 
    print(word[1:]+word[0]+"ay")
