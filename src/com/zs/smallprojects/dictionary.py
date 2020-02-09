import json
from difflib import get_close_matches

print("Welcome to the dictionary.  Enter a word or type '/exit' to quit.")

data = json.load(open("data.json"))

while True:
    def translate(word):
        word = word.lower()
        if word in data:
            return data[word];
        elif word.title() in data:
            return data[word.title()]
        elif word.upper() in data:
            return data[word.upper()]
        elif len(get_close_matches(word, data.keys())) > 0:
            choice = input("Did you mean %s? (y/n)  " % get_close_matches(word, data.keys())[0])
            if choice.lower() == "y":
                return data[get_close_matches(word, data.keys())[0]]
            else:
                return "The world is not in the dictionary."
        else:
            return "The word is not in the dictionary."
    
    word = input("Enter a word: ")
    
    output = translate(word)
    
    if isinstance(output, list):
        for item in output:
            print(item)
    else:
        print(output)
        
    yn = input("\nEnter a new word? (y/n)  ")
    if yn.lower() == "y":
        continue
    else:
        break
    
print("Goodbye")