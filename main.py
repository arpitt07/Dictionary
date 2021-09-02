import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(word):
	word = word.lower()
	if word in data:
		return data[word]
	elif len(get_close_matches(word, data.keys(), cutoff=0.8)) > 0:
		yn = input("do you mean %s instead? Enter Y if YES, or N if NO: " % get_close_matches(word,data.keys())[0])
		if yn in ["Y", "YES"]:
			return data[get_close_matches(word, data.keys())[0]]
		elif yn in ["N", "NO"]:
			return "There is no word like that. Please check again."
		else:
			return "We didn't understand your input. Please try the word again."
	else:
		return "There is no word like that. Please check again."


word = input("Enter the word: ")

output = translate(word)

if type(output) == list:
	for item in output:
		print(item)

else:
	print(output)
