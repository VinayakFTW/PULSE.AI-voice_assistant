import datetime
import os.path
import time
import webbrowser as wb
from urllib.parse import quote_plus
import pyautogui
import pyttsx3
import speech_recognition as sr
import spotipy
import wikipedia
from spotipy.oauth2 import SpotifyOAuth

handled = False
name = input('Your name: ')
engine = pyttsx3.init()

# Change how the Engine Sounds------------------------------------------------------------------------------------------
"""
voices = engine.getProperty('voices')
if len(voices) > 1:
    engine.setProperty('voice', voices[1].id)
else:
    engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 175)
"""

# Functions Complimenting Engine Functioning----------------------------------------------------------------------------
def speak(_audio=None):
    engine.say(_audio)
    engine.runAndWait()
    return _audio


def time_tell():
    taime = datetime.datetime.now().strftime("%I:%M:%S %p")
    speak(f"It is Currently,{taime}")


def date_tell():
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
    global handled
    global listening
    _recog = sr.Recognizer()
    with sr.Microphone() as _source:
        print("Listening...")
        _recog.pause_threshold = 1
        _audio = _recog.listen(_source)
    try:
        print("Recognizing...")
        _query = _recog.recognize_google(_audio)
        print(_query)
    except sr.UnknownValueError:
        speak("Sorry i didn't understand that")
        print("Sorry i didn't understand that")
        handled = True
        listening = True
        return "0"
    except sr.RequestError as error1:
        speak("Could not request results; {0}".format(error1))
        print("Could not request results; {0}".format(error1))
        return "0"
    except Exception as error2:
        speak(error2)
        print(error2)
        return "0"

    return _query


def refine_query(_query):
    stop_words = {"tell", "what", 'find', 'search', 'play', 'is', 'me', 'open', 'please', 'for'}
    refined_query = [word for word in _query.split() if i not in stop_words]
    refined_query = " ".join(refined_query)
    return refined_query


def wikipedia_search(_query):
    try:
        speak("give me a moment to gather my thoughts.")
        results = wikipedia.search(_query, 5)
        for res, ind in zip(results, [ind for ind in range(1, 6)]):
            print(ind, res)
            speak(res)
        else:
            pass
        q_choice = int(input('your choice:')) - 1
        for res in results:
            if results.index(res) == q_choice:
                speak(res)
                _query = res
                break
        else:
            pass
        final_result = wikipedia.summary(_query, sentences=10)
        print(final_result)
        speak(final_result)

    except Exception as e:
        print(e)
        speak(f"Sorry I can't answer that currently because of {e}")


def song_play(_query):
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
        client_id="x",  # Replace with your client_id
        client_secret="x",  # Replace with your client secret
        redirect_uri="http://localhost:8080",
        scope="user-modify-playback-state user-read-playback-state"
    ))

    def wait_for_device():
        print("Waiting for Spotify to become active...")
        for _ in range(10):
            devices = sp.devices()
            device_list = devices.get('devices', [])

            if device_list:

                for device in device_list:
                    print(f"Active Device Found: {device['name']}")
                    return device['id']

            time.sleep(1)

        print("No active device found. Make sure Spotify is running and logged in.")
        return None

    def play_song(_query):

        os.startfile("C:\\Users\\vinay\\AppData\\Roaming\\Spotify\\Spotify.exe")

        device_id = wait_for_device()
        if not device_id:
            return

        results = sp.search(q=_query, type="track", limit=1)
        tracks = results.get('tracks', {}).get('items', [])

        if tracks:
            track = tracks[0]
            track_name = track['name']
            track_artist = ", ".join(artist['name'] for artist in track['artists'])
            track_id = track['id']

            print(f"Found Track: {track_name} by {track_artist}")
            sp.start_playback(device_id=device_id, uris=[f"spotify:track:{track_id}"])
            print(f"Playing {track_name} by {track_artist}")
        else:
            print(f"No track found for '{_query}'.")

    play_song(_query)


if __name__ == '__main__':

    greet(name)
    listening = True
    while True:
        browser_path = "C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe"
        wb.register('brave', None, wb.BackgroundBrowser(browser_path))
        query = command().lower()
        handled = False
        srch_key = ['what is', 'search']  # Search_keywords

        for i in srch_key:
            td_check = "time" not in query and "date" not in query
            if i in query and td_check:
                query = refine_query(query)
                wikipedia_search(query)
                listening = False
                handled = True
                break
            else:
                continue
        else:
            pass
        # Browsing-------------------------------------------------------------------------------------------------------
        websites = {
            "open maps": "https://www.google.com/maps",
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
                listening = False
                handled = True
                break
        else:
            pass
        # Conversational Responses---------------------------------------------------------------------------------------
        conversational_responses = {
            "hello": "Hello! How can I assist you today?",
            "hi": "Hi there! How can I help?",
            "hey": "Hey! What’s on your mind?",
            "how are you": "I'm good and ready to help! How about you?",
            "good morning": "Good morning! Hope your day is off to a great start!",
            "good afternoon": "Good afternoon! How can I help?",
            "good evening": "Good evening! How can I make your night easier?",
            "thank you": "You're very welcome! Anything else I can do?",
            "thanks": "No problem at all! Let me know if there's anything more.",
            "joke": "Why did the computer go to therapy? It had too many bytes!",
            "your name": "I'm your AI assistant! What's yours?",
            "who are you": "I'm here to help make your tasks easier!",
            "help": "Sure, I’m here to help! Just let me know what you need.",
            "what can you do": "I can answer questions, help with tasks, or just chat! What would you like?",
            "how do you work": "I use advanced algorithms to process information and provide useful responses!",
            "good": "I'm glad to hear that! Anything I can do to make it even better?",
            "bad": "I'm sorry to hear that. Is there something I can help with?",
            "i am bored": "How about I tell you a fun fact or suggest something new?",
            "fun fact": "Did you know? Bananas are berries, but strawberries aren't!",
            # "the weather": "I can check the current weather if you need! Just let me know where.",
            "how old are you": "I'm as old as the latest update! Age is just a concept for me.",
            "i love you": "That's sweet! I'm here for you, always.",
            "story": "Once upon a time, in the world of bits and bytes...",
            "motivate": "Remember, every big journey starts with a single step. You’ve got this!",
            "your purpose": "I'm here to assist you in any way I can, making life easier and more fun!",
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
            query = refine_query(query)
            song_play(query)
            listening = False
            handled = True

        # Other Queries-------------------------------------------------------------------------------------------------
        elif 'time' in query:
            time_tell()
            listening = False
            handled = True

        elif 'date' in query:
            date_tell()
            listening = False
            handled = True


        elif 'screenshot' in query:
            screenshot()
            listening = False
            handled = True

        elif 'open browser' in query:
            browser_path = "C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe"
            os.startfile(browser_path)
            listening = False
            handled = True

        elif 'remember that' in query:
            try:
                speak("what should i remember?")
                print("what should i remember?")
                rem_dat = str(command())
                rem_file = open('data.txt', 'a')
                rem_file.write(rem_dat + "\n")
                rem_file.close()
                print(f"i will now remember, {rem_dat}")
                speak(f"i will now remember, {rem_dat}")
                handled = True
            except Exception as ex:
                print(ex)
                speak(ex)
                handled = True
        elif "do you remember" in query:
            try:
                rem_file = open('data.txt', 'r')
                rem_dat = rem_file.readlines()
                print("Yes, I'll read out what i remember.")
                speak("Yes, I'll read out what i remember.")
                for i in rem_dat:
                    print(i)
                    speak(i)
                rem_file.close()
                handled = True
            except Exception as ex:
                print(ex)
                speak(ex)
                handled = True
        elif 'power off' in query:
            quit()

        if handled is False and query != "0":
            print('Do you want to search this on google')
            speak('Do you want to search this on google')

            while True:
                answer = command().lower()
                if "yes" in answer:
                    encoded_query = quote_plus(query)
                    encoded_query = "https://search.brave.com/search?q=" + encoded_query
                    wb.open(encoded_query)
                    listening = False
                    break
                elif "no" in answer:
                    print("Alright!")
                    speak("Alright!")
                    break
                else:
                    print('Please say "yes" or "no"')
                    speak("Please say yes or no")

        if listening is False:
            print("Waiting for 'wake up' or 'resume'...")

            with sr.Microphone() as source:
                recog = sr.Recognizer()
                while True:
                    try:
                        audio = recog.listen(source, timeout=5)
                        wake_up_command = recog.recognize_google(audio).lower()

                        if "wake up" in wake_up_command or "resume" in wake_up_command:
                            print("I'm back! How can I assist you?")
                            speak("I'm back! How can I assist you?")
                            listening = True
                            break

                    except:
                        continue
