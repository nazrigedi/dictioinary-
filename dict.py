import json
from difflib import get_close_matches

data=json.load(open("data.json"))
def define(w):
    w=w.lower()
    if w in data:
        return data[w]
    elif len(get_close_matches(w,data.keys())) >0:
         yn=input("did you mean %s instead? Enter Y if yes, or N if no: " % get_close_matches(w,data.keys())[0])
         if yn=="Y":
             return data[get_close_matches(w,data.keys())[0]]
         elif yn=="N":
             return "word doesnt exit"
         else:
             return "i cant help u , u shit"


    else:
        return "the word doesnt exist"
entry=input("input word: ")
output=define(entry)
if type(output)==list:
    for item in output:
        print(item)
else:
    print(output)
