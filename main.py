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


def greet():
    hour = datetime.datetime.now().hour
    if 12 >= hour >= 6:
        speak(f"Good Morning,{name},Welcome to PulseAI, How may i help you?")
    elif 16 >= hour >= 12:
        speak(f"Good Afternoon,{name},Welcome to PulseAI, How may i help you?")
    elif 24 >= hour >= 16:
        speak(f"Good Evening,{name},Welcome to PulseAI, How may i help you?")


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
        query = recog.recognize_google(audio)
        print(query)
    except sr.UnknownValueError:
        speak("Sorry i didn't understand that")
        print("Sorry i didn't understand that")
        return 'Try Again'
    except sr.RequestError as e:
        speak("Could not request results; {0}".format(e))
        print("Could not request results; {0}".format(e))
    except Exception as e:
        speak(e)
        print(e)
        return "Try Again"

    return query


def song_google(query):
    nquery = query.split()
    nquery.pop(0)
    keywords = " ".join(nquery)
    urls = [url for url in search(keywords, num_results=1)]
    return urls[0]


if __name__ == '__main__':
    greet()
    while True:
        browser_path = r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe"
        wb.register('brave', None, wb.BackgroundBrowser(browser_path))
        query = command().lower()

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
                break
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
                break
        # Song queries(Beta)-----------------------------------<<-x-UNDER CONSTRUCTION-x->>-----------------------------
        if 'play' in query:
            wb.open(song_google(query))

        # Other Queries-------------------------------------------------------------------------------------------------
        elif 'time' in query:
            time()
        elif 'date' in query:
            date()
        elif 'what is' in query:
            try:
                a = "give me a moment to gather my thoughts."
                b = "Ooh, you’re making me think on this one... let’s see!"
                choice = randint(0, 1)
                if choice == 0:
                    speak(a)
                else:
                    speak(b)
                nquery = query.split()
                nquery.pop(0)
                nquery.pop(0)
                new_query = " ".join(nquery).lower()
                results = wikipedia.search(new_query, 5)
                for i, j in zip(results, [i for i in range(1, 6)]):
                    print(j, i)
                    speak(i)
                q_choice = int(input('your choice:')) - 1
                for i in results:
                    if results.index(i) == q_choice:
                        speak(i)
                        query = i
                final_result = wikipedia.summary(query, sentences=10)
                print(final_result)
                speak(final_result)

            except Exception as e:
                print(e)
                speak(f"Sorry I can't answer that currently because of {e}")

        elif 'screenshot' in query:
            screenshot()

        elif 'open browser' in query:
            browser_path = "C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe"
            os.startfile(browser_path)

        elif 'remember that' in query:
            speak("what should i remember?")
            print("what should i remember?")
            rem_dat = command()
            rem_file = open('data.txt', 'a')
            rem_file.write(rem_dat + "\n")
            rem_file.close()
            print(f"i will now remember, {rem_dat}")
            speak(f"i will now remember, {rem_dat}")

        elif "do you remember" in query:
            rem_file = open('data.txt', 'r')
            rem_dat = rem_file.readlines()
            speak("Yes, I'll read out what i remember.")
            for i in rem_dat:
                print(i)
                speak(i)
            rem_file.close()

        elif 'power off' in query:
            quit()

        else:
            print('Do you want to search this on google')
            speak('Do you want to search this on google')

            answer = command().lower()
            if "yes" in answer:
                encoded_query = quote_plus(query)
                encoded_query = "https://search.brave.com/search?q="+encoded_query
                wb.open(encoded_query)
            else:
                speak("Alright!")
                print("Alright!")
                pass
