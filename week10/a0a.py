import json

data = {
    "names": ["Shane", "Oriane", "Kristin", "Gramond", "Amna", "Brandon"],
    "questions": [
        "Best Tacos in Town",
        "Best and Worse American State Flag Design",
        "Favorite Bad Movie",
        "Type of Cocktail or Mocktail You Would Be",
        "Your Superpower",
        "First Celebrity Crush",
        "Hobbies",
        "Fictional Character",
        "Favorite Color",
        "Favorite City to Visit"
    ],
    "responses": {
        "Who makes the best tacos in town?": {
            "Shane": "Tacos Gomez",
            "Oriane": "I don't think I've ever had a taco in my life, unfortunately.",
            "Kristin": "The only tacos I've had so far are from Torchy's but I'm sure they're not the best in town!",
            "Gramond": "Chipotle (I'm vegetarian, so limited options)",
            "Amna": ["They're all underseasoned!", "@Brandon, would love a demonstration!)"],
            "Brandon": "I do"
        },
        "Best and Worst American State Flag Design": {
            "Shane": 'Best are clearly Texas and New Mexico. Also Iowa. I have a weird soft spot for Iowa! Worst is Idaho, which incredibly contains the words "State of Idaho" twice.',
            "Oriane": "I really like Washington (looks really camp). Colorado looks really boring (also who thought the combination of red blue white YELLOW would be good?).",
            "Kristin": "Best is Oregon because the reverse of the flag has a beaver! Worst is Arkansas - I don't know, it's just a little boring?.",
            "Gramond": "I like the design of Maryland's flag. California is cool also. The worst flag is my home state of Alabama for its simplicity.",
            "Amna": "Best: New Mexico and the reverse side of Oregon. Worst: there is a dizzying array of red white and blue that's very hard to choose from."
        },
        "Favorite Bad Movie": {
            "Shane": "The Net (1995) -- I think this is the first depiction of a pizza being ordered through the Internet.",
            "Oriane": 'any Neil Breen movie is a gem. Personal favourites: Pass Thru (2016), Fateful Findings (2021). Favourite quote: "I resign today, as President of The Bank".',
            "Kristin": "Hercules Unchained (1959) -- I love this movie because it's featured on Mystery Science Theater 3000, where they spend the whole episode riffing on the movie.",
            "Gramond": "Shark Tale (2004)",
            "Emmy": "The Pink Panther (2006)",
            "Amna": "The Dictator (it pains me to acknowledge this publicly)"
        },
        "Type of Cocktail or Mocktail You Would Be": {
            "Oriane": '"Pikoù Panez Under the Sun": prosecco, vinho verde, (French) cider, lavender, rose, flower petals, orgeat, brown sugar, lime, chili powder.',
            "Kristin": 'something very sweet! My name would probably be something silly like "the most basic mocktail ever"',
            "Gramond": "I don't drink, so a virgin cocktail.",
            "Amna": '"Bil Batori": Iced black tea, rose water, lemon, ginger.'
        },
        "Your Superpower": {
            "Gramond": "Superspeed, because I like the ability to get anywhere within the blink of an eye.",
            "Shane": "charming regional accent",
            "Amna": "the ability to control probabilities",
            "Kristin": "the ability to fly!",
            "Oriane": "Understanding every language as if it was my own."
        },
        "First Celebrity Crush": {
            "Emmy": "Mitchell Musso",
            "Gramond": "Kyla Pratt",
            "Amna": "Hrithik Roshan",
            "Kristin": "Apolo Ohno",
            "Oriane": "Alyssa Milano."
        },
        "Hobbies": {
            "Emmy": "biking",
            "Gramond": "Watching sports (American football, basketball)",
            "Brandon": "playing music",
            "Amna": "painting",
            "Kristin": "baking",
            "Oriane": "Writing poetry."
        },        
        "Fictional Character": {
            "Amna": "Storm from X-men",
            "Kristin": "Winnie the Pooh",
            "Gramond": "The Fresh Prince (the character)",
            "Oriane": "She-Ra!"
        }, 
        "Favorite Color": {
            "Kristin": "blue",
            "Gramond": "blue",
            "Oriane": "Any pastel colour."
        },
        "Favorite City to Visit": {
            "Gramond": "London, England (Visited); Zweibrücken, Germany where I was born (Wish to Visit)",
            "Oriane": "Plougonvelin (Finistère), where my grandmother is from."
        }
    }
}

with open('week10/icebreaker.json', mode="w") as jsonfile:
    json.dump(data, jsonfile, indent=4)

with open('week10/icebreaker.json', mode="r") as jsonfile:
    datadict = json.load(jsonfile)

for questions in datadict["questions"]:
    print(f"    {questions}")


