"""import json

# Read JSON data from file
with open('data.json', 'r') as file:
    json_data = file.read()

# Parse JSON data into a Python dictionary
python_dict = json.loads(json_data)

print(python_dict)"""

import json
import difflib

def load_dictionary(json_file):
    with open(json_file, 'r') as f:
        data = json.load(f)
    return data

def get_word_definition(dictionary, word):
    #return dictionary.get(word, "Definition not found")
    word = word.lower()
    definition = dictionary.get(word)
    if definition is None:
        suggestions = difflib.get_close_matches(word, dictionary.keys(), n=3, cutoff=0.8)
        if suggestions:
            suggestion_str = ", ".join(suggestions)
            return "The word '{}' is not found in the dictionary. Did you mean: {}?".format(word, suggestion_str)
        else:
            return "The word '{}' is not found in the dictionary.".format(word)
    else:
        return "Definition of '{}': {}".format(word, definition)

# Example usage:
json_file = 'data.json'  # Path to your JSON file
dictionary = load_dictionary(json_file)
word = raw_input('enter a word:')
definition = get_word_definition(dictionary, word)
#print('Definition of "{}": {}'.format(word, definition))

print(definition)