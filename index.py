# Imported Lib
import json
from difflib import get_close_matches

# Data Reading from the Json file (Function)
data = json.load(open("data.json"))


def search(user_input):
    user_input = user_input.lower()
    if user_input in data:
        return data[user_input]
    # to find a close match
    elif len(get_close_matches(user_input, data.keys())) > 0:
        return "Did you mean %s instead?" % get_close_matches(user_input, data.keys())[0]
    else:
        return "The Word Doesn't exist, Please Double check it"


# User Interfacing
user_input = input("Enter Word: ")
print(search(user_input))
