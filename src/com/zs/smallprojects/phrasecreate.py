def sentenceMaker(phrase):
    capitalized = phrase.capitalize()
    if phrase.startswith(("how", "what", "why")):
        return "{}?".format(capitalized)
    else:
        return "{}.".format(capitalized)

results = []

while True:
    userInput = input("Say something: ");
    if userInput == "/end":
        break
    else:
        results.append(sentenceMaker(userInput))
        continue

print(" ".join(results))