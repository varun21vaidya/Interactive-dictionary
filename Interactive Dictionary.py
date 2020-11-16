import json
from difflib import get_close_matches #for getting suggestion for incorrect word
data=json.load(open(r"path\data.json"))
def explain(w):
    w=w.lower()        #to make case insensitive
    if w in data:          #to know the word exist in data
        return data[w]
    elif len(get_close_matches(w,data.keys())[0])>0:         #it gives number of suggestions ie > 0 & when of which generally first is correst hence [0]
        ans=input("did you mean %s Enter Y for yes and N for no " %get_close_matches(w,data.keys())[0])
        
        if ans=='y' or ans=="Y":
            return (data[get_close_matches(w,data.keys())[0]])
        elif ans=='n' or ans=="N":
            return 'the word does not exist, TRY AGAIN PLEASE'
        else:
            return 'did not get response TRY AGAIN'
    else:
        return 'the word does not exist, TRY AGAIN PLEASE'
word=input('\nenter the word to translate:')
print('\n',explain(word) )
