import json,os
from gtts import gTTS
from difflib import get_close_matches
from playsound import playsound

def tts(text):
    conv=gTTS(text,lang='en',slow=False)
    conv.save("speech.mp3")
    playsound("speech.mp3")
    os.remove("speech.mp3")

#load JSON data
data = json.load(open("data.json")) 
def interactive_dict():
    
#take word from user
    tts('Enter the word to search for: ')
    word = input('Word→')
    #function call to get meaning of the word entered by user
    meaning = getMeaning(word)
#printing meaning of the word in console
    if type(meaning) == list:
        tts("The summary is as follows ")
        print("The summary is as follows ")
        for item in meaning:
            tts(item)
            print("\n" + item)
    else:
        tts("Terminating Program.")
        print("Program Terminated.")

#function to return meaning of the word from data
def getMeaning(w):
    #for case sensitivity
    w = w.lower()
    close_match=list()
    #if-else to check word exist in our data or not
    if w in data:
        tts("Word is : "+ data[w])
        return data[w]
    #give matching word
    elif len(get_close_matches(w,data.keys())) > 0:
        close_match = get_close_matches(w,data.keys())
        t=("Did you mean %s instead? Enter Y if yes or N if no: " % close_match)
        print(t)
        tts(t)
        choice = input()
        choice = choice.lower()
        if choice == 'y':
            tts("Enter the position of the word: ")
            c=int(input("\nIndex→"))
            c=c-1
            print("\nChosen word: " , close_match[c])
            return data[close_match[c]]
        elif choice == 'n':
            tts("The word doesn't exist. Please double check it.")
            cont_search()
            return "The word doesn't exist. Please double check it."
        else:
            tts("Sorry, We didn't understand your entry.")
            cont_search()
            return "Sorry, We didn't understand your entry."
    else:
        tts("The word doesn't exist. Please double check it.")
        cont_search()
        return "The word doesn't exist. Please double check it."


def cont_search():
    print("\nDo you want to continue search? 1. Yes 2. No")
    tts("Do you want to continue search? Enter 1. if Yes 2. if No")
    ch=input("Choice → ")
    if ch== "1":
        interactive_dict()
    else:
        return

interactive_dict()