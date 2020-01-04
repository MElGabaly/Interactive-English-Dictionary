# Imported Lib
import json
from difflib import get_close_matches

# Data Reading from the Json file (Function)
data = json.load(open("data.json"))


def search(user_input):
    user_input = user_input.lower()
    if user_input in data:
        return data[user_input]
    elif user_input.title() in data:
        return data[user_input.title()]
    elif user_input.upper() in data:
        return data[user_input.upper()]
    # To find a close match
    elif len(get_close_matches(user_input, data.keys())) > 0:
        close_word = get_close_matches(user_input, data.keys())[0]
        response = input("Did you mean '%s' instead? (Y/N) " % close_word)
        if response == "Y":
            return data[close_word]
        elif response == "N":
            return "Sorry we couldn't help you!! "
        else:
            return "Please Enter (Y) if Yes, or (N) if No"
    else:
        return "The Word Doesn't exist, Please Double check it"


# User Interfacing
user_input = input("Enter Word: ")

# output
outputs = search(user_input)

if type(outputs) == list:
    for output in outputs:
        print(output)
else:
    print(output)
