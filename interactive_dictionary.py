## Kawyn-S Interactive Dictionary

import json
from difflib import get_close_matches


dict_data = json.load(open("data.json", "r"))

def meaning(word):
    word = word.lower()
    if word in dict_data:
        return dict_data[word]
    elif word.title() in dict_data:
        return dict_data[word.title()] # if word has a format with the first letter uppercase like if you enter texas it will check for Texas
    elif word.upper() in dict_data:
        return dict_data[word.upper()] # in case user enters acronyms like "USA" or "NATO"
    elif len(get_close_matches(word, dict_data.keys())) > 0:
        yn = input("Did you mean %s instead? Enter Y if yes, N if no: " % get_close_matches(word, dict_data.keys())[0])
        if yn == "Y":
            return dict_data[get_close_matches(word, dict_data.keys())[0]]
        elif yn == "N":
            return "The word does not exist, please double check it"
        else:
            return "We didn't understand your query"
    else:
        return "This word doesn't exist, please recheck the word and type it again"

word = input("Enter a word: ")

output = meaning(word)

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
