import json
from difflib import get_close_matches

data=json.load(open("E:\Python programs\PYTHON_with_ardit\project_dictionary\data.json"))
data={k.lower():val for k,val in data.items()}
quit=""

def dictionary(word):
    word=word.lower()
    some_other_word=word[0].upper()+word[1:]
    if word in data:
        return data[word]

    elif some_other_word in data:
        return data[some_other_word]

    elif len(get_close_matches(word,data.keys()))>0:
        y_or_n=input("Ummm... Did you mean {}??  hit Y for yes or hit N for no    ".format(get_close_matches(word,data.keys())[0]))
        y_or_n=y_or_n.lower()
        if y_or_n=="y":
            return data[get_close_matches(word,data.keys())[0]]
        elif y_or_n=="n":
            return "Sorry, we couldn't get it, please try again"
        else:
            return "Sorry, please try again"
    else:
        return "Word not found, please check the word"


while quit!="q":
    print("\nPress 'q' to quit. ")
    any_word=input("\nEnter any word:  ")
    if any_word=="q":
        print("\nThanks for using Sagar's dictionary. See you! :) ")
        break

    elif any_word!="q":
        output=dictionary(any_word)

        count=0
        if type(output)==list:
            for i in output:
                count+=1
                print("{}  {} ".format(count,i))
        else:
            print(output)