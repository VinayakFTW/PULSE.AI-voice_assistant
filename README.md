# PulseAI Voice-Activated Assistant

PulseAI is a voice-activated AI assistant developed in Python. It uses speech recognition to interact with users and perform various tasks like opening websites, providing conversational responses, fetching information from Wikipedia, playing songs(Beta), taking screenshots, and remembering user notes. Designed for a more personalized experience, PulseAI uses your name and responds based on the time of day.

## Features

- Voice Commands: Listens to user commands, interprets them, and takes appropriate actions.
- Greeting: Customizes greetings based on the time of day.
- Website Navigation: Opens popular websites by name (e.g., Google, YouTube, Wikipedia).
- Information Retrieval: Fetches summaries from Wikipedia for "what is" queries.
- Screenshot Capture: Takes a screenshot and saves it to the user’s Pictures directory.
- Memory: Remembers information upon request and recalls it when asked.
- Conversational Responses: Provides responses for casual conversations.
- Music Search: Finds and plays songs based on Google search.
- Date and Time: Reads the current date and time upon request.

## Requirements

To use PulseAI, make sure you have the following Python packages installed:

```bash
pip install pyttsx3 SpeechRecognition wikipedia-api pyautogui googlesearch-python spotipy pyaudio 
```

Also, PulseAI is configured to use Brave Browser for web searches. Ensure Brave is installed, or modify the path in the code to your preferred browser.

## Usage

1. Initialize:

- Run the program and enter your name when prompted to personalize the experience.

2. Commands:

- Greet: Just say "Hello," "Hi," or "Good Morning," etc.
- Ask the Time or Date: Use "What time is it?" or "What’s today’s date?"
- Open Websites: Say "Open [website name]" (e.g., "Open Google").
- Wikipedia Search: Say "What is [topic]" to get a Wikipedia summary.
- Take a Screenshot: Just say "Take a screenshot."
- Remember Notes: Say "Remember that [note]" to save information.
- Recall Notes: Use "Do you remember?" to hear stored information.
- Play a Song: Say "Play [song name]" to play a song on spotify.
- End Session: Say "Power off" to exit PulseAI.

3. Error Handling:

- If speech recognition fails or the request cannot be completed, PulseAI will inform you with a spoken error message.

## File Structure

1. main.py: The main file containing the code for the assistant.

2. data.txt: Stores notes or information you ask PulseAI to remember.


## Code Overview

1. Initialization: Configures the pyttsx3 engine and registers Brave Browser.

2. Main Functions:
    - speak(): Text-to-speech for spoken responses.
    - command(): Listens for user commands.
    - greet(): Provides time-based greetings.
    - song_play(): Plays a song on spotify.
        - wait_for_device(): A helper function to open spotify on a device if not already open.
            **IF DOWNLOADED FROM MICROSOFT STORE THEN REPLACE THE PATH WITH "start spotify"<br>if downloaded from the spotify website then simply replace with spotify.exe path on your system**
        - play_song(): The helper function that actually plays the song after connecting to the spotify api.
            **REPLACE THE "client_id" AND "client_secret" WITH YOUR ID AND API FROM https://developer.spotify.com**

3. Loop Execution: The main loop listens for commands and checks them against a set of conditions for executing specific tasks.

## Customization

You can customize PulseAI by:

- Adding more websites to the websites dictionary.
    **THIS WILL BE REPLACED BY A MORE GENERALISED WAY TO REDUCE EFFORT AND ASSIST BETTER**

- Expanding conversational_responses with additional responses.
    **THIS WILL BE REPLACED BY A GPT IN FUTURE UPDATES**

- Adjusting the speech rate or voice type in the speak() function.


**Troubleshooting**

- No Response to Commands: Ensure your microphone is working and configured correctly.

- Incorrect Recognition: If speech recognition accuracy is low, try speaking more clearly or adjusting recog.pause_threshold in the command() function.

- Missing Wikipedia Summaries: Make sure you have an internet connection for fetching data from Wikipedia.

## Spotify API Usage

This project utilizes the Spotify Web API to search for and play music. To use this application, you will need to generate your own API credentials from the <a href = "https://developer.spotify.com">Spotify Developer Dashboard.</a>

**Data Handling and Compliance**

- **No Data Ingestion**:This application does not ingest, store, cache, or copy any data returned by the Spotify API. All API calls are made in real-time to fulfill a user's direct action (e.g., searching for a song).

- **User Responsibility**:As a user of this project, you are responsible for creating and managing your own Spotify API keys and adhering to the <a href = "https://developer.spotify.com/terms">Spotify Developer Terms of Service.</a>



## Spotify API Usage

This project utilizes the Spotify Web API to search for and play music. To use this application, you will need to generate your own API credentials from the <a href = "https://developer.spotify.com">Spotify Developer Dashboard.</a>

**Data Handling and Compliance**

- **No Data Ingestion**:This application does not ingest, store, cache, or copy any data returned by the Spotify API. All API calls are made in real-time to fulfill a user's direct action (e.g., searching for a song).

- **User Responsibility**:As a user of this project, you are responsible for creating and managing your own Spotify API keys and adhering to the <a href = "https://developer.spotify.com/terms">Spotify Developer Terms of Service.</a>