import datetime
import os.path
import webbrowser as wb
from random import randint
from urllib.parse import quote_plus
import pyautogui
import pyttsx3
import speech_recognition as sr
import wikipedia
from googlesearch import search
import nltk

name = input('Your name: ')
engine = pyttsx3.init()
# Change how the Engine Sounds------------------------------------------------------------------------------------------
'''voices = engine.getProperty('voices')
if len(voices) > 1:
    engine.setProperty('voice', voices[1].id)
else:
    engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 145)
'''
# Functions Complimenting Engine Functioning----------------------------------------------------------------------------
def speak(audio=None):
    engine.say(audio)
    engine.runAndWait()
    return audio


def time():
    taime = datetime.datetime.now().strftime("%I:%M:%S %p")
    speak(f"It is Currently,{taime}")


def date():
    day: int = datetime.datetime.now().day
    month: int = datetime.datetime.now().month
    year: int = datetime.datetime.now().year
    speak(f"It is Currently,{day}, {month}, {year},in DDMMYYYY format")


def greet(_name):
    hour = datetime.datetime.now().hour
    if 6 <= hour < 12:
        speak(f"Good Morning, {_name}. Welcome to PulseAI! How may I help you?")
    elif 12 <= hour < 16:
        speak(f"Good Afternoon, {_name}. Welcome to PulseAI! How may I help you?")
    elif 16 <= hour <= 24:
        speak(f"Good Evening, {_name}. Welcome to PulseAI! How may I help you?")
    else:
        speak(f"Hello, {_name}. It's quite late! How can I assist you?")


def screenshot():
    image = pyautogui.screenshot()
    image_path = os.path.expanduser('~\\Pictures\\Screenshots\\PulseAI.png')
    image.save(image_path)
    os.startfile(image_path)


def command():
    recog = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recog.pause_threshold = 1
        audio = recog.listen(source)
    try:
        print("Recognizing...")
        _query = recog.recognize_google(audio)
        print(_query)
    except sr.UnknownValueError:
        speak("Sorry i didn't understand that")
        print("Sorry i didn't understand that")
        return "0"
    except sr.RequestError as error1:
        speak("Could not request results; {0}".format(error1))
        print("Could not request results; {0}".format(error1))
        return "2"
    except Exception as error2:
        speak(error2)
        print(error2)
        return "2"

    return _query


def song_google(_query):
    n_query = _query.split()
    n_query.pop(0)
    keywords = " ".join(n_query)
    urls = [url for url in search(keywords, num_results=1)]
    return urls[0]


if __name__ == '__main__':
    greet(name)
    while True:
        browser_path = r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe"
        wb.register('brave', None, wb.BackgroundBrowser(browser_path))
        query = command().lower()
        handled = False
        # Browsing-------------------------------------------------------------------------------------------------------
        websites = {
            "open google": "https://www.google.com",
            "open youtube": "https://www.youtube.com",
            "open facebook": "https://www.facebook.com",
            "open twitter": "https://www.twitter.com",
            "open instagram": "https://www.instagram.com",
            "open linkedin": "https://www.linkedin.com",
            "open reddit": "https://www.reddit.com",
            "open amazon": "https://www.amazon.in",
            "open flipkart": "https://www.flipkart.com",
            "open netflix": "https://www.netflix.com",
            "open gmail": "https://mail.google.com",
            "open yahoo": "https://www.yahoo.com",
            "open wikipedia": "https://www.wikipedia.org",
            "open pinterest": "https://www.pinterest.com",
            "open tumblr": "https://www.tumblr.com",
            "open bing": "https://www.bing.com",
            "open quora": "https://www.quora.com",
            "open stackoverflow": "https://stackoverflow.com",
            "open github": "https://github.com",
            "open medium": "https://medium.com",
            "open dropbox": "https://www.dropbox.com",
            "open spotify": "https://www.spotify.com",
            "open zoom": "https://zoom.us",
            "open slack": "https://slack.com",
            "open wordpress": "https://wordpress.com",
            "open times of india": "https://timesofindia.indiatimes.com",
            "open the hindu": "https://www.thehindu.com",
            "open indian express": "https://indianexpress.com",
            "open hindustan times": "https://www.hindustantimes.com",
            "open ndtv": "https://www.ndtv.com",
            "open zee news": "https://zeenews.india.com",
            "open economic times": "https://economictimes.indiatimes.com",
            "open india today": "https://www.indiatoday.in",
            "open news18": "https://www.news18.com"
        }

        for i in websites:
            if i in query:
                wb.open(websites[i])
                handled = True
                break
        else:
            pass
        # Conversational Responses---------------------------------------------------------------------------------------
        conversational_responses = {
            "hello": "Hello! How can I assist you today?",
            "hi": "Hi there! How can I help?",
            "hey": "Hey! What’s on your mind?",
            "how are you": "I'm here and ready to help! How about you?",
            "what's up": "Not much, just here to assist you. What about you?",
            "good morning": "Good morning! Hope your day is off to a great start!",
            "good afternoon": "Good afternoon! How can I help?",
            "good evening": "Good evening! How can I make your night easier?",
            "thank you": "You're very welcome! Anything else I can do?",
            "thanks": "No problem at all! Let me know if there's anything more.",
            "tell me a joke": "Why did the computer go to therapy? It had too many bytes!",
            "what's your name": "I'm your AI assistant! What's yours?",
            "who are you": "I'm here to help make your tasks easier!",
            "help": "Sure, I’m here to help! Just let me know what you need.",
            "what can you do": "I can answer questions, help with tasks, or just chat! What would you like?",
            "how do you work": "I use advanced algorithms to process information and provide useful responses!",
            "good": "I'm glad to hear that! Anything I can do to make it even better?",
            "bad": "I'm sorry to hear that. Is there something I can help with?",
            "tell me something": "Did you know? Honey never spoils. They found pots of it in ancient Egyptian tombs!",
            "i'm bored": "How about I tell you a fun fact or suggest something new?",
            "fun fact": "Did you know? Bananas are berries, but strawberries aren't!",
            "what's the weather": "I can check the current weather if you need! Just let me know where.",
            "how old are you": "I'm as old as the latest update! Age is just a concept for me.",
            "i love you": "That's sweet! I'm here for you, always.",
            "tell me a story": "Once upon a time, in the world of bits and bytes...",
            "motivate me": "Remember, every big journey starts with a single step. You’ve got this!",
            "what's your purpose": "I'm here to assist you in any way I can, making life easier and more fun!",
        }

        for i in conversational_responses:
            if i in query:
                print(conversational_responses[i])
                speak(conversational_responses[i])
                handled = True
                break
        else:
            pass
        # Song queries(Beta)-----------------------------------<<-x-UNDER CONSTRUCTION-x->>-----------------------------
        if 'play' in query:
            wb.open(song_google(query))
            handled = True
        # Other Queries-------------------------------------------------------------------------------------------------
        elif 'time' in query:
            time()
            handled = True
        elif 'date' in query:
            date()
            handled = True
        elif 'what is' in query:
            try:
                a = "give me a moment to gather my thoughts."
                b = "Ooh, you’re making me think on this one... let’s see!"
                choice = randint(0, 1)
                if choice == 0:
                    speak(a)
                else:
                    speak(b)
                query = query.split()
                query.pop(0)
                query.pop(0)
                query = " ".join(query).lower()
                results = wikipedia.search(query, 5)
                for i, j in zip(results, [i for i in range(1, 6)]):
                    print(j, i)
                    speak(i)
                else:
                    pass
                q_choice = int(input('your choice:')) - 1
                for i in results:
                    if results.index(i) == q_choice:
                        speak(i)
                        query = i
                        break
                else:
                    pass
                final_result = wikipedia.summary(query, sentences=10)
                print(final_result)
                speak(final_result)
                handled = True
            except Exception as e:
                print(e)
                speak(f"Sorry I can't answer that currently because of {e}")

        elif 'screenshot' in query:
            screenshot()
            handled = True

        elif 'open browser' in query:
            browser_path = "C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe"
            os.startfile(browser_path)
            handled = True

        elif 'remember that' in query:
            speak("what should i remember?")
            print("what should i remember?")
            rem_dat = str(command())
            rem_file = open('data.txt', 'a')
            rem_file.write(rem_dat + "\n")
            rem_file.close()
            print(f"i will now remember, {rem_dat}")
            speak(f"i will now remember, {rem_dat}")
            handled = True

        elif "do you remember" in query:
            rem_file = open('data.txt', 'r')
            rem_dat = rem_file.readlines()
            print("Yes, I'll read out what i remember.")
            speak("Yes, I'll read out what i remember.")
            for i in rem_dat:
                print(i)
                speak(i)
            rem_file.close()
            handled = True

        elif 'power off' in query:
            handled = True
            quit()

        if handled is False:
            print('Do you want to search this on google')
            speak('Do you want to search this on google')

            answer = command().lower()
            if "yes" in answer:
                encoded_query = quote_plus(query)
                encoded_query = "https://search.brave.com/search?q="+encoded_query
                wb.open(encoded_query)

            else:
                print("Alright!")
                speak("Alright!")
