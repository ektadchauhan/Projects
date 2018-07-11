import json
from difflib import get_close_matches

mydata = json.load(open("data.json"))
ans = " "

def translate(w):
    w = w.lower()
    if w in mydata:
        return mydata[w]
    elif w.title() in mydata:   #if user entered "texas" this will check for "Texas" as well.
        return mydata[w]
    elif w.upper() in mydata:   #in case user enters words like USA or NATO
        return mydata[w]
    elif len(get_close_matches(w,mydata.keys())) > 0:
        correct_word = get_close_matches(w,mydata.keys())[0]
        ans = input("Did you mean %s instead? Enter Y for yes and N for exit" %correct_word)
        if ans == "Y":
            return mydata[correct_word]
        elif ans == "N":
            return "The word doesn't exist. Please double check it."
        else:
            return "We didn't understand your entry."
    else:
        return "The word doesn't exist. Please double check it."


word = input("enter key: ")

output = translate(word)
if type(output) == list:
    for i in output:
        print(i)
else:
    print(output)